# app.py
import streamlit as st
from chatbot.chatbot_logic import generate_reply

st.set_page_config(page_title="Shopping Assistant", layout="centered")
st.title("🛒 Shopping Assistant (Streamlit + MySQL)")
st.write("Type a query like: 'show mobiles under 20000', 'find Redmi', or 'search headphones'.")

if 'history' not in st.session_state:
    st.session_state.history = []

# chat input
user_text = st.chat_input("Ask me about products (e.g., 'show mobiles under 15000')")

if user_text:
    st.session_state.history.append(("user", user_text))
    result = generate_reply(user_text)
    if isinstance(result, dict):
        st.session_state.history.append(("bot", result['header']))
        for line in result['items']:
            st.session_state.history.append(("bot", line))
    else:
        st.session_state.history.append(("bot", result))

# display conversation
for sender, text in st.session_state.history[::-1]:
    if sender == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**ShopBot:** {text}")

st.markdown("---")
st.write("Phase 2: Database & basic rule-based chatbot are integrated.")
