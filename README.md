# Playwright Study Notes (Python)

A beginner-friendly yet detailed guide for learning Playwright automation testing using Python and Pytest.

---

# 📚 Topics Covered

- Introduction to Playwright
- Python & Playwright Installation
- Browser Automation Basics
- Playwright with Pytest
- Writing Automated Tests
- Pytest Execution Commands
- Project Structure Setup
- Recording Scripts using Codegen
- Page Object Model (POM)
- Trace Viewer
- API Testing
- APIRequestContext
- Data-Driven Testing
- Debugging & Troubleshooting
- Playwright Best Practices
- Advanced Playwright Features
- CI/CD Integration Basics

---

# 🚀 Features

- Cross-browser automation
  - Chromium
  - Firefox
  - WebKit

- Supports:
  - Headless & headed execution
  - Parallel execution
  - API testing
  - Mobile emulation
  - Network interception
  - Screenshots & tracing

---

# 🛠️ System Requirements

- Python 3.9+
- Minimum 4 GB RAM (8 GB recommended)
- Stable internet connection

---

# 📦 Installation

## 1. Install Python

Download and install Python from the official website.

After installation, verify:

```bash
python --version
```

---

## 2. Install Playwright

```bash
pip install playwright
```

Install browsers:

```bash
playwright install
```

Optional browser-specific installs:

```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

---

## 3. Install Pytest

```bash
pip install pytest
```

Optional parallel execution support:

```bash
pip install pytest-xdist
```

---

# ▶️ Running Tests

Run all tests:

```bash
pytest
```

Useful execution options:

```bash
pytest -v
pytest -k "login"
pytest -x
pytest --maxfail=2
pytest -n auto
```

---

# 📁 Recommended Project Structure

```text
project/
│
├── tests/
├── pages/
├── utils/
├── test_data/
├── reports/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

# 🧪 Sample Playwright Script

```python
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        print(page.title())

        browser.close()

run()
```

---

# 🔥 Advanced Features

## Network Interception

```python
page.route("**/api/**", lambda route: route.continue_())
```

## Multiple Tabs

```python
new_page = context.wait_for_event("page")
```

## File Upload

```python
page.set_input_files("input[type='file']", "file.txt")
```

## Screenshots

```python
page.screenshot(path="screenshot.png")
```

## Handling Alerts

```python
page.on("dialog", lambda dialog: dialog.accept())
```

---

# 🐞 Debugging Tips

Pause execution:

```python
page.pause()
```

Temporary timeout:

```python
page.wait_for_timeout(5000)
```

---

# ✅ Best Practices

## Do's

- Use Page Object Model (POM)
- Keep tests independent
- Use meaningful test names
- Use fixtures for setup and teardown

## Don'ts

- Avoid hard waits (`sleep`)
- Avoid duplicate locators
- Don’t mix page logic with test logic

---

# 🔄 CI/CD Support

Example headless execution:

```bash
pytest --headless
```

Recommended for CI environments:

```bash
playwright install --with-deps
```

---

# 📖 Learning Notes

This repository is intended for:

- Learning Playwright step-by-step
- Practicing automation concepts
- Building scalable testing frameworks
- Understanding Pytest integration

---

# 📌 Final Notes

Playwright + Pytest provides a powerful modern automation framework with excellent stability and developer experience.

Focus on:
- Clean code
- Reusability
- Maintainability
- Stable automation practices

Happy Testing 🚀