# app.py
# Shopping Assistant - Modern UI with Enhanced Features

import streamlit as st
from database.chatbot.chatbot_logic import generate_reply
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Shopping Assistant", 
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for dark modern UI
st.markdown("""
<style>
    /* Global dark theme */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* Main styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2.5rem;
        text-align: center;
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 12px 40px rgba(0,0,0,0.3);
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        margin: 0;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.95;
        font-weight: 500;
    }
    
    /* Product cards - Dark theme */
    .product-card {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        border-radius: 18px;
        padding: 1.8rem;
        margin: 1.2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        border: 1px solid #4a5568;
        transition: all 0.3s ease;
    }
    
    .product-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 16px 48px rgba(102, 126, 234, 0.3);
        background: linear-gradient(135deg, #374151 0%, #4a5568 100%);
    }
    
    .product-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #f7fafc;
        margin-bottom: 0.6rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .product-brand {
        color: #81e6d9;
        font-weight: 600;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .product-price {
        font-size: 1.6rem;
        font-weight: 800;
        color: #68d391;
        margin: 0.8rem 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .product-rating {
        font-size: 1.2rem;
        margin: 0.5rem 0;
        color: #ffd700;
    }
    
    .product-stock {
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.8rem 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .in-stock {
        background: linear-gradient(45deg, #38a169, #48bb78);
        color: white;
        box-shadow: 0 4px 15px rgba(56, 161, 105, 0.3);
    }
    
    .low-stock {
        background: linear-gradient(45deg, #ed8936, #f6ad55);
        color: white;
        box-shadow: 0 4px 15px rgba(237, 137, 54, 0.3);
    }
    
    .out-stock {
        background: linear-gradient(45deg, #e53e3e, #fc8181);
        color: white;
        box-shadow: 0 4px 15px rgba(229, 62, 62, 0.3);
    }
    
    .product-description {
        color: #cbd5e0;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-top: 1rem;
        font-style: italic;
    }
    
    /* Quick command buttons */
    .quick-command {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.8rem 1.4rem;
        border-radius: 30px;
        font-weight: 600;
        margin: 0.4rem;
        cursor: pointer;
        transition: all 0.4s ease;
        font-size: 0.95rem;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
    }
    
    .quick-command:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
        transform: scale(1.08) translateY(-2px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
    }
    
    /* Chat messages */
    .chat-user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.2rem 1.8rem;
        border-radius: 25px 25px 8px 25px;
        margin: 1.2rem 0 1.2rem 4rem;
        max-width: 75%;
        margin-left: auto;
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.4);
        font-weight: 500;
    }
    
    .chat-bot {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        border: 1px solid #4a5568;
        color: #e2e8f0;
        padding: 1.2rem 1.8rem;
        border-radius: 25px 25px 25px 8px;
        margin: 1.2rem 4rem 1.2rem 0;
        max-width: 75%;
        box-shadow: 0 6px 25px rgba(0,0,0,0.3);
        font-weight: 500;
    }
    
    /* Statistics */
    .stat-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.8rem;
        border-radius: 18px;
        color: white;
        text-align: center;
        margin: 1.2rem 0;
        box-shadow: 0 8px 30px rgba(240, 147, 251, 0.3);
    }
    
    .stat-number {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.6rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .stat-label {
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 500;
    }
    
    /* Sidebar styling - Dark theme */
    .sidebar-section {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.2rem 0;
        border: 1px solid #4a5568;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        color: #e2e8f0;
    }
    
    .sidebar-section h3 {
        color: #81e6d9;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .sidebar-section p {
        color: #cbd5e0;
        font-size: 0.9rem;
    }
    
    /* Filter section */
    .filter-container {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 1.8rem;
        border-radius: 18px;
        margin: 1.5rem 0;
        border: 1px solid #4a5568;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        color: #e2e8f0;
    }
    
    /* No results */
    .no-results {
        text-align: center;
        padding: 4rem;
        color: #cbd5e0;
        font-size: 1.2rem;
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        border-radius: 20px;
        border: 1px solid #4a5568;
    }
    
    /* Welcome section */
    .welcome-section {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        color: #e2e8f0;
        border: 1px solid #4a5568;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    }
    
    .welcome-section h4 {
        color: #81e6d9;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    /* Loading animation */
    .loading-dots {
        display: inline-block;
        color: #81e6d9;
    }
    
    .loading-dots::after {
        content: '';
        animation: dots 2s infinite;
    }
    
    @keyframes dots {
        0%, 20% { content: ''; }
        40% { content: '.'; }
        60% { content: '..'; }
        80%, 100% { content: '...'; }
    }
    
    /* Override Streamlit defaults */
    .stSelectbox > div > div {
        background-color: #374151 !important;
        color: #e2e8f0 !important;
        border: 1px solid #4a5568 !important;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        font-weight: 600 !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2, #667eea) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5) !important;
    }
    
    .stMetric {
        background: linear-gradient(135deg, #2d3748 0%, #374151 100%) !important;
        padding: 1rem !important;
        border-radius: 15px !important;
        border: 1px solid #4a5568 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    
    .stMetric > div > div {
        color: #e2e8f0 !important;
    }
    
    .stMetric [data-testid="metric-value"] {
        color: #81e6d9 !important;
        font-weight: 700 !important;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .chat-user, .chat-bot {
            margin-left: 1rem;
            margin-right: 1rem;
            max-width: 90%;
        }
        
        .product-card {
            margin: 0.8rem;
            padding: 1.2rem;
        }
        
        .main-header h1 {
            font-size: 2.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'last_products' not in st.session_state:
    st.session_state.last_products = []
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "All"

# Helper function to render product card
def render_product_card(product):
    # Determine stock status
    stock_class = "out-stock"
    stock_text = "Out of Stock"
    if product['stock'] > 10:
        stock_class = "in-stock"
        stock_text = f"✅ In Stock ({product['stock']} units)"
    elif product['stock'] > 0:
        stock_class = "low-stock"
        stock_text = f"⚠️ Low Stock ({product['stock']} units)"
    else:
        stock_text = "❌ Out of Stock"
    
    # Generate rating stars
    rating = float(product.get('rating', 0))
    stars = "⭐" * int(rating) + "☆" * (5 - int(rating))
    
    # Format price
    price_formatted = f"₹{product['price']:,.0f}"
    
    card_html = f"""
    <div class="product-card">
        <div class="product-title">{product['name']}</div>
        <div class="product-brand">by {product.get('brand', 'Unknown')}</div>
        <div class="product-price">{price_formatted}</div>
        <div class="product-rating">{stars} {rating}/5</div>
        <div class="product-stock {stock_class}">{stock_text}</div>
        <div class="product-description">{product.get('description', 'No description available')}</div>
    </div>
    """
    return card_html

# Helper function to execute query
def execute_query(query):
    with st.spinner('🔍 Searching products...'):
        time.sleep(0.3)  # Brief pause for better UX
        result = generate_reply(query)
        
    if isinstance(result, dict) and 'products' in result:
        st.session_state.last_products = result['products']
        return result
    else:
        st.session_state.last_products = []
        return result

# Main header
st.markdown(
    """
    <div class="main-header">
        <h1>🛒 AI Shopping Assistant</h1>
        <p>Discover amazing products with natural language search • 150+ Products Available</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-section">
        <h3>🚀 Quick Commands</h3>
        <p>Click any command to search instantly!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick command buttons - optimized to always return results
    quick_commands = [
        "show mobiles under 50000",
        "find Samsung", 
        "search Apple",
        "laptops below 80000",
        "headphones under 25000",
        "Nike shoes",
        "TVs above 25000",
        "show wearables"
    ]
    
    for cmd in quick_commands:
        if st.button(cmd, key=f"cmd_{cmd}", use_container_width=True):
            # Execute the command
            result = execute_query(cmd)
            st.session_state.history.append(("user", cmd))
            st.session_state.message_count += 1
            
            # Add response to history
            if isinstance(result, dict):
                st.session_state.history.append(("bot", f"Found {len(result['products'])} products matching '{cmd}'"))
            else:
                st.session_state.history.append(("bot", str(result)))
            
            st.rerun()
    
    st.markdown("---")
    
    # Category filter
    st.markdown("""
    <div class="sidebar-section">
        <h3>📂 Browse Categories</h3>
    </div>
    """, unsafe_allow_html=True)
    
    categories = ["All", "Mobile", "Laptop", "Headphones", "TV", "Wearable", "Shoes"]
    selected_category = st.selectbox(
        "Select Category:",
        categories,
        index=categories.index(st.session_state.selected_category)
    )
    
    if selected_category != st.session_state.selected_category:
        st.session_state.selected_category = selected_category
        if selected_category != "All":
            query = f"show {selected_category.lower()}s"
            result = execute_query(query)
            st.session_state.history.append(("user", f"Browse {selected_category} category"))
            st.session_state.message_count += 1
            
            if isinstance(result, dict):
                st.session_state.history.append(("bot", f"Showing all {selected_category} products"))
            else:
                st.session_state.history.append(("bot", str(result)))
            
            st.rerun()
    
    st.markdown("---")
    
    # Statistics
    if st.session_state.message_count > 0:
        st.markdown("""
        <div class="sidebar-section">
            <h3>📊 Session Stats</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.metric("🗨️ Messages", st.session_state.message_count)
        st.metric("🤖 Bot Responses", len([msg for sender, msg in st.session_state.history if sender == "bot"]))
        st.metric("🛍️ Products Found", len(st.session_state.last_products))
    
    st.markdown("---")
    
    # Clear history button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.history = []
        st.session_state.message_count = 0
        st.session_state.last_products = []
        st.session_state.selected_category = "All"
        st.success("Chat history cleared!")
        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Chat input
    st.markdown("### 💬 Chat with ShopBot")
    user_input = st.chat_input(
        "Ask me anything! Try: 'show iPhone under 80000' or 'find gaming laptops'",
        key="main_chat_input"
    )
    
    if user_input:
        # Execute query
        result = execute_query(user_input)
        st.session_state.history.append(("user", user_input))
        st.session_state.message_count += 1
        
        # Add response to history
        if isinstance(result, dict):
            st.session_state.history.append(("bot", f"Found {len(result['products'])} products matching your search 🎯"))
        else:
            st.session_state.history.append(("bot", str(result)))
        
        st.rerun()
    
    # Display products if available
    if st.session_state.last_products:
        st.markdown(f"### 🛍️ Search Results ({len(st.session_state.last_products)} products found)")
        
        # Sort options
        sort_option = st.selectbox(
            "Sort by:",
            ["Price: Low to High", "Price: High to Low", "Rating: High to Low", "Name: A to Z"]
        )
        
        # Sort products
        products = st.session_state.last_products.copy()
        if sort_option == "Price: Low to High":
            products.sort(key=lambda x: float(x['price']))
        elif sort_option == "Price: High to Low":
            products.sort(key=lambda x: float(x['price']), reverse=True)
        elif sort_option == "Rating: High to Low":
            products.sort(key=lambda x: float(x.get('rating', 0)), reverse=True)
        elif sort_option == "Name: A to Z":
            products.sort(key=lambda x: x['name'])
        
        # Display products in grid
        for i in range(0, len(products), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(products):
                    with col:
                        st.markdown(render_product_card(products[i + j]), unsafe_allow_html=True)
    
    elif st.session_state.message_count > 0:
        st.markdown("""
        <div class="no-results">
            <h3>🔍 No products found</h3>
            <p>Try a different search or browse categories from the sidebar</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    # Chat history
    st.markdown("### 💭 Conversation History")
    
    if not st.session_state.history:
        st.markdown("""
        <div class="welcome-section">
            <h4>👋 Welcome!</h4>
            <p>Start chatting to see your conversation history here.</p>
            <p>Try the quick commands in the sidebar or type your own queries!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Display chat messages
        for sender, message in reversed(st.session_state.history[-10:]):  # Show last 10 messages
            if sender == "user":
                st.markdown(f'<div class="chat-user"><strong>You:</strong> {message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-bot"><strong>ShopBot:</strong> {message}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
footer_cols = st.columns(4)

with footer_cols[0]:
    st.markdown("**Status:** ✅ Online")

with footer_cols[1]:
    st.markdown(f"**Products:** 150 items")

with footer_cols[2]:
    st.markdown(f"**Database:** student_db")

with footer_cols[3]:
    st.markdown(f"**Version:** 3.0")

st.markdown(
    f"""
    <div style="text-align: center; padding: 1rem; color: #888; font-size: 0.9rem;">
        <p>🚀 Made with ❤️ by Om & Dattaprasad | AI-DBMS Mini Project | Last updated: {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    """, 
    unsafe_allow_html=True
)
