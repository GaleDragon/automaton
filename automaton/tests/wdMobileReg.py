from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import string
import random
import names

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


#put your email address in here
email = "des+" + id_generator() + "@boomtownroi.com"


firstname = names.get_first_name()
lastname = names.get_last_name()

class WdMobileReg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.driver.set_window_size(960, 640)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wd_mobile_reg(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
        driver.find_element_by_id("wp-submit").click()
        driver.get(self.base_url + "/m/home/#registerPanel")
        #driver.find_element_by_css_selector("a[title=\"Sign Up\"]").click()
        driver.find_element_by_id("reg-fname").clear()
        driver.find_element_by_id("reg-fname").send_keys(firstname)
        driver.find_element_by_id("reg-lname").clear()
        driver.find_element_by_id("reg-lname").send_keys(lastname)
        driver.find_element_by_id("reg-email").clear()
        driver.find_element_by_id("reg-email").send_keys(email)
        driver.find_element_by_id("reg-phone").clear()
        driver.find_element_by_id("reg-phone").send_keys("123566463")
        driver.find_element_by_id("reg-password").clear()
        driver.find_element_by_id("reg-password").send_keys("123456")
        driver.find_element_by_id("btnRegister").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
