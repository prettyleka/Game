import AutoChromedriver
from selenium import webdriver


class E2E:
    def test_scores_service(self):
        AutoChromedriver.download_chromedriver(version="97.0.4692.71", location="/usr/bin")
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        self.driver.get("http://127.0.0.1:5000/")
        text1 = self.driver.find_element(by="id", value='score')
        text2=text1.text
        if 1<int(text2)<1000:
            return True
        else:
            return False

    def main_function(self, url):
        if self.test_scores_service(url):
            return 0
        else:
            return -1
