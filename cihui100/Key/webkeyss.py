from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

class WebKey(object):
    def __init__(self,deiver:webdriver.remote):
        self.browser = deiver

    def _locate_element(self,loc):
        ''''loc : '定位方法','元素位置'
        '''
        if loc is not None:
            ele = self.browser.find_element(*loc)
        else:
            raise NameError('找不到指定元素%s!' % loc)
        return ele

    #定位元素
    def find_element(self,loc):
        return self._find_element(*loc)

    def _find_element(self, *loc):
        try:
            # 加一个显式等待，元素加载成功
            WebDriverWait(self.browser, 10).until(EC.visibility_of_all_elements_located(loc))
            element = self.browser.find_element(*loc)
            return element
        except AttributeError:
            print('F')



    #输入文本框
    def send_keys(self,loc,text):
        self.find_element(loc).send_keys(text)


    # 执行js脚本
    def execute_js(self, src):
        self.browser.execute_script(src)

    #关闭浏览器
    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.browser.close()

    def is_element_exist(self, loc):
        try:
            element = self.find_element(loc)
        except NoSuchElementException as E:
            return False
        else:
            return True