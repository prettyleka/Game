from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
TIME_TO_WAIT: int = 20

class E2E:
    def chrome_driver(self) -> WebDriver:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless")
        chrome_driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options)
        chrome_driver.implicitly_wait(TIME_TO_WAIT)
        return chrome_driver

    def test_scores_service(self):
        self.driver = self.chrome_driver()
        self.driver.get("http://127.0.0.1:5000/")
        text1 = self.driver.find_element(by="id", value='score')
        text2=text1.text
        if 1<int(text2)<1000:
            return True
        else:
            return False

    def main_function(self):
        if self.test_scores_service():
            return 0
        else:
            return -1
