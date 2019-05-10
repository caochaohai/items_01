from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BaseAction:
    #
    def __init__(self, driver):
        self.driver = driver
    #使用显示等待查找元素,并返回元素

    def find_element(self, feature, timeout=10.0, poll=1.0):
        # allure.attach("查找元素", "按照时间%f频率%f" % timeout, poll)
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))
    #点击
    def click(self, feature):
        # allure.attach("点击", "查找元素点击" )
        self.find_element(feature).click()
    #输入
    def input(self, feature, content):
        self.clear(feature)
        self.find_element(feature).send_keys(content)
        # allure.attach("输入", "查找元素输入" % feature, content)
    #清空
    def clear(self, feature):
        self.find_element(feature).clear()
    #返回
    def press_back(self):
        self.driver.press_keycode(4)
    #确认
    def press_enter(self):
        self.driver.press_keycode(66)

    def find_toast_text(self, message):
        toast_xpath = By.XPATH, "//*[contains(@text,'" + message + "')]"
        print(toast_xpath)
        return self.find_element(toast_xpath, timeout=5.0, poll= 0.1).text

    def is_toast_exits(self, message):
        try:
            self.find_toast_text(message)
            return True
        except:
            return False