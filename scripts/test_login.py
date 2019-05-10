import pytest

from base.base_analysis import data_analysis
from base.base_driver import init_driver
from page.page import Page


class TestLogin:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", data_analysis("login_data", "test_login"))
    def test_login(self, args):
        phone = args['phone']
        password = args['password']
        expect = args["expect"]
        #点击我的
        self.page.home_page.click_mine()
        #点击登录
        self.page.mine_page.click_login()
        #输入电话
        self.page.login_page.input_phone(phone)
        #输入密码
        self.page.login_page.input_password(password)
        #点击登录
        self.page.login_page.click_login_in()

        assert self.page.login_page.is_toast_exits(expect)
