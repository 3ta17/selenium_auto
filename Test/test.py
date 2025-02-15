import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # ヘッドレスモードを有効化（CIで実行するため）
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.quit()  # `quit()` を使って全プロセスを閉じる

    def test_python_org(self):
        self.driver.get("http://www.python.org")

        # タイトルチェック
        self.assertIn("Python", self.driver.title)

        # "Downloads" リンクをクリック
        self.driver.find_element(By.LINK_TEXT, "Downloads").click()

        # 指定の要素が表示されるまで待機
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "widget-title"))
        )
        self.assertEqual('Looking for a specific release?', element.text)

        # "Documentation" リンクをクリック
        self.driver.find_element(By.LINK_TEXT, "Documentation").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "call-to-action"))
        )
        self.assertIn("Browse the docs", element.text)

if __name__ == "__main__":
    unittest.main()
