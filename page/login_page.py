
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    phone_input = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_input = By.ID, "com.tpshop.malls:id/edit_password"
    login_in_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_phone(self, name ):
        self.input(self.phone_input, name)

    def input_password(self, password):
        self.input(self.password_input, password)

    def click_login_in(self):
        self.click(self.login_in_button)