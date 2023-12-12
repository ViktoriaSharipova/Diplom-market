from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "http://localhost:1111"
        self.quantity = 0


    def driverwait(self, locator):
        return WebDriverWait(self.browser, 20).until(ec.visibility_of_element_located(locator))

    def go_to_site(self):
        return self.browser.get(self.base_url)



