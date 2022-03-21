import time
from cihui100.Key.webkeyss import WebKey
from selenium.webdriver.common.by import By
import pytest

class pageLogin(WebKey):


    def login_1(self,username,password):
        _username_box_type = (By.XPATH, '//*[@id="userName"]')  # 用户名输入框
        _password_box_type = (By.XPATH, '//*[@id="passWord"]')  # 密码输入框
        _submit_button_type = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]')
          # 登录按钮
        '''
        登录用例，判断首页弹窗
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.send_keys(loc=_username_box_type,text=username)
        self.send_keys(loc=_password_box_type,text=password)
        self.find_element(_submit_button_type).click()
        #self.gotoStudentLevelHome() #登录判断弹窗


    def dy_tc(self,a,b):
        #a检查的框 b关闭的按钮
        aa = self.is_element_exist(a)
        if aa is True:
            self.find_element(b).click()
        else:
            pass

    def click(self,a):
        self.find_element(a).click()

