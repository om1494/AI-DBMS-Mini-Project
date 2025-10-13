# setup_database.py
# Script to create database and set up tables

import mysql.connector
from mysql.connector import Error
import getpass

def setup_database():
    print("🚀 Shopping Assistant - Database Setup")
    print("=" * 50)
    
    # Get credentials (without specifying database first)
    host = input("MySQL Host (default: localhost): ") or "localhost"
    port = input("MySQL Port (default: 3306): ") or "3306"
    user = input("MySQL Username (default: root): ") or "root"
    password = getpass.getpass("MySQL Password: ")
    
    try:
        port = int(port)
    except ValueError:
        print("❌ Invalid port number")
        return
    
    print(f"\n🔄 Connecting to MySQL server as {user}@{host}:{port}...")
    
    try:
        # Connect to MySQL server (without specifying database)
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            print("✅ Connected to MySQL server!")
            
            # Create database
            print("🔄 Creating student_db database...")
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
                print("✅ Database 'student_db' created successfully!")
            except Error as e:
                print(f"⚠️  Database creation: {e}")
            
            # Switch to the database
            cursor.execute("USE student_db")
            
            # Create products table
            print("🔄 Creating products table...")
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS products (
              id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255) NOT NULL,
              category VARCHAR(100) NOT NULL,
              price DECIMAL(10,2) NOT NULL,
              stock INT DEFAULT 0,
              description TEXT,
              brand VARCHAR(100),
              rating DECIMAL(2,1) DEFAULT 0.0,
              image_url VARCHAR(500),
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
            """
            
            try:
                cursor.execute(create_table_sql)
                print("✅ Products table created successfully!")
            except Error as e:
                print(f"⚠️  Table creation: {e}")
            
            # Insert sample data
            print("🔄 Inserting sample products...")
            insert_sql = """
            INSERT INTO products (name, category, price, stock, description, brand, rating) VALUES
            ('Redmi Note 12', 'Mobile', 12999.00, 10, '6.67 inch AMOLED display, 128GB storage, 48MP camera', 'Redmi', 4.2),
            ('Samsung Galaxy A14', 'Mobile', 15999.00, 7, '48MP triple camera, 64GB storage, 5000mAh battery', 'Samsung', 4.0),
            ('Realme Narzo 50', 'Mobile', 11999.00, 5, 'MediaTek Helio G96, 6GB RAM, good battery life', 'Realme', 4.1),
            ('iPhone 13', 'Mobile', 59999.00, 3, 'A15 Bionic chip, 128GB, dual camera system', 'Apple', 4.6),
            ('OnePlus Nord CE 3', 'Mobile', 26999.00, 8, '6.7 inch display, Snapdragon 782G, 8GB RAM', 'OnePlus', 4.3),
            
            ('HP 15 Laptop', 'Laptop', 34999.00, 5, 'Intel i3-1215U, 8GB RAM, 512GB SSD, Windows 11', 'HP', 4.0),
            ('Lenovo Ideapad 3', 'Laptop', 37999.00, 3, 'AMD Ryzen 5, 8GB RAM, 512GB SSD', 'Lenovo', 4.2),
            ('Dell Inspiron 15', 'Laptop', 42999.00, 4, 'Intel i5, 8GB RAM, 1TB HDD, dedicated graphics', 'Dell', 4.1),
            ('MacBook Air M1', 'Laptop', 89999.00, 2, 'Apple M1 chip, 8GB RAM, 256GB SSD, 13.3 inch', 'Apple', 4.7),
            
            ('Boat Rockerz 450', 'Headphones', 1999.00, 20, 'Wireless over-ear headphones, 40mm drivers, 15hr battery', 'Boat', 4.1),
            ('Noise Buds VS102', 'Headphones', 1499.00, 35, 'In-ear TWS earbuds, 24hr playtime, IPX4', 'Noise', 3.9),
            ('Sony WH-CH720N', 'Headphones', 8999.00, 8, 'Noise cancelling, 35hr battery, V1 processor', 'Sony', 4.4),
            ('JBL Tune 510BT', 'Headphones', 2999.00, 15, 'Wireless on-ear headphones, JBL Pure Bass', 'JBL', 4.2),
            
            ('Sony Bravia 32 inch', 'TV', 24999.00, 3, '32 inch HD Ready Smart Android TV, X-Reality PRO', 'Sony', 4.3),
            ('Samsung 43 inch 4K', 'TV', 34999.00, 2, '43 inch Ultra HD Smart LED TV, HDR10+', 'Samsung', 4.2),
            ('Mi Smart Band 7', 'Wearable', 1999.00, 25, 'Fitness tracker, 1.62 inch display, 14 days battery', 'Xiaomi', 4.1),
            ('Apple Watch Series 8', 'Wearable', 41999.00, 5, 'GPS, 45mm, fitness tracking, ECG app', 'Apple', 4.5),
            
            ('Puma Running Shoes', 'Shoes', 2999.00, 12, 'Men sports shoes, comfortable cushioning', 'Puma', 4.0),
            ('Nike Air Max', 'Shoes', 7999.00, 8, 'Premium running shoes, Air Max technology', 'Nike', 4.4),
            ('Adidas Ultraboost', 'Shoes', 12999.00, 6, 'Energy return running shoes, Boost midsole', 'Adidas', 4.5)
            """
            
            try:
                cursor.execute(insert_sql)
                connection.commit()
                print("✅ Sample products inserted successfully!")
                
                # Count products
                cursor.execute("SELECT COUNT(*) FROM products")
                count = cursor.fetchone()[0]
                print(f"📊 Total products in database: {count}")
                
            except Error as e:
                print(f"⚠️  Data insertion: {e}")
            
            # Update config file
            config_content = f"""# database/db_config.py
# Database configuration for Shopping Assistant
DB_CONFIG = {{
    "host": "{host}",
    "user": "{user}",
    "password": "{password}",
    "database": "student_db",
    "port": {port}
}}"""
            
            print("\n📝 Updating database/db_config.py...")
            try:
                with open('database/db_config.py', 'w') as f:
                    f.write(config_content)
                print("✅ Database configuration updated successfully!")
            except Exception as e:
                print(f"❌ Failed to update config: {e}")
            
            cursor.close()
            connection.close()
            
            print("\n🎉 Database setup completed successfully!")
            print("📋 Next steps:")
            print("   1. Run: python test_db_connection.py")
            print("   2. If tests pass, run: streamlit run app.py")
            
            return True
            
    except Error as e:
        print(f"❌ Connection failed: {e}")
        
        if "Access denied" in str(e):
            print("💡 Please check your MySQL username and password")
        elif "Can't connect to MySQL server" in str(e):
            print("💡 Please make sure MySQL server is running")
        
        return False

if __name__ == "__main__":
    setup_database()