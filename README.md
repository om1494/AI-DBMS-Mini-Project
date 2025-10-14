<div align="center">

# 🛒 AI Shopping Assistant

### *Intelligent Product Discovery with Natural Language Processing*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://mysql.com)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

*A sophisticated chatbot that revolutionizes online shopping through conversational AI*

![Shopping Assistant Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=AI+Shopping+Assistant+Demo)

</div>

---

## 🌟 **Project Overview**

The **AI Shopping Assistant** is an advanced e-commerce chatbot that leverages natural language processing to help users discover products effortlessly. Built with modern web technologies and featuring a stunning dark-themed interface, this application demonstrates the power of conversational AI in online retail.

### 🎯 **Key Highlights**
- 🤖 **Smart NLP Engine** - Understands natural language queries
- 🌙 **Modern Dark UI** - Professional gradient-based design
- 📊 **Rich Database** - 150+ products across 6 categories
- ⚡ **Real-time Search** - Instant product discovery
- 🎨 **Interactive Interface** - Engaging user experience

---

## 🚀 **Features**

<table>
<tr>
<td width="50%">

### 🧠 **Intelligent Search**
- Natural language query processing
- Multi-criteria filtering (price, brand, category)
- Smart price extraction ("under 20k", "below 15000")
- Brand and category recognition
- Contextual search suggestions

</td>
<td width="50%">

### 🎨 **Modern Interface**
- Dark-themed professional design
- Interactive product cards with hover effects
- Real-time chat interface
- Responsive layout for all devices
- Smooth animations and transitions

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Rich Data**
- 150+ products across 6 categories
- Detailed product information
- Stock availability tracking
- Customer ratings and reviews
- Price comparison and sorting

</td>
<td width="50%">

### ⚡ **Performance**
- Fast database queries
- Optimized search algorithms
- Real-time updates
- Session management
- Error handling and recovery

</td>
</tr>
</table>

---

## 🛠️ **Technology Stack**

<div align="center">

| **Frontend** | **Backend** | **Database** | **AI/ML** |
|:---:|:---:|:---:|:---:|
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) | ![NLP](https://img.shields.io/badge/NLP-Rule--Based-brightgreen?style=for-the-badge) |
| Modern Web UI | Core Logic | Data Storage | Text Processing |

</div>

### **Additional Technologies**
- **CSS3** - Custom styling and animations
- **HTML5** - Markup and structure
- **JavaScript** - Interactive elements
- **Git** - Version control
- **Markdown** - Documentation

---

## 📁 **Project Architecture**

```
🛒 Shopping_assistant/
├── 📱 app.py                          # Main Streamlit application
├── 📋 requirements.txt                # Python dependencies
├── 🗃️ schema.sql                      # Database schema
├── 📦 seed.sql                        # Sample product data
├── ✅ test_db_connection.py           # Database connection tester
├── 🚀 setup_enhanced_database.py     # Enhanced database setup
├── 🎮 demo.py                        # Feature demonstration
├── ℹ️ about.py                        # About page
├── 📁 database/
│   ├── ⚙️ db_config.py               # Database configuration
│   ├── 📋 db_config_template.py      # Configuration template
│   ├── 🔍 queries.py                 # Database query functions
│   └── 🧠 chatbot/
│       └── 💬 chatbot_logic.py       # NLP and chatbot logic
└── 📖 README.md                      # Project documentation
```

---

## ⚡ **Quick Start**

### **Prerequisites**
- 🐍 Python 3.8 or higher
- 🗄️ MySQL Server 8.0+
- 💻 Modern web browser
- 🔧 Git (for cloning)

### **1. Clone Repository**
```bash
git clone https://github.com/om1494/AI-DBMS-Mini-Project.git
cd Shopping_assistant
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Database Setup**

#### **Option A: Automated Setup (Recommended)**
```bash
python setup_enhanced_database.py
```
*Follow the interactive prompts to configure your database*

#### **Option B: Manual Setup**
1. **Configure Database:**
   ```bash
   # Windows
   copy database\db_config_template.py database\db_config.py
   
   # Linux/Mac
   cp database/db_config_template.py database/db_config.py
   ```

2. **Edit Configuration:**
   ```python
   # database/db_config.py
   DB_CONFIG = {
       "host": "localhost",
       "user": "your_username",       # Your MySQL username
       "password": "your_password",   # Your MySQL password
       "database": "student_db",
       "port": 3306
   }
   ```

3. **Create Database:**
   ```bash
   mysql -u root -p < schema.sql
   mysql -u root -p < seed.sql
   ```

### **4. Test Connection**
```bash
python test_db_connection.py
```
*Should show ✅ for all tests*

### **5. Launch Application**
```bash
streamlit run app.py
```

🎉 **Open your browser to `http://localhost:8501`**

---

## 🎮 **Usage Guide**

### **💬 Natural Language Queries**
The AI understands human language! Try these examples:

<table>
<tr>
<th>Query Type</th>
<th>Example Queries</th>
<th>What It Does</th>
</tr>
<tr>
<td>💰 **Price-based**</td>
<td>

```
show mobiles under 25000
laptops below 50k
headphones less than 15000
```

</td>
<td>Filters by price range</td>
</tr>
<tr>
<td>🏷️ **Brand-based**</td>
<td>

```
find Samsung phones
search Apple products
Nike shoes
```

</td>
<td>Searches by brand name</td>
</tr>
<tr>
<td>📱 **Category-based**</td>
<td>

```
show all laptops
find TVs
search wearables
```

</td>
<td>Browse by product category</td>
</tr>
<tr>
<td>🔄 **Combined**</td>
<td>

```
Samsung mobiles under 30000
Apple laptops below 100000
Nike shoes under 10000
```

</td>
<td>Multiple criteria search</td>
</tr>
</table>

### **🚀 Quick Commands**
Click any of these sidebar buttons for instant results:
- 📱 **"show mobiles under 50000"**
- 🔍 **"find Samsung"**
- 🍎 **"search Apple"**
- 💻 **"laptops below 80000"**
- 🎧 **"headphones under 25000"**
- 👟 **"Nike shoes"**
- 📺 **"TVs above 25000"**
- ⌚ **"show wearables"**

---

## 📊 **Database Schema**

### **Products Table Structure**
```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    description TEXT,
    brand VARCHAR(100),
    rating DECIMAL(2,1) DEFAULT 0.0,
    image_url VARCHAR(500),
    specifications JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (category),
    INDEX idx_price (price),
    INDEX idx_brand (brand)
);
```

### **Data Distribution**
| **Category** | **Products** | **Price Range** | **Top Brands** |
|:---:|:---:|:---:|:---:|
| 📱 Mobile | 25 | ₹10,999 - ₹134,999 | Apple, Samsung, OnePlus |
| 💻 Laptop | 25 | ₹36,999 - ₹249,999 | Apple, Dell, HP, Lenovo |
| 🎧 Headphones | 25 | ₹1,499 - ₹59,999 | Sony, Apple, Bose |
| 📺 TV | 25 | ₹14,999 - ₹349,999 | Samsung, LG, Sony |
| ⌚ Wearable | 25 | ₹1,999 - ₹89,999 | Apple, Samsung, Garmin |
| 👟 Shoes | 25 | ₹2,995 - ₹17,999 | Nike, Adidas, Puma |

---

## 🧪 **Testing**

### **Comprehensive Test Suite**
```bash
# Test database connection and functionality
python test_db_connection.py

# Run feature demonstration
python demo.py
```

### **Test Coverage**
- ✅ Database connectivity
- ✅ Table structure validation
- ✅ Sample data verification
- ✅ Search functionality
- ✅ Natural language processing
- ✅ Error handling

---

## 👥 **Team & Development**

### **Project Team**
<table>
<tr>
<td align="center" width="50%">

**Om** 💻<br>
*Full-Stack Developer*
- Streamlit UI Design & Architecture
- Database Schema Development
- Natural Language Processing Logic
- Interactive Component Design
- CSS Styling & Dark Theme
- Product Search Implementation
- Testing & Quality Assurance

</td>
<td align="center" width="50%">

**Dattaprasad** 🚀<br>
*Full-Stack Developer*
- Backend Architecture & APIs
- Frontend User Experience
- MySQL Database Management
- Chatbot Logic & NLP Parsing
- Responsive Design Implementation
- Search Algorithm Optimization
- Documentation & Project Setup

</td>
</tr>
</table>

### **Development Phases**
- [x] **Phase 1:** Database Setup & Configuration
- [x] **Phase 2:** Core NLP & Search Logic
- [x] **Phase 3:** Streamlit UI Development
- [x] **Phase 4:** Enhanced Features & Dark Theme
- [x] **Phase 5:** Testing & Documentation
- [x] **Phase 6:** Final Polish & Optimization

---

## 🎯 **Key Achievements**

<div align="center">

### **📊 Project Statistics**

![Products](https://img.shields.io/badge/Products-150+-success?style=for-the-badge)
![Categories](https://img.shields.io/badge/Categories-6-blue?style=for-the-badge)
![Brands](https://img.shields.io/badge/Brands-20+-purple?style=for-the-badge)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-2000+-orange?style=for-the-badge)

</div>

### **✨ Features Implemented**
- ✅ **Natural Language Processing** - Rule-based query understanding
- ✅ **Advanced Search** - Multi-criteria product filtering
- ✅ **Modern UI/UX** - Dark theme with smooth animations
- ✅ **Real-time Updates** - Dynamic product information
- ✅ **Responsive Design** - Mobile and desktop compatibility
- ✅ **Error Handling** - Robust error management
- ✅ **Session Management** - Conversation history tracking
- ✅ **Performance Optimization** - Fast query execution

---

## 🚀 **Future Enhancements**

### **🎯 Short-term Goals**
- [ ] **Machine Learning Integration** - Advanced NLP models
- [ ] **User Authentication** - Personal accounts and preferences
- [ ] **Shopping Cart** - Add to cart functionality
- [ ] **Product Recommendations** - AI-powered suggestions

### **🌟 Long-term Vision**
- [ ] **Voice Search** - Speech-to-text integration
- [ ] **Image Search** - Visual product discovery
- [ ] **Multi-language Support** - International accessibility
- [ ] **Mobile App** - Native mobile experience
- [ ] **API Integration** - External service connectivity

---

## 🛡️ **System Requirements**

### **Minimum Requirements**
- **OS:** Windows 10, macOS 10.14, or Ubuntu 18.04+
- **Python:** 3.8 or higher
- **RAM:** 4 GB minimum, 8 GB recommended
- **Storage:** 1 GB free space
- **Network:** Internet connection for initial setup

### **Recommended Setup**
- **OS:** Latest version of Windows 11, macOS, or Ubuntu
- **Python:** 3.10 or higher
- **RAM:** 16 GB or more
- **Storage:** SSD with 5+ GB free space
- **Network:** High-speed broadband connection

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### **Ways to Contribute**
- 🐛 **Bug Reports** - Found an issue? Let us know!
- 💡 **Feature Requests** - Have an idea? Share it!
- 📖 **Documentation** - Help improve our docs
- 🧪 **Testing** - Help us test new features
- 💻 **Code** - Submit pull requests

### **Development Setup**
```bash
# Fork the repository
git fork https://github.com/om1494/AI-DBMS-Mini-Project

# Clone your fork
git clone https://github.com/yourusername/AI-DBMS-Mini-Project

# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Create a pull request
```

---

## 📞 **Support & Contact**

### **Getting Help**
- 📖 **Documentation** - Check this README first
- 🐛 **Issues** - Open a GitHub issue for bugs
- 💬 **Discussions** - Join our GitHub Discussions
- 📧 **Email** - Contact the development team

### **Useful Links**
- 🏠 **Homepage:** [Project Repository](https://github.com/om1494/AI-DBMS-Mini-Project)
- 👥 **Team Info:** [Meet the Team](TEAM.md)
- 📊 **Demo:** Try the live demo
- 📖 **Docs:** Detailed documentation
- 🎥 **Video:** Watch the demo video

---

## 📄 **License**

This project is developed for educational purposes as part of an AI-DBMS Mini Project. 

```
Educational License

Copyright (c) 2024 Shopping Assistant Team

This project is created for educational purposes only.
Not for commercial use without permission.
```

---

<div align="center">

## 🌟 **Acknowledgments**

*Special thanks to all the open-source projects that made this possible*

[![Streamlit](https://img.shields.io/badge/Thanks-Streamlit-red?style=flat-square)](https://streamlit.io)
[![MySQL](https://img.shields.io/badge/Thanks-MySQL-blue?style=flat-square)](https://mysql.com)
[![Python](https://img.shields.io/badge/Thanks-Python-yellow?style=flat-square)](https://python.org)

---

### 🚀 **Ready to Shop Smart?**

**[🎮 Try the Demo](http://localhost:8501)** • **[📖 Read the Docs](#)** • **[⭐ Star the Repo](https://github.com/om1494/AI-DBMS-Mini-Project)**

---

**Made with ❤️ by Om & Dattaprasad**

*"Revolutionizing e-commerce through conversational AI"*

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)
![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![AI](https://img.shields.io/badge/Powered%20by-AI-brightgreen.svg)

</div>
