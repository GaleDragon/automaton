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

class WdSaveSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 900)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wd_save_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
        driver.find_element_by_id("wp-submit").click()
        driver.find_element_by_css_selector("h2[title=\"Price\"]").click()
        driver.find_element_by_id("search-max-price-input").click()
        driver.find_element_by_css_selector("option[value=\"325000\"]").click()
        driver.find_element_by_id("search-price-apply-btn").click()
        driver.find_element_by_css_selector("h2[title=\"Beds\"]").click()
        driver.find_element_by_css_selector("input[value=\"3\"]").click()
        driver.find_element_by_id("gobutton").click()
        driver.find_element_by_css_selector("span.show-inline-large-min").click()
        driver.find_element_by_id("searchName").send_keys(firstname + lastname)
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_xpath("//form/button").click()
        try: self.assertEqual("1", driver.find_element_by_id("savedsearchcount").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
