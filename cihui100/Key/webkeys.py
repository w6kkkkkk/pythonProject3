# coding=utf-8
import datetime
import json
import re
from idlelib import window
from lib2to3.pgen2 import driver
from cihui100.configs.config import NAME_PSW, NAME_PSW_teacher,NAME_PSW1,NAME_PSW2,NAME_PSW3,NAME_PSW4,NAME_PSW5,url1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.select import Select
import os
import time
from selenium.webdriver.common.keys import Keys
from cihui100.configs.config import py_mysql
py_mysql = py_mysql()
from selenium.common.exceptions import NoSuchElementException
class WebKey:

    def __init__(self):
        self.driver = None

    def openbrwser(self,br='Chrome'):
        '''
        打开浏览器
        :param br:
        :return:
        '''
        if br == 'Chrome':
            self.driver = webdriver.Chrome()
        elif br == 'edg':
            self.driver = webdriver.Edge()
        elif br == 'Firefox':
            self.driver = webdriver.Firefox()
        elif br == 'Ie':
            self.driver = webdriver.Ie()
        else:
            print('F')

        #默认隐式等待20s
        self.driver.implicitly_wait(5)

    def driver_time(self,dtime=None):
        time.sleep(float(dtime))

    def geturl(self,url=url1):
        '''
        打开URL
        :param url: 地址
        :return:
        '''
       # self.driver.get('http://dc.kouyu100.com/dc100p')
        self.driver.get(url1)

    def back(self):
        '''
        浏览器后退
        Returns
        -------
        '''
        self.back()

    def forward(self):
        '''
        浏览器前进
        Returns
        -------
        '''
        self.forward()

    def refresh(self):
        '''刷新'''
        self.driver.refresh()

    def clear(self):
        '''清空文本'''
        self.driver.clear()

    def submit(self):
        '''提交表单'''
        self.driver.submit()

    def quit(self):
        '''退出'''
        self.driver.quit()


#时间
    def str_time(self):
        '''
        :return: 返回当前系统时间：格式为：2016-03-20形式
        '''
        str_time = time.strftime("%Y-%m-%d", time.localtime())
        return str_time

    def strftime(self,ele_type=None,locator=None):
        '''
        :return: 返回当前系统时间：格式为：2016-03-20形式
        '''
        strftime = time.strftime("%Y-%m-%d", time.localtime())
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(strftime)

    def strftime_HMS(self,ele_type=None,locator=None):
        '''
        :return: 返回当前系统时间：格式为：2016-03-20 11:45:39形式
        '''
        strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(strftime)

    def stattime(self,ele_type=None,locator=None):
        '''时间输入框，输入明天的时间，格式XXXX/XX/XX'''
        import datetime
        a= datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(b))

    def stattime2(self,ele_type=None,locator=None):
        '''时间输入框，输入明天的时间，格式XXXX/XX/XX'''
        import datetime
        a= datetime.datetime.now()
        b = (a + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(b))


    def stattime_HMS(self,ele_type=None,locator=None):
        '''时间输入框，输入明天的时间，格式XXXX/XX/XX2016-03-20 11:45:39'''
        import datetime
        a= datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(b))
        ele.send_keys(Keys.ENTER)






#操作
    def maximize_window(self):
        '''
        浏览器最大化
        '''
        self.driver.maximize_window()

    def set_window_size(self,outerWidth=None,outerHeight=None):
        '''
        设置浏览器窗口的宽高
        Parameters
        ----------
        outerWidth：浏览器窗口的宽
        outerHeight：浏览器窗口的高
        Returns
        -------
        '''
        self.driver.set_window_size(outerWidth,outerHeight)

    def test_element(self,ele_type='',locator='',numb=None):
        '''
        定位方法
        :param ele_type: 类型
        :param locator:
        :return:
        '''
        ele = None
        self.ele = None
        if ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)
        elif ele_type == 'name':
            ele = self.driver.find_element_by_name(locator)
        elif ele_type == 'class_name':
            ele = self.driver.find_element_by_class_name(locator)
        elif ele_type == 'class_names':
            ele = self.driver.find_elements_by_class_name(locator)
        elif ele_type == 'tag_name':
            ele = self.driver.find_element_by_tag_name(locator)
        elif ele_type == 'css':
            ele = self.driver.find_element_by_css_selector(locator)
        elif ele_type == 'csss':
            ele = self.driver.find_elements_by_css_selector(locator)
        elif ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'link_text':
            ele = self.driver.find_element_by_link_text(locator)
        elif ele_type == 'partial_link_text':
            ele = self.driver.find_element_by_partial_link_text(locator)
        elif ele_type == 'xpaths':
            ele = self.driver.find_elements_by_xpath(locator)
        self.ele = ele
        return ele

    def size(self,ele_type=None,locator=None):
        '''
        返回元素的尺寸
        Parameters
        ----------
        height：xx
        width：xx
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        size = ele.size()
        return size

    def click(self,ele_type=None,locator=None):
        '''点击'''
        ele = self.test_element(ele_type,locator)
        ele.click()

    def clicks(self, ele_type=None, locator=None):
        ele = self.test_element(ele_type, locator)
        self.driver.execute_script('arguments[0].click()', ele)

    def context_click(self,ele_type=None,locator=None):
        '''
        右击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.context_click()

    def double_click(self,ele_type=None,locator=None):
        '''
        双击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.double_click()

    def drag_and_drop(self,source_ele_type=None,source_locator=None,target_ele_type=None,target_locator=None):
        '''
        拖动鼠标
        Parameters
        ----------
        source_ele_type：拖动开始的type
        source_locator：拖动开始的locator
        target_ele_type：拖动目标终点的type
        target_locator：拖动目标终点的locator
        drag_and_drop：拖动的方法
        Returns
        -------
        '''
        source = self.test_element(source_ele_type,source_locator)
        target = self.test_element(target_ele_type,target_locator)
        Action = ActionChains(self.driver)
        Action.drag_and_drop(source,target)

    def move_to_element(self,ele_type=None,locator=None):
        '''
        执行鼠标悬停操作
        Parameters
        ----------
        element：定位需要悬停的元素怒
        ActionChains(self.driver)：构造ActionChains对象
        perform()：执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作
        Returns：返回悬停显示的文本
        -------
        '''
        element = self.test_element(ele_type,locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def send_keys(self,ele_type=None,locator=None,value=None,ctrl_value=None):
        '''
        键盘输入
        Parameters
        ----------
        Keys.BACK_SPACE：删除键
        Keys.SPACE：空格键
        Keys.TAB：制表键
        Keys.ESCAPE：回退键
        Keys.ENTER：回车键
        组合键
        Keys.CONTROL,‘a’：全选（Ctrl+A）
        Keys.CONTROL,‘c’：复制（Ctrl+C）
        Keys.CONTROL,‘x’：剪切（Ctrl+X）
        Keys.CONTROL,‘v’：粘贴（Ctrl+V）
        Keys.F1…Fn：键盘 F1…Fn
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.send_keys(value,str(ctrl_value))
        ele.send_keys(Keys.ENTER)

    def input(self,ele_type=None,locator=None,value=None):
        '''
        模拟键盘按键
        :param ele_type:
        :param locator:
        :param value: 输入text
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(value))

    def input_d(self,ele_type=None,locator=None,value=None):
        '''
        模拟键盘按键
        :param ele_type:
        :param locator:
        :param value: 输入text
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        ele.clear()
        text = self.test_element('xpath','//*[@class="word_item word_item_c"][1]').text
        ele.send_keys(str(text))

    def input_c(self,ele_type=None,locator=None,value=None):
        '''
        模拟键盘按键
        :param ele_type:
        :param locator:
        :param value: 输入text
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        ele.clear()
        text = self.test_element('xpath','//*[@id="contentBox"]/h2').text
        a = text.split(" - ")
        b = a[1].split("，")
        ele.send_keys(str(b[value]))



    def text(self,ele_type=None,locator=None):
        '''
        获取文本内容
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        text = self.test_element(ele_type,locator).text
        return text

    def intoiframe(self,ele_type=None,locator=None):
        '''
        进入iframe
        :param locator:
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        self.driver.switch_to.frame(ele)

    def default_content(self):
        '''
        从iframe跳到最外层
        Returns
        -------
        '''
        self.driver.switch_to.default_content()

    def current_window_handle(self):
        '''
        获取当前窗口的句柄
        Returns
        -------
        '''
        sreach_windows = self.driver.current_windows_handle
        return sreach_windows

    def window_handles(self):
        '''
        返回所有窗口的句柄
        Returns
        -------
        '''
        all_handles = self.driver.window_handles
        return all_handles

    def switch_to_window(self):
        '''
        切换到新打开的窗口
        Returns
        -------
        sreach_windows：第一页（未切换窗口时第一个窗口）的句柄
        all_handles：所有窗口的句柄
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                print('切换句柄到新窗口')
            pass
        pass

    def switch_to_window_close(self):
        '''
        切换到之前的窗口
        Returns
        -------
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.close()
                self.driver.switch_to.window(handle)
                print('切换句柄到之前窗口')
            pass
        pass

    def close(self):
        '''
        关闭非当前定位到句柄的窗口
        Returns
        -------
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.close()
            pass
        pass

    def alert(self,choice = None,keysToSend = None):
        '''
        :text: 返回警告框文本
        :accept: 接受现有警告框
        :dismiss: 解散现有警告框
        :send_keys: 发送文本至警告框。keysToSend：将文本发送至警告框。
        '''
        if choice == 'text':
            del_alert = self.driver.switch_to.alert
            alert_text = del_alert.text()
            return alert_text
        elif choice == 'accept':
            del_alert=self.driver.switch_to.alert
            del_alert.accept()
        elif choice == 'dismiss':
            del_alert = self.driver.switch_to.alert
            del_alert.dismiss()
        elif choice == 'send_keys':
            del_alert = self.driver.switch_to.alert
            del_alert.send_keys(keysToSend)

    def select(self,ele_type=None,locator=None,select_by=None,value=None):
        '''
        :select_by :
                    1、select_by_value: select标签的value属性的值
                    2、select_by_index:下拉框的索引
                    3、select_by_visible_testx:下拉框的文本值
        value: 输入的value值
        '''
        sel = self.test_element(ele_type,locator)
        if select_by == 'select_by_value':
            Select(sel).select_by_value(value)
        elif select_by == 'select_by_index':
            Select(sel).select_by_index(value)
        elif select_by == 'select_by_visible_testx':
            Select(sel).select_by_visible_text(value)

    def file_path(self,ele_type=None,locator=None,file_path=None):
        '''
        :file_path: 上传文件的地址，格式：'D:\\upload_file.txt'
        '''
        self.test_element(ele_type,locator).send_keys(file_path)

    def cookies(self,name=None,key=None,cookie_dict=None):
        '''
        :get_cookies: 获得所有cookie信息
        :get_cookie(key): 返回字典的key为“key”的cookie信息
        :add_cookie(cookie_dict): 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值
        :delete_all_cookies(): 删除所有cookie信息
        '''
        if name == 'get_cookies()':
            cookies = self.driver.get_cookies()
            return cookies
        elif name == 'get_cookie(%s)%key':
            cookies_value = self.driver.get_cookies(key)
            return cookies_value
        elif name == 'add_cookie(%s)%cookie_dict':
            self.driver.add_cookie(cookie_dict)
        elif name == 'delete_all_cookies()':
            self.driver.delete_all_cookies()

    def execute_script(self,left=None,top=None):
        '''
        滚动条
        :param left: 左边距
        :param top: 上边距
        '''
        javascript = "window.scrollTo(%d,%d);"%(left,top)
        self.driver.execute_script(javascript)

    def get_screenshot_as_file(self,filename=None):
        '''
        窗口截图
        :param filename: 用于截取当前窗口，并把图片保存到本地，格式为：D:\\baidu.png
        '''
        self.driver.get_screenshot_as_file(filename)

    def current_url(self):
        '''
        获得当前页面的URL
        Returns
        -------
        '''
        now_url = self.driver.current_url
        return now_url

    def title1(self,test=None):
        '''
       获得当前页面的标题
        Returns
        -------
        '''
        title1 = self.driver.title
        # print(title1)
        return title1

    def get_attribute(self, name=None):
        '''
        获取元素属性
        Parameters
        ----------
        name：1、获取元素标签的内容(文本信息)：textContent
              2、获取元素内的全部HTML：innerHTML
              3、获取包含选中元素的HTML：outerHTML
        Returns
        -------
        '''
        get_attribute = self.driver.get_attribute(name)
        return get_attribute


#断言
    def assert_results(self,ele_type=None,locator=None,Deserved_results=None):
        '''text断言'''
        self.Deserved_results = Deserved_results
        Actual_results = self.test_element(ele_type,locator).text
        return Actual_results

    def is_displayed(self,ele_type=None,locator=None):
        '''
        断言弹窗,查看元素是否可见
        :param locator:
        :return:
        '''
        pp = self.test_element(ele_type,locator).is_displayed()
        return pp

    def qzdj(self,ele_type=None,locator=None):
        '''
        强制点击（元素被遮挡后使用）
        :param ele_type:
        :param locator:
        :return:
        '''
        qzdj = self.test_element(ele_type,locator)
        self.driver.execute_script('arguments[0].click()',qzdj)
        return qzdj



    def move_to_element_text(self,ele_type=None,locator=None):
        '''
        执行鼠标悬停操作
        Parameters
        ----------
        element：定位需要悬停的元素怒
        ActionChains(self.driver)：构造ActionChains对象
        perform()：执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作
        Returns：返回悬停显示的文本
        -------
        '''
        element = self.test_element(ele_type,locator)
        Action = ActionChains(self.driver).move_to_element(element).perform()
        return Action.text()

    def gotoStudentLevelHome(self):
        '''
        判断是否有查阅暑假练听说首页弹窗,如果有就关闭，没有不动
        :return:
        '''
        if self.test_element('xpaths', '//*[@id="check"]') != []:
            self.test_element('xpath', '//*[@id="closeImg1"]/img').click()
        elif self.test_element('xpaths', '//*[@id="teacherTipsDivUl"]') != []:
            self.test_element('xpath', '//*[@id="teacherTipsDiv"]/div/img').click()
        else:
            pass

    def Login_update(self, br='Chrome', url='', data=NAME_PSW):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def Login_update1(self, br='Chrome', url='', data=NAME_PSW1):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def Login_update2(self, br='Chrome', url='', data=NAME_PSW2):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def Login_update3(self, br='Chrome', url='', data=NAME_PSW3):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def Login_update4(self, br='Chrome', url='', data=NAME_PSW4):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def Login_update5(self, br='Chrome', url='', data=NAME_PSW5):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()


    def Login_update_teacher(self, br='Chrome', url='', data=NAME_PSW_teacher):
        '''
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.openbrwser(br)
        self.geturl(url)
        name = self.test_element('xpath', '//*[@id="userName"]')
        name.clear()
        name.send_keys(data['username'])
        pws = self.test_element('xpath', '//*[@id="passWord"]')
        pws.clear()
        pws.send_keys(data['password'])
        self.test_element('xpath', '/html/body/div[1]/div[2]/div/div[2]').click()
        self.gotoStudentLevelHome()

    def picture(self,url='http://192.168.1.191:8080/job/test_tool8/allure/'):
        driver= webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        time.sleep(10)
        # driver.refresh()
        # time.sleep(5)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            driver.get_screenshot_as_file('E:\\Program Files\\test_tool\\image\\picture\\'+picture_time+'.png')
            print('截图成功')
        except BaseException as msg:
            print(msg)
        return picture_time+'.png'

    def dancixuexi(self):
        '''
        单词学习练习
        :return:
        '''
        learn_jindu = self.test_element('xpath', '//*[@id="wordListInfo"]/div[1]/div[1]/span[3]').text  # '0/11'
        Over_jindu = int(int(learn_jindu[2:])+1)

        for i in range(0, Over_jindu):
            if self.test_element('xpaths', '//*[@id="wordBtn"]/div/span[2]') != []:

                self.test_element('xpath', '//*[@id="wordBtn"]/div/span[2]').click()
                continue

            else:
                break


    def word_option(self):
        '''
        单词辨识 遍历单词选项，找到选项后，配以单词是否一致
        :return:
        # '''
        # learn_jindu = self.test_element('class_name', 'total').text
        Over_jindu = 200


        for i in range(0,Over_jindu):
            a = self.is_element_exist('xpath', '//*[@id="wrapper"]/div/h3')
            if a is True:

                # test = self.test_element('xpath', '//*[@id="wrapper"]/div/h3').text
                #
                # sql0 = "SELECT distinct word from w2m_wordclass where cnText = '{}';" .format(test)
                # sql1 = "SELECT  word from w2m_wordclass where cnText like '{}%' LIMIT 1;" .format(test)
                # fanyi0 = py_mysql.mysql1(sql0)
                # list = []
                # for j in range(0, len(fanyi0)):
                #     b = fanyi0[j][0]
                #     list.append(b)
                #
                # if str(fanyi0) == 'None':
                #     fanyi1 = py_mysql.mysql(sql1)
                #     Eng_fanyi = fanyi1[0]
                # else:
                #     Eng_fanyi = list
                src = self.test_element('xpath', '//*[@class="word-image"]/img').get_attribute('src')
                k = src.split('/')
                H = k[-1]
                list_ABC = re.findall(r"[A-Za-z]+", H)  # 提取字母，列表类型 ['abCD']
                Eng_fanyi = list_ABC[0]

                option_a=self.test_element('xpath', '//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[1]').text
                option_b=self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[2]').text
                option_c=self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[3]').text
                if i == 0:
                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[4]').click()
                        time.sleep(5)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[3]').click()
                        time.sleep(5)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[2]').click()
                        time.sleep(5)
                    else:
                        self.test_element('xpath', '//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[1]').click()
                        time.sleep(5)
                else:

                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[1]').click()
                        time.sleep(5)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[2]').click()
                        time.sleep(5)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[3]').click()
                        time.sleep(5)
                    else:
                        self.test_element('xpath','//*[@id="contentBox"]/div/div[1]/div[2]/div[3]/div[1]/p[4]').click()

                        time.sleep(5)
            else:
                break



    def word_dictation(self):
        '''
        单词听写
        :return:
        '''
        #learn_jindu = self.test_element('class_name', 'total').text
        Over_jindu = 200

        for i in range(0,Over_jindu):
            a= self.is_element_exist('xpath', '//*[@id="wrapper"]/div/div')
            if a is True:
                # test1 = self.test_element('xpath', '//*[@id="wrapper"]/div/div').text
                # num = int(int(len(test1)) / 2)
                #
                # s1=self.is_element_exist('class_name', 'word-topic_Test')
                # if s1 is True:
                #     test = test1[0:num]
                #
                # elif s1 is False:
                #     test = test1
                #
                # sql0 = "SELECT word from w2m_wordclass where cnText = '{}' LIMIT 1;" .format(test)
                # sql1 = "SELECT word from w2m_wordclass where cnText like '{}%' LIMIT 1;" .format(test)
                # fanyi0 = py_mysql.mysql(sql0)
                # if str(fanyi0) == 'None':
                #     fanyi1 = py_mysql.mysql(sql1)
                #     Eng_fanyi = fanyi1[0]
                # else:
                #     Eng_fanyi = fanyi0[0]
                src = self.test_element('xpath','//*[@class="word-image"]/img').get_attribute('src')
                k = src.split('/')
                H = k[-1]
                list_ABC = re.findall(r"[A-Za-z]+", H)  # 提取字母，列表类型 ['abCD']
                Eng_fanyi = list_ABC[0]

                self.input('xpath','//*[@id="contentBox"]/div/div/div[2]/div[4]/div[2]/input',Eng_fanyi)
                time.sleep(2.5)

            else:
                break


    def word_dictation_znfx(self):
        '''
        单词听写
        :return:
        '''
        #learn_jindu = self.test_element('class_name', 'total').text
        Over_jindu = 200

        for i in range(0,Over_jindu):
            a = self.is_element_exist('xpath', '//*[@id="wrapper"]/div/div')
            if a is True:
                # test1 = self.test_element('xpath', '//*[@id="wrapper"]/div/div').text
                # num = int(int(len(test1)) / 2)
                #
                # s1=self.is_element_exist('class_name', 'word-topic_Test')
                # if s1 is True:
                #     test = test1[0:num]
                #
                # elif s1 is False:
                #     test = test1
                #
                # sql0 = "SELECT word from w2m_wordclass where cnText = '{}' LIMIT 1;" .format(test)
                # sql1 = "SELECT word from w2m_wordclass where cnText like '{}%' LIMIT 1;" .format(test)
                # fanyi0 = py_mysql.mysql(sql0)
                # if str(fanyi0) == 'None':
                #     fanyi1 = py_mysql.mysql(sql1)
                #     Eng_fanyi = fanyi1[0]
                # else:
                #     Eng_fanyi = fanyi0[0]
                src = self.test_element('xpath', '//*[@class="word-image"]/img').get_attribute('src')
                k = src.split('/')
                H = k[-1]
                list_ABC = re.findall(r"[A-Za-z]+", H)  # 提取字母，列表类型 ['abCD']
                Eng_fanyi = list_ABC[0]

                self.input('xpath','//*[@id="contentBox"]/div/div/div[2]/div[4]/div[2]/input',Eng_fanyi)
                time.sleep(2.5)
            else:
                break


    def ying_han(self):
        '''
        英译汉，单词听选遍历单词选项，找到选项后，配以单词是否一致
        :return:
        '''
        learn_jindu = self.test_element('id','totalNum').text
        Over_jindu = int(int(learn_jindu) / 3)
        print(type(Over_jindu))

        for i in range(0,Over_jindu):

            word1 = self.test_element('xpath', '//*[@id="cur-word"]').get_attribute('alt')

            sql0 = "SELECT cnText from w2m_wordclass where wordID = '{}';" .format(word1)

            fanyi0 = py_mysql.mysql(sql0)


            option_a=self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').get_attribute('wordid')
            option_b=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').get_attribute('wordid')
            option_c=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').get_attribute('wordid')
            if i == 0:
                time.sleep(1)
                if option_a == word1:
                    self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[4]').click()
                    s1 = self.is_element_exist('xpath','//*[@class="close-btn"]')
                    if  s1 is True:
                        self.test_element('xpath', '//*[@class="close-btn"]').click()
                    elif s1 is False:
                        pass
                    time.sleep(4)
                elif option_b == word1:
                    self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').click()
                    s1 = self.is_element_exist('xpath','//*[@class="close-btn"]')
                    if  s1 is True:
                        self.test_element('xpath', '//*[@class="close-btn"]').click()
                    elif s1 is False:
                        pass
                    time.sleep(4)
                elif option_c == word1:
                    self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').click()
                    s1 = self.is_element_exist('xpath','//*[@class="close-btn"]')
                    if  s1 is True:
                        self.test_element('xpath', '//*[@class="close-btn"]').click()
                    elif s1 is False:
                        pass
                    time.sleep(4)
                else:
                    self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').click()
                    s1 = self.is_element_exist('xpath','//*[@class="close-btn"]')
                    if  s1 is True:
                        self.test_element('xpath', '//*[@class="close-btn"]').click()
                    elif s1 is False:
                        pass
                    time.sleep(4)

            else:
                time.sleep(1)
                if option_a == word1:
                    self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').click()
                    time.sleep(2.5)
                elif option_b == word1:
                    self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').click()
                    time.sleep(2.5)
                elif option_c == word1:
                    self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').click()
                    time.sleep(2.5)
                else:
                    self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[4]').click()
                    time.sleep(2.5)

    def han_ying(self):
        '''
        汉译英遍历单词选项，找到选项后，配以单词是否一致
        :return:
        '''

        learn_jindu = self.test_element('id','totalNum').text
        Over_jindu = int(int(learn_jindu) / 3)

        for i in range(0,Over_jindu):

            test = self.test_element('xpath', '//*[@id="cur-word"]').get_attribute('alt')



            option_a=self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').get_attribute('wordid')
            option_b=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').get_attribute('wordid')
            option_c=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').get_attribute('wordid')

            time.sleep(1)
            if option_a == test:
                self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').click()
                time.sleep(2.5)
            elif option_b == test:
                self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').click()
                time.sleep(2.5)
            elif option_c == test:
                self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').click()
                time.sleep(2.5)
            else:
                self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[4]').click()
                time.sleep(2.5)

    def tingci_xuantu(self):
        '''
        听词选图，找到选项后，配以单词是否一致
        :return:
        '''

        Over_jindu = 100
        for i in range(0,Over_jindu):
            a = self.is_element_exist('xpath', '//*[@id="cur-word"]')
            if a is True:
                word1 = self.test_element('xpath', '//*[@id="cur-word"]').get_attribute('text')

                option_a = self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[1]').get_attribute('alt')
                option_b = self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[2]').get_attribute('alt')
                option_c = self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[3]').get_attribute('alt')



                # sql0 = "SELECT word from w2m_wordclass where wordID = '{}';".format(test)
                # fanyi = py_mysql.mysql(sql0)
                # ENG_fanyi=fanyi[0]
                # a = '/'
                # word1 = a + ENG_fanyi
                # print(word1)
                #
                #
                # option_a = self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[1]/img').get_attribute('src')
                # option_b = self.test_element('xpath','//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[2]/img').get_attribute('src')
                # option_c = self.test_element('xpath','//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[3]/img').get_attribute('src')
                if i == 0 :
                    if len(word1) == len(option_a):
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[2]/img').click()
                        time.sleep(4)
                    elif len(word1) == len(option_b):
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[1]/img').click()
                        time.sleep(4)
                    elif len(word1) == len(option_c):
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[4]/img').click()
                        time.sleep(4)
                    else:
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[3]/img').click()
                        time.sleep(4)
                else:
                    if len(word1) == len(option_a):
                        self.test_element('xpath','//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[1]/img').click()
                        time.sleep(8)
                    elif len(word1) == len(option_b):
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[2]/img').click()
                        time.sleep(8)
                    elif len(word1) == len(option_c):
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[3]/img').click()
                        time.sleep(8)
                    else:
                        self.test_element('xpath', '//*[@id="contentBox"]/div[1]/div/div[2]/div/ul/li[4]/img').click()
                        time.sleep(8)
            else:
                break


    def ying_han1(self):
        '''
        英译汉，单词听选遍历单词选项，找到选项后，配以单词是否一致
        :return:
        '''
        learn_jindu = self.test_element('id','totalNum').text
        Over_jindu = int(int(learn_jindu) / 3)
        print(type(Over_jindu))

        for i in range(0,Over_jindu):

            word1 = self.test_element('xpath', '//*[@id="cur-word"]').get_attribute('alt')

            sql0 = "SELECT cnText from w2m_wordclass where wordID = '{}';" .format(word1)

            fanyi0 = py_mysql.mysql(sql0)


            option_a=self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').get_attribute('wordid')
            option_b=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').get_attribute('wordid')
            option_c=self.test_element('xpath','//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').get_attribute('wordid')

            time.sleep(1)
            if option_a == word1:
                self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[1]').click()
                time.sleep(2.5)
            elif option_b == word1:
                self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[2]').click()
                time.sleep(2.5)
            elif option_c == word1:
                self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[3]').click()
                time.sleep(2.5)
            else:
                self.test_element('xpath', '//*[@id="contentBox"]/div/div[2]/div[3]/div/ul/li[4]').click()
                time.sleep(2.5)

    def alerts(self=None):  # 关闭弹窗
        # Click the link to activate the alert
        # driver.find_element(By.LINK_TEXT, "至少使用所给单词里的3个单词进行台词创作").click()
        alert = self.driver.switch_to_alert()
        self.driver_time(2)
        print(alert.text)
        alert.accept()
        self.driver_time(2)

        # Wait for the alert to be displayed and store it in a variable
        #alert = wait.until(expected_conditions.alert_is_present())

        # Store the alert text in a variable
        # text = alert.text

        # Press the OK button
        #alert.accept()


    def is_element_exist(self, ele_type1='', locator1=''):

        try:
            element = self.test_element(ele_type1,locator1)
        except NoSuchElementException as E:
            return False
        else:
            return True


    def cihuiliang(self):   #  单词学习情况---词汇量数

        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')   #获取学生id
        orgId1 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')    #获取班级id(str)
        orgId1 = orgId1.split('_')[0]
        cihuiliang = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[4]/span').text   #获取页面学生完成的前测词汇量数
        cihuiliang = int(cihuiliang)
        sql1 = "SELECT a.num FROM (select ui.id as userId,t1.num,t2.num1 from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId="+orgId1+" LEFT JOIN (select a1.userId,wuv.wordNum as num from (select ui.id as userId,wa.id as waid from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId="+orgId1+" INNER JOIN w2m_assessment wa  ON wa.user_id=ui.id and wa.delete_flag=0 and wa.progress=1 ORDER BY wa.id desc) as a1 left JOIN w2m_user_vocabulary wuv ON wuv.testid=a1.waid and a1.userId=wuv.userId group by a1.userId ) as t1 ON t1.userId=ui.id LEFT JOIN (select ui.id as userId,count(wm.notepadId) as num1 from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId="+orgId1+"  INNER JOIN w2m_notepad wm ON wm.passportId=ui.id and wm.delFlag=0 and wm.needReview=1 GROUP BY ui.id) as t2 ON t2.userId=ui.id) as a WHERE a.userId = {}".format(userId)
        cihuiliang_num = py_mysql.mysql(sql1)
        cihuiliang_nums = cihuiliang_num[0]    #数据库查询的学生前测词汇量数
        # print(fuxishu)
        # print(fuxishu_nums)
        return cihuiliang_nums,cihuiliang


    def lianxishu(self):  # 单词学习情况--练习数

        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId1 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId1 = orgId1.split('_')[0]  # 获取班级id(int)
        lianxi_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if lianxi_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        now = datetime.datetime.now()
        starttime = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)  # 当天零点
        stime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        endtime = starttime + datetime.timedelta(hours=23, minutes=59, seconds=59)  # 当天24点
        etime = endtime.strftime("%Y-%m-%d %H:%M:%S")
        lianxishus = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[8]/span').text  # 获取页面学生完成的练习数
        lianxishus = int(lianxishus)
        sql2 = "SELECT taskNum FROM (SELECT user_id, SUM(count) AS taskNum FROM ( SELECT ctcl.user_id, ctcl.course_task_task_id, ctt.pass_mode, ctt.pass_line, IF(ctt.pass_mode = 1,floor( COUNT( DISTINCT( ctcl.course_task_task_id) ) / ctt.pass_line ),COUNT(DISTINCT( ctcl.course_task_task_id) )) AS count FROM course_task_complete_list ctcl INNER JOIN student_org so ON so.studentId = ctcl.user_id LEFT JOIN course_task_task ctt ON ctcl.course_task_task_id = ctt.id LEFT JOIN course_task_step cts ON cts.id = ctt.course_task_step_id LEFT JOIN course_task_package ctp ON ctp.id = cts.course_task_package_id WHERE so.orgId = " + orgId1 + " AND ctcl.create_time > '" + stime + "' AND ctcl.create_time <='" + etime + "' AND ctcl.is_pass = 1 AND ctcl.course_resource_type <> 114 AND ctp.type_id = " + types + " and ctp.package_type=5 GROUP BY user_id, course_task_task_id ORDER BY user_id DESC, course_task_task_id ASC ) AS d GROUP BY user_id ) AS a WHERE a.user_id = {}".format(userId)
        lianxishu_num = py_mysql.mysql(sql2)
        lianxishu_nums = lianxishu_num[0]  # 数据库查询的学生练习数
        return lianxishu_nums, lianxishus


    def danyuanshu(self):  # 单词学习情况--通过单元数
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId3 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId3 = orgId3.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        now = datetime.datetime.now()
        starttime = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)  # 当天零点
        stime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        endtime = starttime + datetime.timedelta(hours=23, minutes=59, seconds=59)  # 当天24点
        etime = endtime.strftime("%Y-%m-%d %H:%M:%S")
        danyuanshus = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[7]/span').text  # 获取页面学生完成的单元数
        danyuanshus = danyuanshus.split('(')[0]
        danyuanshus = int(danyuanshus)
        sql3 = "SELECT a.comtotal FROM (SELECT ui.realname, ud.reg_grade_year , GROUP_CONCAT(upp.package_id) as package_id, ui.id as user_id, sum(upp.ctstotal) ctstotal, sum(comtotal) comtotal, max(so.classgroup_no) as group_no, sum(upp.word_total) as wordTotal  FROM user_info ui INNER JOIN user_details ud ON ui.id = ud.id INNER JOIN student_org so ON so.studentid = ui.id left join (select complete.id as package_id , complete.user_id , count(complete.ctsid) as ctstotal, sum(complete.com) as comtotal ,sum(complete.word_total) as word_total from ( select ctp.id , upp.user_id , cts.id as ctsid , IF(ctc.id is null ,0,1) as com , sum(wlu.wluCount) as word_total from user_package_purview upp inner join course_task_package ctp on upp.package_id = ctp.id and ctp.package_type = 5 and  ctp.type_id = " + types + " left join course_task_step cts on ctp.id = cts.course_task_package_id   left join course_task_complete ctc on ctc.user_id = upp.user_Id and ctc.course_task_id = cts.id AND ctc.STATUS = 1  and ctc.nofiy_time > '" + stime + "' and ctc.nofiy_time<'" + etime + "' left join (select count(wlu.id) wluCount, ctt.course_task_step_id as ctsId from course_task_task ctt inner JOIN  w2m_lesson_userword wlu on ctt.course_resource_id = wlu.lesson_id where ctt.course_resource_type = 99  group by ctt.course_task_step_id ) wlu  on  wlu.ctsId =  ctc.course_task_id where now() > upp.create_time and now() < upp.end_time  group by upp.user_id , cts.id ) as complete group by complete.user_id,complete.id order by complete.user_id,complete.id) upp on upp.user_id = ui.id WHERE so.orgid = " + orgId3 + " GROUP BY ui.id) AS a WHERE a.user_id = {}".format(userId)
        danyuanshu_num = py_mysql.mysql(sql3)
        danyuanshu_nums = danyuanshu_num[0]  # 数据库查询的学生练习数
        return danyuanshu_nums, danyuanshus


    def zhengquelv(self):  # 单词学习情况--正确率
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId3 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId3 = orgId3.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        now = datetime.datetime.now()
        starttime = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)  # 当天零点
        stime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        endtime = starttime + datetime.timedelta(hours=23, minutes=59, seconds=59)  # 当天24点
        etime = endtime.strftime("%Y-%m-%d %H:%M:%S")
        zhengquelvs=self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[10]/span').text# 获取页面学生正确率
        sql4 = "set @category=0,@rownum=0,@step=0;"
        sql5 = "SELECT a.record_info FROM(select user_id,record_info,id from ( SELECT * FROM ( SELECT CASE WHEN @category != t.user_id or @step != t.step_id THEN @rownum /*'*/:=/*'*/ 1 ELSE @rownum /*'*/:=/*'*/ @rownum + 1 END AS rank, @category /*'*/:=/*'*/ t.user_id AS var_category, @step /*'*/:=/*'*/ t.step_id AS var_step, t.* FROM unit_test_record t INNER JOIN student_org so ON so.studentid = t.user_id AND so.orgid = "+orgId3+" WHERE task_type = 114 AND create_time < '"+etime+"' AND create_time > '"+stime+"' and (step_id,user_id) in ( select cts.id,upp.user_id from course_task_step cts inner join user_package_purview upp on upp.package_id = cts.course_task_package_id  inner join course_task_package ctp on ctp.id = cts.course_task_package_id and ctp.package_type = 5 and ctp.type_id = "+types+" inner join student_org so on so.studentid = upp.user_id and so.orgId = "+orgId3+" where now() > upp.create_time and now() < upp.end_time ) and (step_id,user_id) in (select utr.step_id,user_id from unit_test_record utr where utr.is_pass = 1 and utr.task_type = 114 AND create_time < '"+etime+"' AND create_time > '"+stime+"' ) ORDER BY user_id,step_id, create_time DESC ) utr WHERE utr.rank <= 3 ) as utr) AS a where a.user_id={}".format(userId)
        b1 = py_mysql.mysql1(sql4)
        b2 = py_mysql.mysql1(sql5)
        wordCount = 0
        correctCount = 0
        for i in range(0, len(b2)):
            a = b2[i][0]
            b4 = json.loads(a)
            b5 = b4['wordCount']
            b6 = int(b4['correctCount'])
            wordCount += b5
            correctCount += b6
        print(wordCount)
        print(correctCount)
        zhengquelv_num = float(correctCount) / float(wordCount)
        zhengquelv_nums = "%.2f%%" % (zhengquelv_num * 100)# 数据库查询的学生正确率
        return zhengquelv_nums, zhengquelvs


    def Last_unit(self):  # 单词学习情况--最后一单元
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute(
            'studentid')  # 获取学生id
        orgId4 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId4 = orgId4.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        name1 = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[11]/span').text  # 获取页面学生完成的最后一个单元名
        name0 = name1.split('-')
        num = name0[0]
        nums = num.split(' ')[1]
        nums = int(nums)  # 获取得第几单元
        name1 = name0[1]  # 获取书名
        # print(name1)
        sql4 = "SELECT a.package_name,a.indexes FROM (select user_id,package_name,indexes from ( select * from ( select * from course_task_complete where (course_task_id,user_id) in ( select cts.id,upp.user_id from course_task_step cts inner join user_package_purview upp on upp.package_id = cts.course_task_package_id inner join course_task_package ctp on ctp.id = cts.course_task_package_id and ctp.type_id = " + types + " inner join student_org so on so.studentid = upp.user_id and so.orgId = " + orgId4 + " where now() > upp.create_time and now() < upp.end_time ) and status =1 order by nofiy_time desc) ctc group by user_id ) ctc inner join course_task_step cts on cts.id = ctc.course_task_id inner join course_task_package ctp on ctp.id = cts.course_task_package_id) as a WHERE a.user_id = 320671"
        name2 = py_mysql.mysql(sql4)  # 返回('书名'，单元)
        name4 = name2[0]  # 数据库查询的书名
        name3 = name2[1]  # 获取单元
        return name1, name4, nums, name3


    def fuxishu(self):  # 单词学习情况--待复习数
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId6 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId6 = orgId6.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        reviews = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[6]/span').text  # 获取页面学生完成的复习数
        reviews = int(reviews)
        # print(name1)
        sql6 = "SELECT a.num1 FROM (select ui.id as userId,t2.num1 from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId= " + orgId6 + " LEFT JOIN (select a1.userId,wuv.wordNum as num from (select ui.id as userId,wa.id as waid from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId= " + orgId6 + " INNER JOIN w2m_assessment wa  ON wa.user_id=ui.id and wa.delete_flag=0 and wa.progress=1 ORDER BY wa.id desc) as a1 left JOIN w2m_user_vocabulary wuv ON wuv.testid=a1.waid and a1.userId=wuv.userId group by a1.userId ) as t1 ON t1.userId=ui.id LEFT JOIN (select ui.id as userId,count(wm.notepadId) as num1 from student_org so INNER JOIN user_info ui ON so.studentId=ui.id and so.orgId= " + orgId6 + "  INNER JOIN w2m_notepad wm ON wm.passportId=ui.id and wm.delFlag=0 and wm.needReview=1 GROUP BY ui.id) as t2 ON t2.userId=ui.id) AS a WHERE a.userId = {}".format(
            userId)
        reviews_num = py_mysql.mysql(sql6)
        reviews_num = reviews_num[0]  # 数据库查询的学生待复习数
        return reviews, reviews_num


    def Evaluation_time(self):  # 单词学习情况--测试通过平均耗时
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId3 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId3 = orgId3.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        now = datetime.datetime.now()
        starttime = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)  # 当天零点
        stime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        endtime = starttime + datetime.timedelta(hours=23, minutes=59, seconds=59)  # 当天24点
        etime = endtime.strftime("%Y-%m-%d %H:%M:%S")
        Evaluation_times = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[9]/span').text# 获取页面学生通过平均耗时
        sql7 = "SELECT a.useTime FROM(select utr.user_id , sum(use_time)/count(id) as useTime from ( select * from (  select * from unit_test_record where is_pass = 1 and task_type = 114 and (step_id,user_id) in ( select cts.id,upp.user_id from course_task_step cts inner join user_package_purview upp on upp.package_id = cts.course_task_package_id  inner join course_task_package ctp on ctp.id = cts.course_task_package_id and ctp.type_id = 11 inner join student_org so on so.studentid = upp.user_id and so.orgId = "+orgId3+" where now() > upp.create_time and now() < upp.end_time ) and create_time > '"+stime+"' and create_time < '"+etime+"'  order by create_time desc ) cc group by user_id , task_id  ) utr group by user_id) AS a where a.user_id ={}".format(userId)
        Evaluation_time_num = py_mysql.mysql(sql7)
        Evaluation_time_num2 = Evaluation_time_num[0] / 1000
        Evaluation_time_num3 = "%.2f" % Evaluation_time_num2
        Evaluation_time_nums = Evaluation_time_num3 + 's' #数据库中查询平均耗时
        print(Evaluation_time_nums)
        return Evaluation_time_nums,Evaluation_times


    def ctstotal(self):  # 单词学习情况--总单元数
        userId = self.test_element('xpath', '//*[@id="personalDiv"]/div[1]/div[2]/span').get_attribute('studentid')  # 获取学生id
        orgId3 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')  # 获取班级id(str)
        orgId3 = orgId3.split('_')[0]  # 获取班级id(int)
        danyuan_type = self.test_element('xpath','/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/span[2]/label').text  # 获取选择的是7天还是一年
        if danyuan_type == '智能集训突击营':
            types = '11'
        else:
            types = '12'
        now = datetime.datetime.now()
        starttime = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)  # 当天零点
        stime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        endtime = starttime + datetime.timedelta(hours=23, minutes=59, seconds=59)  # 当天24点
        etime = endtime.strftime("%Y-%m-%d %H:%M:%S")
        ctstotal_num = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[5]/span/span[1]').text #获取页面上显示的总单元数
        sql8 = "select a.ctstotal from(SELECT ui.realname, ud.reg_grade_year , GROUP_CONCAT(upp.package_id) as package_id, ui.id as user_id, sum(upp.ctstotal) ctstotal, sum(comtotal) comtotal, max(so.classgroup_no) as group_no, sum(upp.word_total) as wordTotal  FROM user_info ui INNER JOIN user_details ud ON ui.id = ud.id INNER JOIN student_org so ON so.studentid = ui.id left join (select complete.id as package_id , complete.user_id , count(complete.ctsid) as ctstotal, sum(complete.com) as comtotal ,sum(complete.word_total) as word_total from ( select ctp.id , upp.user_id , cts.id as ctsid , IF(ctc.id is null ,0,1) as com , sum(wlu.wluCount) as word_total from user_package_purview upp inner join course_task_package ctp on upp.package_id = ctp.id and ctp.package_type = 5 and  ctp.type_id = "+types+" left join course_task_step cts on ctp.id = cts.course_task_package_id   left join course_task_complete ctc on ctc.user_id = upp.user_Id and ctc.course_task_id = cts.id AND ctc.STATUS = 1  and ctc.nofiy_time > '"+stime+"' and ctc.nofiy_time<'"+etime+"' left join (select count(wlu.id) wluCount, ctt.course_task_step_id as ctsId from course_task_task ctt inner JOIN  w2m_lesson_userword wlu on ctt.course_resource_id = wlu.lesson_id where ctt.course_resource_type = 99  group by ctt.course_task_step_id ) wlu  on  wlu.ctsId =  ctc.course_task_id where now() > upp.create_time and now() < upp.end_time  group by upp.user_id , cts.id ) as complete group by complete.user_id,complete.id order by complete.user_id,complete.id) upp on upp.user_id = ui.id WHERE so.orgid = "+orgId3+" GROUP BY ui.id) AS a where a.user_id={}".format(userId)
        ctstotal_num1 = py_mysql.mysql(sql8)
        ctstotal_nums = str(ctstotal_num1[0])   #数据库查询总单元数
        return ctstotal_nums,ctstotal_num

    def zhengquelv_Report(self):  # 个人分享报告--正确率
        zhengquelv_Report_num = self.test_element('xpath','/html/body/div/div[1]/div[2]/div/div/div[3]/div[1]/span[2]').text#报告中显示的数据
        self.switch_to_window_close()
        zhengquelv_Report_nums = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[10]/span').text#单词学习情况中显示的数据
        return zhengquelv_Report_num,zhengquelv_Report_nums

    def Evaluation_time_Report(self):  # 个人分享报告--测试通过平均耗时
        Evaluation_time_Report_num = self.test_element('xpath','/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/span[2]').text#报告中显示的数据
        self.switch_to_window_close()
        Evaluation_time_Report_nums = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[9]/span').text  # 单词学习情况中显示的数据
        return Evaluation_time_Report_num, Evaluation_time_Report_nums

    def lianxishu_Report(self):  # 个人分享报告--练习数
        lianxishu_Report_num = self.test_element('xpath','/html/body/div/div[1]/div[2]/div/div/div[3]/div[3]/span[2]').text  # 报告中显示的数据
        self.switch_to_window_close()
        lianxishu_Report_nums = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[8]/span').text  # 单词学习情况中显示的数据
        return lianxishu_Report_num, lianxishu_Report_nums

    def danyuanshu_Report(self):  # 个人分享报告--通过单元数
        danyuanshu_Report_num1 = self.test_element('xpath','/html/body/div/div[1]/div[2]/div/div/div[3]/div[4]/span[2]').text # 报告中显示的数据
        danyuanshu_Report_num = danyuanshu_Report_num1.split('(')[0]
        self.switch_to_window_close()
        danyuanshu_Report_nums1 = self.test_element('xpath','//*[@id="personalDiv"]/div[1]/div[7]/span').text  # 单词学习情况中显示的数据
        danyuanshu_Report_nums = danyuanshu_Report_nums1.split('(')[0]
        return danyuanshu_Report_num, danyuanshu_Report_nums

    def jiangli(self):
        a = self.is_element_exist('xpath','//*[@id="getAward"]/img')
        if a is True:
            self.test_element('xpath','//*[@id="getAward"]/img').click()
            self.driver_time(2)
            self.test_element('xpath','//*[@id="closeAward"]/img').click()
        else:
            pass

    def fuxi(self):
        a = self.is_element_exist('xpath', '//*[@class="btn"]')
        if a is True:
            self.test_element('xpath','//*[@onclick="closeReviewNotepadWords()"]').click()
        else:
            pass




    def pK_number_teacher(self):   #  PK签到人数和班级人数--老师页面
        signed_number1 = self.test_element('xpath', '//*[@id="signMemberCount"]').text   #已签到人数
        signed_number1 = int(signed_number1)
        class_number = self.test_element('xpath', '//*[@class="extendTime_sign_cd2"]').text  # 班级人数
        class_number = class_number.split(': ')[1]
        class_numbers1 = class_number[0:-1]
        class_numbers1 = int(class_numbers1)
        orgId6 = self.test_element('xpath', '//*[@id="classId"]').get_attribute('value')    #获取班级id(str)
        orgId7 = orgId6.split('_')[0]   #获取班级id(int)
        # print(name1)
        sql7 = "select count(distinct ctsr.id) as scount,count(distinct so.studentId) as ucount from course_task_sginin cts left join course_task_sginin_record  ctsr on cts.id = ctsr.sgin_id left join student_org so on so.orgId=cts.org_id and so.orgType = cts.org_type left join user_info ui on ui.id = ctsr.user_id where cts.id = (select sgin_id from course_task_pk ctp where ctp.org_id=" + orgId7 + " and ctp.org_type=1 and ctp.status>0 and start_time BETWEEN DATE_FORMAT(now(),'%Y-%m-%d') and DATE_FORMAT(DATE_ADD(now(),INTERVAL 1 day),'%Y-%m-%d') order by start_time desc limit 1)"
        num = py_mysql.mysql(sql7)
        signed_number2 = num[0]   #数据库查询的学生已签到人数
        class_number2 = num[1]
        return signed_number1,class_numbers1,signed_number2,class_number2


    def pK_number_studennt(self):   #  PK签到人数和班级人数--学生页面
        signed_number1 = self.test_element('xpath', '/html/body/div[5]/div[2]/div[2]/div[1]/div/p/span[1]/span').text   #已签到人数
        signed_number1 = signed_number1[0:-1]    #已签到人数
        signed_number1 = int(signed_number1)
        class_number = self.test_element('xpath', '/html/body/div[5]/div[2]/div[2]/div[1]/div/p/span[2]/span').text  # 班级人数
        class_number = class_number[0:-1]   # 班级人数
        class_number = int(class_number)
        orgId7 = '4914'
        # print(name1)
        sql7 = "select count(distinct ctsr.id) as scount,count(distinct so.studentId) as ucount from course_task_sginin cts left join course_task_sginin_record  ctsr on cts.id = ctsr.sgin_id left join student_org so on so.orgId=cts.org_id and so.orgType = cts.org_type left join user_info ui on ui.id = ctsr.user_id where cts.id = (select sgin_id from course_task_pk ctp where ctp.org_id=" + orgId7 + " and ctp.org_type=1 and ctp.status>0 and start_time BETWEEN DATE_FORMAT(now(),'%Y-%m-%d') and DATE_FORMAT(DATE_ADD(now(),INTERVAL 1 day),'%Y-%m-%d') order by start_time desc limit 1)"
        num = py_mysql.mysql(sql7)
        signed_number2 = num[0]   #数据库查询的学生已签到人数
        class_number2 = num[1]
        return signed_number1,class_number,signed_number2,class_number2


    def chlcs_lxzq(self):
        """
        词汇量全部选择正确训练测试
        """
        Over_jindu = 100
        for i in range(0, Over_jindu):

            a = self.is_element_exist('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[1]')
            if a is True:
                wordid = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[1]').get_attribute('wordid')
                sql0 = "SELECT  word from w2m_wordclass where wordid = {};".format(wordid)
                fanyi0 = py_mysql.mysql(sql0)
                Eng_fanyi = fanyi0[0]
                option_a = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').text
                option_b = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').text
                option_c = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').text


                if i == 0:
                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').click()
                        time.sleep(1)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').click()
                        time.sleep(1)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[6]/p[2]').click()
                        time.sleep(1)
                    else:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').click()
                        time.sleep(1)
                else:

                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').click()
                        time.sleep(3)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').click()
                        time.sleep(3)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').click()
                        time.sleep(3)
                    else:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[6]/p[2]').click()
                        time.sleep(3)

            else:
                break


    def xznj(self):
        a = self.is_element_exist('xpath','//*[@id="wtmVocabulary"]/div/div[2]/div/p')
        if a is True:
            self.test_element('xpath','//*[@id="wtmVocabulary"]/div/div[2]/div/div[2]/div/div[1]').click()
            self.driver_time(2)
            self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div[2]/div/div[2]/div/div[2]/div[1]').click()
            self.driver_time(2)
            self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div[2]/div/div[3]').click()
        else:
            pass

    def chlcs_lxcw(self):
        """
        词汇量测试错误训练测试
        """
        Over_jindu = 1000
        for i in range(0, Over_jindu):
            a = self.is_element_exist('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[1]')
            if a is True:

                wordid = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[1]').get_attribute('wordid')
                sql0 = "SELECT  word from w2m_wordclass where wordid = {};".format(wordid)
                fanyi0 = py_mysql.mysql(sql0)
                Eng_fanyi = fanyi0[0]
                option_a = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').text
                option_b = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').text
                option_c = self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').text

                if i % 2==0:
                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').click()
                        time.sleep(2)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').click()
                        time.sleep(2)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[6]/p[2]').click()
                        time.sleep(2)
                    else:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').click()
                        time.sleep(2)
                else:

                    time.sleep(1)
                    if option_a == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[3]/p[2]').click()
                        time.sleep(3)
                    elif option_b == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[4]/p[2]').click()
                        time.sleep(3)
                    elif option_c == Eng_fanyi:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[5]/p[2]').click()
                        time.sleep(3)
                    else:
                        self.test_element('xpath', '//*[@id="wtmVocabulary"]/div/div/div[2]/div[6]/p[2]').click()
                        time.sleep(3)
            else:
                break

    def danyuan_click(self):
        a = self.is_element_exist('css','img[src$="icon1.png"]')
        b = self.is_element_exist('csss','img[src$="icon3.png"]')
        if a is True:
            self.test_element('css','img[src$="icon1.png"]').click()
        else:
            if b is True:
                self.test_element('csss', 'img[src$="icon3.png"]')[-1].click()
            else:
                self.test_element('csss', 'img[src$="icon2.png"]')[-1].click()

    def xuanze_kecheng(self):
        a = self.is_element_exist('xpath','//div[@class="curriculum-info"]/div[2]/p')
        if a is True:
            self.test_element('xpath','//div[@class="left-box1"]/h3/span').click()
            self.driver_time(2)
            self.test_element('xpath', '//*[@id="wordCourseList"]/li[1]/div[1]/img').click()
            self.driver_time(2)
            self.test_element('xpath', '//*[@class="select"]').click()

        else:
            pass

    def skip_read(self,num=None):
        url1 = self.current_url()

        a = url1.split('=')
        b = round(float(a[1]))
        c = str(b + num)
        print(c)

        qq = str(a[0]) + '=' + c
        # 拼链接
        new_url = str(qq)
        print(new_url)
        self.driver.get(new_url)
        self.driver_time(5)

    def Eng_name(self):
        a = self.is_element_exist('xpath','//*[@id="engTitle"]')
        if a is True:
            self.input('xpath','//*[@id="engName"]','test')
            self.driver_time(2)
            self.test_element('xpath','//*[@id="engNameBtn"]').click()
            self.driver_time(2)
        else:
            pass



