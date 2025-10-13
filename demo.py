# demo.py
# Demo script to showcase Shopping Assistant features

from database.chatbot.chatbot_logic import generate_reply
from database.queries import search_products
import time

def print_header(title):
    print("\n" + "="*60)
    print(f"🚀 {title}")
    print("="*60)

def print_products(products, limit=5):
    if not products:
        print("❌ No products found")
        return
    
    print(f"✅ Found {len(products)} products (showing top {min(limit, len(products))}):")
    for i, product in enumerate(products[:limit]):
        rating_stars = "⭐" * int(product.get('rating', 0))
        stock_status = "✅ In Stock" if product['stock'] > 0 else "❌ Out of Stock"
        print(f"   {i+1}. {product['name']} by {product.get('brand', 'Unknown')}")
        print(f"      💰 ₹{product['price']:,.0f} | {rating_stars} {product.get('rating', 0)}/5 | {stock_status}")
        print(f"      📝 {product.get('description', 'No description')[:80]}...")
        print()

def demo_search_functionality():
    print_header("Database Search Demo")
    
    # Test different search types
    search_tests = [
        ("Category Search", {"category": "mobile", "limit": 3}),
        ("Price Range Search", {"max_price": 20000, "limit": 5}),
        ("Brand Search", {"name_like": "samsung", "limit": 4}),
        ("Combined Search", {"category": "laptop", "max_price": 60000, "limit": 3})
    ]
    
    for test_name, params in search_tests:
        print(f"\n🔍 {test_name}:")
        print(f"   Query: {params}")
        products = search_products(**params)
        print_products(products, limit=3)
        time.sleep(1)

def demo_chatbot():
    print_header("Chatbot Natural Language Demo")
    
    # Test natural language queries
    queries = [
        "show mobiles under 25000",
        "find Samsung phones",
        "search Apple products", 
        "laptops below 50000",
        "headphones under 10000",
        "Nike shoes",
        "smartwatches under 30000",
        "TVs above 40000"
    ]
    
    for query in queries:
        print(f"\n💬 User: \"{query}\"")
        result = generate_reply(query)
        
        if isinstance(result, dict) and 'products' in result:
            print(f"🤖 Bot: {result['header']}")
            print_products(result['products'], limit=2)
        else:
            print(f"🤖 Bot: {result}")
        
        time.sleep(0.5)

def demo_statistics():
    print_header("Database Statistics")
    
    # Get category statistics
    from database.db_config import DB_CONFIG
    import mysql.connector
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Category counts
        cursor.execute("""
            SELECT category, COUNT(*) as count, 
                   AVG(price) as avg_price,
                   AVG(rating) as avg_rating
            FROM products 
            GROUP BY category 
            ORDER BY count DESC
        """)
        
        print("\n📊 Products by Category:")
        categories = cursor.fetchall()
        total_products = 0
        
        for category, count, avg_price, avg_rating in categories:
            total_products += count
            print(f"   📱 {category}: {count} products | Avg Price: ₹{avg_price:,.0f} | Avg Rating: {avg_rating:.1f}⭐")
        
        print(f"\n🎯 Total Products: {total_products}")
        
        # Price ranges
        cursor.execute("""
            SELECT 
                CASE 
                    WHEN price < 10000 THEN 'Under ₹10K'
                    WHEN price < 25000 THEN '₹10K - ₹25K'
                    WHEN price < 50000 THEN '₹25K - ₹50K'
                    WHEN price < 100000 THEN '₹50K - ₹1L'
                    ELSE 'Above ₹1L'
                END as price_range,
                COUNT(*) as count
            FROM products
            GROUP BY price_range
            ORDER BY MIN(price)
        """)
        
        print("\n💰 Products by Price Range:")
        for price_range, count in cursor.fetchall():
            print(f"   💵 {price_range}: {count} products")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error getting statistics: {e}")

def main():
    print("🛒 Shopping Assistant - Feature Demo")
    print("=" * 60)
    print("This demo showcases the enhanced Shopping Assistant with:")
    print("• 150 products across 6 categories")
    print("• Natural language search")
    print("• Advanced filtering")
    print("• Modern Streamlit UI")
    print("• Interactive features")
    
    # Run demos
    demo_statistics()
    demo_search_functionality()
    demo_chatbot()
    
    print_header("Demo Complete!")
    print("🎉 Your Shopping Assistant is ready!")
    print("💡 Start the web app with: python -m streamlit run app.py")
    print("🌐 Then open: http://localhost:8501")
    print("\n🚀 Made with ❤️ by Om & Dattaprasad")

if __name__ == "__main__":
    main()