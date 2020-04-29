from Test_Dly.baseView.baseView import BaseView
from Test_Dly.Common.desired_capability import desired_caps
from Test_Dly.Common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

class Moudle(Common,BaseView):
    tv_tab_title = (By.XPATH, '//*[@text="工作"]/parent::* ')
    '''工作中心'''
    btn_multi_search = (By.XPATH,'[@index="1" and @class="android.widget.ImageButton"]')
    '''选择模块'''


    def check_work(self):
        try:
            self.driver.find_element(*self.tv_tab_title)
        except NoSuchElementException:
            logging.info('不在工作中心')
        else:
            self.driver.find_element(*self.tv_tab_title).click()

    def check_module(self):
        try:
            self.driver.find_element(*self.btn_multi_search)
        except NoSuchElementException:
            logging.info('没找到模块选择按钮')
        else:
            self.driver.find_element(*self.btn_multi_search).click()

    def select_module(self,element):
        element = self.element
        try:
            self.driver.find_element(element)
        except NoSuchElementException:
            logging.info('没有那个找到要选择模块')







if __name__ == '__main__':

    driver = desired_caps()
    module = Moudle(driver)
    module.check_work()
    module.swipe_Down()
    module.base_Information()