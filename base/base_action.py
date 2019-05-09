from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.clear(feature)
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)