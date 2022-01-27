import os
import AutoChromedriver
from selenium import webdriver
SELENIUM_GRID_HOST = os.environ.get('SELENIUM_GRID_HOST', 'localhost')


class E2E:
    def test_scores_service(self,url):
        AutoChromedriver.download_chromedriver(version="97.0.4692.71", location="/usr/bin")
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

        self.driver.get(url)
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

if __name__ == '__main__':
    w = E2E()
    w.main_function(url="http://127.0.0.1:5000/")