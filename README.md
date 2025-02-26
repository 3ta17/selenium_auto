## Selenium Python Test Automation

### Overview
This project automates UI testing for Python.org using Selenium and Python's `unittest` framework.

### Prerequisites
- Python 3.x
- Firefox with GeckoDriver
- `pip` installed

### Installation
```sh
git clone https://github.com/your-username/selenium_auto.git
cd selenium_auto
pip install selenium webdriver-manager unittest
```

### Usage
Run the test suite:
```sh
python test_script.py
```

### Test Actions
- Opens Python.org
- Verifies title
- Clicks "Downloads" and verifies content
- Clicks "Documentation" and verifies content

### Configuration
Runs in **headless mode**; remove `options.add_argument("--headless")` to disable.

### License
MIT License.
