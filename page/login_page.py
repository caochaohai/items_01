
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class LoginPage(BaseAction):

    phone_input = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_input = By.ID, "com.tpshop.malls:id/edit_password"
    login_in_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title='登录 - 输入 账号')
    def input_phone(self, content ):
        allure.attach("登录页面--输入电话" ,content)
        self.input(self.phone_input, content)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title='登录 - 输入 密码')
    def input_password(self, content):
        allure.attach("登录页面--输入密码" ,content)
        self.input(self.password_input, content)

    @allure.step(title='登录 - 点击 登录')
    def click_login_in(self):
        self.click(self.login_in_button)

