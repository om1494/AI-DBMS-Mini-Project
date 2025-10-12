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
    cats = ['mobile', 'phone', 'laptop', 'headphone', 'headphones', 'tv', 'camera', 'watch', 'shoe', 'shoes','wearable','earbuds']
    s = msg.lower()
    for c in cats:
        if c in s:
            # normalize plural
            return c.rstrip('s')
    return None

def extract_name_like(msg):
    # pull words after keywords like "find", "search", "show me", or use first capitalized token
    s = msg.lower()
    m = re.search(r'(?:find|search|show|show me|i want)\s+(.*)', s)
    if m:
        candidate = re.split(r'\bunder\b|\bbelow\b|\bfor\b|\bwith\b', m.group(1))[0].strip()
        if candidate and len(candidate) > 2:
            return candidate
    # fallback: if user typed a brand/model like "redmi" or "hp"
    brands = ['redmi','samsung','hp','lenovo','boat','sony','noise','puma','realme','mi']
    for b in brands:
        if b in s:
            return b
    return None

def generate_reply(message):
    m = message.strip()
    if not m:
        return "Please type something like 'show mobiles under 20000' or 'find Redmi'."

    msg_low = m.lower()
    greetings = ['hi','hello','hey']
    if any(g in msg_low for g in greetings) and len(msg_low.split()) < 4:
        return "Hello! I'm ShopBot. Ask me to 'show mobiles under 20000', 'find headphones', or 'search Redmi'."

    price = extract_price(m)
    category = extract_category(m)
    name_like = extract_name_like(m)

    if not (price or category or name_like):
        # default fallback: ask clarifying question
        return "I can help you find products — try 'show mobiles under 15000' or 'find Redmi'."

    # Query DB
    products = search_products(category=category, max_price=price, name_like=name_like, limit=10)
    if not products:
        return "Sorry — no products matched. Try broader keywords or higher price."

    # Build structured response
    header = f"Found {len(products)} product(s). Showing top results (sorted by price):"
    # convert to readable lines
    lines = []
    for p in products:
        lines.append(f"{p['name']} — {p['category'].title()} — ₹{p['price']} — Stock: {p['stock']}")
    return {"header": header, "items": lines, "products": products}
