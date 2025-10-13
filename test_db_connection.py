# test_db_connection.py
# Test database connection and basic functionality

import mysql.connector
from mysql.connector import Error
import sys
import os

# Add the current directory to Python path to import database modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from database.db_config import DB_CONFIG
except ImportError:
    print("❌ Error: database/db_config.py not found!")
    print("📋 Instructions:")
    print("1. Copy database/db_config_template.py to database/db_config.py")
    print("2. Update database/db_config.py with your MySQL credentials")
    print("3. Run this test again")
    sys.exit(1)

def test_connection():
    """Test basic database connection"""
    try:
        print("🔄 Testing database connection...")
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()[0]
            print(f"✅ Successfully connected to database: {database_name}")
            
            # Check MySQL version
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()[0]
            print(f"📋 MySQL version: {version}")
            
            return True
            
    except Error as e:
        print(f"❌ Database connection failed: {e}")
        return False
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def test_tables():
    """Test if tables exist and have data"""
    try:
        print("\n🔄 Testing database tables...")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        # Check if products table exists
        cursor.execute("SHOW TABLES LIKE 'products';")
        result = cursor.fetchone()
        
        if result:
            print("✅ Products table exists")
            
            # Count products
            cursor.execute("SELECT COUNT(*) FROM products;")
            count = cursor.fetchone()[0]
            print(f"📊 Total products in database: {count}")
            
            # Show sample products
            cursor.execute("SELECT name, category, price FROM products LIMIT 5;")
            products = cursor.fetchall()
            print("\n📋 Sample products:")
            for product in products:
                print(f"   - {product[0]} ({product[1]}) - ₹{product[2]}")
                
            return True
        else:
            print("❌ Products table does not exist")
            print("📋 Run the schema.sql file to create tables")
            return False
            
    except Error as e:
        print(f"❌ Table test failed: {e}")
        return False
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def test_search_functionality():
    """Test the search functionality"""
    try:
        print("\n🔄 Testing search functionality...")
        from database.queries import search_products
        
        # Test category search
        mobile_products = search_products(category='mobile', limit=3)
        print(f"✅ Found {len(mobile_products)} mobile products")
        
        # Test price search
        budget_products = search_products(max_price=20000, limit=5)
        print(f"✅ Found {len(budget_products)} products under ₹20,000")
        
        # Test brand search
        brand_products = search_products(name_like='samsung', limit=3)
        print(f"✅ Found {len(brand_products)} Samsung products")
        
        return True
        
    except Exception as e:
        print(f"❌ Search functionality test failed: {e}")
        return False

def test_chatbot_logic():
    """Test the chatbot parsing logic"""
    try:
        print("\n🔄 Testing chatbot logic...")
        from database.chatbot.chatbot_logic import generate_reply
        
        # Test queries
        test_queries = [
            "show mobiles under 15000",
            "find Samsung phones",
            "search headphones",
            "laptops below 50000"
        ]
        
        for query in test_queries:
            result = generate_reply(query)
            if isinstance(result, dict) and 'products' in result:
                print(f"✅ Query: '{query}' -> Found {len(result['products'])} products")
            else:
                print(f"⚠️  Query: '{query}' -> {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Chatbot logic test failed: {e}")
        return False

def main():
    """Run all database tests"""
    print("🚀 Shopping Assistant - Database Connection Test")
    print("=" * 50)
    
    # Test 1: Basic connection
    connection_ok = test_connection()
    
    if not connection_ok:
        print("\n❌ Database connection failed. Please check your configuration.")
        return
    
    # Test 2: Tables and data
    tables_ok = test_tables()
    
    if not tables_ok:
        print("\n📋 To set up the database:")
        print("1. Open your MySQL client (DBeaver, MySQL Workbench, or command line)")
        print("2. Run the schema.sql file to create tables")
        print("3. Run the seed.sql file to insert sample data")
        print("4. Run this test again")
        return
    
    # Test 3: Search functionality
    search_ok = test_search_functionality()
    
    # Test 4: Chatbot logic
    chatbot_ok = test_chatbot_logic()
    
    # Final results
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"   Database Connection: {'✅' if connection_ok else '❌'}")
    print(f"   Tables & Data:      {'✅' if tables_ok else '❌'}")
    print(f"   Search Functions:   {'✅' if search_ok else '❌'}")
    print(f"   Chatbot Logic:      {'✅' if chatbot_ok else '❌'}")
    
    if all([connection_ok, tables_ok, search_ok, chatbot_ok]):
        print("\n🎉 All tests passed! Your Shopping Assistant is ready to run.")
        print("💡 Start the app with: streamlit run app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")

if __name__ == "__main__":
    main()