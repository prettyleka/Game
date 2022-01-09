import selenium.webdriver.chrome.webdriver
import selenium.webdriver.remote.webelement


class E2E:
    def test_scores_service(self):
        self.driver = selenium.webdriver.chrome.webdriver.WebDriver('/home/user/Downloads/chromedriver')
        self.driver.get("http://172.17.0.2:5000/")
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

if __name__ == '__main__':
    w = E2E()
    w.main_function()