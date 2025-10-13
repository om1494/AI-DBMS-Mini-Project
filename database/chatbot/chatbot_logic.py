# chatbot/chatbot_logic.py
import re
from database.queries import search_products

def extract_price(msg):
    # basic patterns: "under 20000", "below 15k", "less than 10000", "<=10000", "10000"
    s = msg.replace(',', '').lower()
    m = re.search(r'(?:under|below|less than|<=|<)\s*₹?\s*(\d{2,6})', s)
    if m:
        return float(m.group(1))
    m2 = re.search(r'(\d+)\s*[kK]\b', s)
    if m2:
        return float(m2.group(1)) * 1000
    # fallback: pick a standalone number if it makes sense
    m3 = re.search(r'\b(\d{3,6})\b', s)
    if m3:
        return float(m3.group(1))
    return None

def extract_category(msg):
    cats = ['mobile', 'phone', 'phones', 'laptop', 'laptops', 'headphone', 'headphones', 'tv', 'camera', 'watch', 'shoe', 'shoes','wearable','earbuds']
    s = msg.lower()
    for c in cats:
        if c in s:
            # normalize plural and map phones to mobile
            if c in ['phone', 'phones']:
                return 'mobile'
            elif c in ['laptops']:
                return 'laptop'
            elif c in ['headphones', 'earbuds']:
                return 'headphones'
            elif c in ['shoes']:
                return 'shoes'
            else:
                return c.rstrip('s')
    return None

def extract_name_like(msg):
    # pull words after keywords like "find", "search", "show me", or use first capitalized token
    s = msg.lower()
    
    # Skip generic category words
    category_words = ['mobiles', 'mobile', 'phones', 'phone', 'laptops', 'laptop', 'headphones', 'headphone', 'tvs', 'tv', 'wearables', 'wearable', 'shoes', 'shoe']
    
    m = re.search(r'(?:find|search|show|show me|i want)\s+(.*)', s)
    if m:
        candidate = re.split(r'\bunder\b|\bbelow\b|\bfor\b|\bwith\b', m.group(1))[0].strip()
        if candidate and len(candidate) > 2 and candidate not in category_words:
            return candidate
    
    # fallback: if user typed a brand/model like "redmi" or "hp"
    brands = ['redmi','samsung','hp','lenovo','boat','sony','noise','puma','realme','mi','apple','oneplus','dell','jbl','nike','adidas','xiaomi']
    for b in brands:
        if b in s:
            return b
    return None

def generate_reply(message):
    m = message.strip()
    if not m:
        return "Please type something like 'show mobiles under 20000' or 'find Samsung phones'."

    msg_low = m.lower()
    greetings = ['hi','hello','hey','good morning','good evening']
    if any(g in msg_low for g in greetings) and len(msg_low.split()) < 4:
        return "Hello! I'm ShopBot 🛒. Ask me to 'show mobiles under 20000', 'find headphones', or 'search Samsung phones'."

    # Handle thanks
    if any(word in msg_low for word in ['thank', 'thanks']):
        return "You're welcome! 😊 Need help finding anything else?"

    price = extract_price(m)
    category = extract_category(m)
    name_like = extract_name_like(m)

    if not (price or category or name_like):
        # default fallback: ask clarifying question
        return "I can help you find products! Try: 'show mobiles under 15000', 'find Samsung phones', or 'search headphones'."

    # Query DB
    products = search_products(category=category, max_price=price, name_like=name_like, limit=10)
    if not products:
        suggestions = []
        if price:
            suggestions.append(f"try increasing your budget above ₹{int(price)}")
        if category:
            suggestions.append(f"search in other categories besides {category}")
        if name_like:
            suggestions.append(f"try different brands or keywords instead of '{name_like}'")
        
        suggestion_text = " or ".join(suggestions) if suggestions else "try different search terms"
        return f"Sorry, no products matched your search. You could {suggestion_text}."

    # Build structured response with enhanced formatting
    header = f"Found {len(products)} product(s) matching your search 🎯"
    # convert to readable lines with enhanced information
    lines = []
    for p in products:
        rating_stars = "⭐" * int(p.get('rating', 0)) if p.get('rating') else ""
        stock_status = "✅ In Stock" if p['stock'] > 0 else "❌ Out of Stock"
        brand_info = f"by {p.get('brand', 'Unknown')}" if p.get('brand') else ""
        
        line = f"**{p['name']}** {brand_info}"
        line += f"\n   💰 ₹{p['price']} | 📦 {stock_status} ({p['stock']} units)"
        if rating_stars:
            line += f" | {rating_stars} {p.get('rating', 0)}/5"
        if p.get('description'):
            line += f"\n   📝 {p['description'][:100]}{'...' if len(p['description']) > 100 else ''}"
        
        lines.append(line)
    
    return {"header": header, "items": lines, "products": products}
