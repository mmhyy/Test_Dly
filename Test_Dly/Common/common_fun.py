from Test_Dly.baseView.baseView import BaseView
from Test_Dly.Common.desired_capability import desired_caps
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
import time
import datetime


class Common(BaseView):

    edt = (By.XPATH,'//*[contains(@text,"自动编码")]')

    def swipe_Down(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.9)
        y1 = int(y * 0.9)
        y2 = int(y * 0.2)
        time.sleep(2)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipe_left(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.9)
        x2 = int(x * 0.6)
        y1 = int(y * 0.2)
        time.sleep(2)
        self.driver.swipe(x1, y1, x2, y1, 1000)



    def Encoding_rule(self):
        endco = 0
        try:
            self.driver.find_element(*self.edt)
        except NoSuchElementException:
            logging.info('不是自动编码')
        else:
            endco = 1
        return endco

    def Endcoding_set(self):
        today = datetime.datetime.today()
        encoding = str(today.year)+str(today.month)+str(today.day)
        return encoding


if __name__ == '__main__':
    driver = desired_caps()
    com = Common(driver)
    com.check_work()
    # '''点击工作中心'''
    logging.info(com.Endcoding_set())
