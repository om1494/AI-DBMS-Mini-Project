# Contributing to AI Shopping Assistant

Thank you for your interest in contributing to the AI Shopping Assistant project! 🎉

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/AI-DBMS-Mini-Project.git
   cd Shopping_assistant
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ Development Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the database:**
   ```bash
   python setup_enhanced_database.py
   ```

3. **Run tests:**
   ```bash
   python test_db_connection.py
   ```

## 📝 How to Contribute

### 🐛 Reporting Bugs
- Use the GitHub issue tracker
- Describe the bug clearly
- Include steps to reproduce
- Add screenshots if applicable

### 💡 Suggesting Features
- Open a GitHub issue
- Describe the feature in detail
- Explain why it would be useful
- Consider implementation challenges

### 💻 Code Contributions

#### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions

#### Database Changes
- Update `schema.sql` for structural changes
- Update `seed.sql` for sample data changes
- Test database migrations thoroughly

#### UI Changes
- Maintain the dark theme consistency
- Ensure responsiveness across devices
- Test with different browsers
- Follow existing CSS patterns

#### Testing
- Test your changes thoroughly
- Run the existing test suite
- Add new tests for new features
- Ensure all quick commands work

## 🔄 Pull Request Process

1. **Update documentation** if needed
2. **Test your changes** thoroughly
3. **Commit your changes:**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
4. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a pull request** on GitHub

### Pull Request Guidelines
- Use a clear and descriptive title
- Describe your changes in detail
- Reference any related issues
- Include screenshots for UI changes
- Ensure tests pass

## 🏷️ Commit Message Format

Use clear and descriptive commit messages:
- `Add: new feature description`
- `Fix: bug description`
- `Update: what was updated`
- `Remove: what was removed`
- `Refactor: what was refactored`

## 📁 Project Structure

```
Shopping_assistant/
├── app.py                    # Main Streamlit app
├── database/
│   ├── chatbot/
│   │   └── chatbot_logic.py  # NLP logic
│   ├── db_config.py          # Database config
│   └── queries.py            # Database queries
├── schema.sql                # Database schema
├── seed.sql                  # Sample data
└── tests/                    # Test files
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Improve NLP accuracy
- [ ] Add more product categories
- [ ] Enhance error handling
- [ ] Mobile optimization

### Medium Priority
- [ ] Add product images
- [ ] Implement user favorites
- [ ] Add search filters
- [ ] Performance optimization

### Low Priority
- [ ] Voice search integration
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] API endpoints

## ❓ Questions?

If you have questions about contributing:
- Check existing GitHub issues
- Open a new discussion
- Contact the development team

## 🙏 Recognition

All contributors will be recognized in:
- The project README
- Release notes
- GitHub contributors page

Thank you for helping make AI Shopping Assistant better! 🌟