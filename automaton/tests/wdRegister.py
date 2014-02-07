import sys, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from config import ConfigurationMixin, FailedTestException
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

class RegWD(unittest.TestCase, ConfigurationMixin):
    def setUp(self):
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 900)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_reg_w_d(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("user_login").send_keys(self.wp_login)
        driver.find_element_by_id("user_pass").send_keys(self.wp_pass)
        driver.find_element_by_id("wp-submit").click()
        driver.get(self.base_url + "results/")
        driver.find_element_by_css_selector("i.icon.icon-forward").click()
        driver.find_element_by_css_selector("i.icon.icon-cross-2").click()
        driver.find_element_by_css_selector("i.icon.icon-forward").click()
        driver.find_element_by_css_selector("i.icon.icon-cross-2").click()
        driver.find_element_by_css_selector("i.icon.icon-forward").click()
        driver.find_element_by_css_selector("i.icon.icon-cross-2").click()
        driver.find_element_by_css_selector("i.icon.icon-forward").click()
        driver.find_element_by_css_selector(".modal-section.register #firstname").clear()
        driver.find_element_by_css_selector(".modal-section.register #firstname").send_keys(firstname)
        driver.find_element_by_css_selector(".modal-section.register #lastname").clear()
        driver.find_element_by_css_selector(".modal-section.register #lastname").send_keys(lastname)
        driver.find_element_by_css_selector(".modal-section.register #email").clear()
        driver.find_element_by_css_selector(".modal-section.register #email").send_keys(self.email)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("1234567890")
        driver.find_element_by_css_selector(".modal-section.register .btn-primary").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h1.listing-address"))
        driver.find_element_by_id("signoutlink").click()
        self.assertEqual("Sign In", driver.find_element_by_id("signinlink").text)
    
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
    test = RegWD('test_reg_w_d')
    test.inject()