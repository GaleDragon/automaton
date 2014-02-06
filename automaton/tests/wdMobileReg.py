import sys, argparse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest
from config import ConfigurationMixin
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


#put your email address in here
email = "des+" + id_generator() + "@boomtownroi.com"


firstname = names.get_first_name()
lastname = names.get_last_name()

class WdMobileReg(unittest.TestCase, ConfigurationMixin):
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
        driver.find_element_by_id("user_login").send_keys(self.wp_login)
        driver.find_element_by_id("user_pass").send_keys(self.wp_pass)
        driver.find_element_by_id("wp-submit").click()
        driver.get(self.base_url + "/m/home/#registerPanel")
        #driver.find_element_by_css_selector("a[title=\"Sign Up\"]").click()
        driver.find_element_by_id("reg-fname").clear()
        driver.find_element_by_id("reg-fname").send_keys(firstname)
        driver.find_element_by_id("reg-lname").clear()
        driver.find_element_by_id("reg-lname").send_keys(lastname)
        driver.find_element_by_id("reg-email").clear()
        driver.find_element_by_id("reg-email").send_keys(self.email)
        driver.find_element_by_id("reg-phone").clear()
        driver.find_element_by_id("reg-phone").send_keys("123566463")
        driver.find_element_by_id("reg-password").clear()
        driver.find_element_by_id("reg-password").send_keys("123456")
        driver.find_element_by_id("btnRegister").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
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
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('email')
    parser.add_argument('--beta', action='store_true')
    parser.add_argument('wp_login')
    parser.add_argument('wp_password')
    args = parser.parse_args()
    test = WdMobileReg('test_wd_mobile_reg')
    test.inject(args)
    result = unittest.TestResult()
    test.run(result)