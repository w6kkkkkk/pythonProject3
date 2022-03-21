import time
import turtle
from selenium import webdriver
from selenium.webdriver.common.by import By
from cihui100.Key.WebPage import pageLogin
import allure
import pytest

class Testabc:
    # url = 'http://tomcat4.kouyu100.com/dc100p/'
    # data = [{'username': 'nr1', 'password': '123456'},
    #         {'username': 'nr2', 'password': '123456'}
    #
    # @pytest.mark.dependency()
    @pytest.mark.run(order=0)
    def test_login1(self, odriver):
        r = pageLogin(odriver)
        a = (By.XPATH, '//*[@class="btn"]')
        b = (By.XPATH, '//*[@onclick="closeReviewNotepadWords()"]')
        r.dy_tc(a,b)
        time.sleep(5)
        pass
    # @pytest.mark.dependency(depends=["Testabc::test_login1"])
    @pytest.mark.run(order=1)
    def test_login2(self,odriver):
        r = pageLogin(odriver)
        a = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[1]/ul/li[2]/a/img')
        r.click(a)
        time.sleep(15)
        pass




if __name__ == '__main__':
    pytest.main('-n 2')
