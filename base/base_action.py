from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    #
    def __init__(self, driver):
        self.driver = driver
    #使用显示等待查找元素,并返回元素
    def find_element(self, feature, timeout=10, poll=1):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))
    #点击
    def click(self, feature):
        self.find_element(feature).click()
    #输入
    def input(self, feature, content):
        self.clear(feature)
        self.find_element(feature).send_keys(content)
    #清空
    def clear(self, feature):
        self.find_element(feature).clear()
    #返回
    def press_back(self):
        self.driver.press_keycode(4)
    #确认
    def press_enter(self):
        self.driver.press_keycode(66)