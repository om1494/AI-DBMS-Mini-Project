# credential_tester.py
# Interactive tool to test MySQL credentials

import mysql.connector
from mysql.connector import Error
import getpass

def test_credentials():
    print("🔧 MySQL Credential Tester")
    print("=" * 40)
    
    # Get credentials interactively
    host = input("MySQL Host (default: localhost): ") or "localhost"
    port = input("MySQL Port (default: 3306): ") or "3306"
    user = input("MySQL Username (default: root): ") or "root"
    password = getpass.getpass("MySQL Password: ")
    database = input("Database Name (default: student_db): ") or "student_db"
    
    try:
        port = int(port)
    except ValueError:
        print("❌ Invalid port number")
        return
    
    print(f"\n🔄 Testing connection to {user}@{host}:{port}/{database}...")
    
    try:
        # Test connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Get MySQL version
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()[0]
            
            # Check current database
            cursor.execute("SELECT DATABASE();")
            current_db = cursor.fetchone()[0]
            
            print(f"✅ Connection successful!")
            print(f"📋 MySQL version: {version}")
            print(f"📋 Current database: {current_db}")
            
            # Check if products table exists
            cursor.execute("SHOW TABLES LIKE 'products';")
            table_exists = cursor.fetchone()
            
            if table_exists:
                print("✅ Products table exists")
                cursor.execute("SELECT COUNT(*) FROM products;")
                count = cursor.fetchone()[0]
                print(f"📊 Products in database: {count}")
            else:
                print("⚠️  Products table does not exist - you need to run schema.sql")
            
            # Generate config file content
            config_content = f"""# database/db_config.py
# Database configuration for Shopping Assistant
DB_CONFIG = {{
    "host": "{host}",
    "user": "{user}",
    "password": "{password}",
    "database": "{database}",
    "port": {port}
}}"""
            
            print("\n📝 Your db_config.py should contain:")
            print("-" * 50)
            print(config_content)
            print("-" * 50)
            
            # Ask if user wants to update the file
            update = input("\n❓ Would you like me to update database/db_config.py? (y/N): ")
            if update.lower() == 'y':
                try:
                    with open('database/db_config.py', 'w') as f:
                        f.write(config_content)
                    print("✅ Updated database/db_config.py successfully!")
                except Exception as e:
                    print(f"❌ Failed to update file: {e}")
            
            cursor.close()
            connection.close()
            return True
            
    except Error as e:
        print(f"❌ Connection failed: {e}")
        
        # Common error suggestions
        if "Access denied" in str(e):
            print("💡 Suggestions:")
            print("   - Check your username and password")
            print("   - Make sure MySQL server is running")
            print("   - Try connecting with DBeaver first to verify credentials")
        elif "Unknown database" in str(e):
            print("💡 Suggestions:")
            print("   - Create the 'student_db' database first")
            print("   - Check if you're using the correct database name")
        elif "Can't connect to MySQL server" in str(e):
            print("💡 Suggestions:")
            print("   - Make sure MySQL server is running")
            print("   - Check if the host and port are correct")
        
        return False

if __name__ == "__main__":
    test_credentials()