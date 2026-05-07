# Playwright Study Notes (Python) — Enhanced Version

---

## Table of Contents

1. What is Playwright?
2. System Requirements
3. Installing Python
4. Installing Playwright
5. Playwright Test (Basic)
6. Playwright with Pytest
7. Writing Your First Test
8. Pytest Execution Options
9. Project Structure Setup
10. Recording Scripts
11. Page Object Model (POM)
12. Trace Viewer
13. API Testing
14. APIRequestContext
15. Data-Driven Testing
16. Debugging & Troubleshooting
17. Best Practices
18. Playwright Advanced Features
19. CI/CD Integration Basics

---

## What is Playwright?

* Tool for end-to-end website testing
* Supports:

  * Chromium (Chrome, Edge)
  * WebKit (Safari)
  * Firefox
* Works on:

  * Windows, Linux, Mac
* Features:

  * CI/CD support (e.g., Jenkins)
  * Headless & headed execution
  * Mobile emulation

### 🔥 Additional Insights

* Supports **parallel test execution**
* Built-in **auto-waiting mechanism** (no need for explicit waits in most cases)
* Handles **iframes, multiple tabs, and network interception**

---

## System Requirements

* Minimum 4 GB RAM (8 GB recommended)
* ~1.5 GB disk space
* Stable internet

---

## Installing Python

*(Your original steps retained)*

### ✅ Additional Tip

* Prefer **Python 3.9+** for better compatibility
* Use `py -m pip install --upgrade pip` to keep pip updated

---

## Installing Playwright

*(Your original steps retained)*

### 🔥 Additional Commands

```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

👉 Useful if you want **specific browser installs only**

---

## Playwright Test (Basic)

*(Original retained)*

### ✅ Add a Minimal Example

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

## Playwright with Pytest

*(Original retained)*

### 🔥 Why Use Pytest?

* Parallel execution (`-n auto` with pytest-xdist)
* Fixtures = reusable setup
* Rich reporting ecosystem

---

## Writing Your First Test

*(Original retained)*

### ⚡ Important Concept: Auto-Waiting

Playwright automatically waits for:

* Elements to be visible
* Elements to be enabled
* Network stability

👉 This reduces flaky tests significantly

---

## Pytest Execution Options

*(Original retained)*

### 🔥 Additional Useful Flags

```bash
pytest -v                # verbose output
pytest -k "login"       # run specific tests
pytest -x               # stop on first failure
pytest --maxfail=2      # stop after 2 failures
pytest -n auto          # parallel execution (requires pytest-xdist)
```

---

## Project Structure Setup

*(Original retained)*

### ✅ Recommended Enhanced Structure

```
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

## Recording Scripts

*(Original retained)*

### ⚠️ Important Tip

* Codegen is **great for learning**
* But **should not be used directly in production tests**
* Always refactor into clean POM structure

---

## Page Object Model (POM)

*(Original retained)*

### 🔥 Best Practice Additions

* Keep **locators private**
* Expose only **actions (methods)**
* Avoid assertions inside page classes (keep them in tests)

---

## Trace Viewer

*(Original retained)*

### 🔥 Why It’s Powerful

* Shows:

  * DOM snapshots
  * Network requests
  * Console logs
* Helps debug **flaky tests easily**

---

## API Testing

*(Original retained)*

### 🔥 Add Assertions for Headers

```python
assert response.headers["content-type"] == "application/json"
```

---

## APIRequestContext

*(Original retained)*

### ⚠️ Common Mistake

* Using `json=` instead of `data=` in `.post()` (depends on API)
* Always check API docs

---

## Data-Driven Testing

*(Original retained)*

### 🔥 Best Practice

* Keep test data separate from test logic
* Use **fixtures + external files**

---

## Debugging & Troubleshooting

### Useful Debug Tools

```python
page.pause()
```

* Opens Playwright Inspector
* Lets you step through execution

```python
page.wait_for_timeout(5000)
```

* Temporary debugging (avoid in final code)

### Common Issues

| Issue             | Cause         | Fix                 |
| ----------------- | ------------- | ------------------- |
| Element not found | Wrong locator | Use `get_by_role()` |
| Timeout errors    | Slow page     | Increase timeout    |
| Flaky tests       | Timing issues | Use auto-waiting    |

---

## Best Practices

### ✅ Do’s

* Use **Page Object Model**
* Use **meaningful test names**
* Keep tests **independent**
* Use **fixtures for setup/teardown**

### ❌ Don’ts

* Avoid hard waits (`sleep`)
* Don’t duplicate locators
* Don’t mix test logic with page logic

---

## Playwright Advanced Features

### 1. Network Interception

```python
page.route("**/api/**", lambda route: route.continue_())
```

👉 Modify or block API calls

---

### 2. Handling Multiple Tabs

```python
new_page = context.wait_for_event("page")
```

---

### 3. File Upload

```python
page.set_input_files("input[type='file']", "file.txt")
```

---

### 4. Screenshots

```python
page.screenshot(path="screenshot.png")
```

---

### 5. Handling Alerts

```python
page.on("dialog", lambda dialog: dialog.accept())
```

---

## CI/CD Integration Basics

### Example: Run in CI

```bash
pytest --headless
```

### Jenkins / GitHub Actions Flow

1. Install dependencies
2. Install Playwright browsers
3. Run tests
4. Generate reports

---

### 🔥 Pro Tip

Use:

```bash
playwright install --with-deps
```

👉 Ensures CI environment works correctly

---

## Final Notes

* Playwright + Pytest is a **powerful combination**
* Focus on:

  * Clean structure
  * Reusability
  * Stability
* Avoid shortcuts → build scalable frameworks

---