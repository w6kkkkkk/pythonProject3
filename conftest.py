from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from cihui100.Key.WebPage import pageLogin
import allure


data1 = [{'username': 'nr1', 'password': '123456'},
            {'username': 'nr2', 'password': '123456'}
            ]

@pytest.fixture(scope='module', params = data1)
def odriver(request):
    url = 'http://tomcat4.kouyu100.com/dc100p/'
    global driver
    browser = webdriver.Chrome()
    browser.get(url)
    r = pageLogin(browser)
    r.login_1(username=(request.param['username']), password=request.param['password'])
    yield browser