import sys, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re
from config import ConfigurationMixin

class WdSearchBar(unittest.TestCase, ConfigurationMixin):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 900)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wd_search_bar(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("user_login").send_keys(self.wp_login)
        driver.find_element_by_id("user_pass").send_keys(self.wp_pass)
        driver.find_element_by_id("wp-submit").click()
        driver.get(self.base_url + "/results")
        driver.find_element_by_css_selector("h2[title=\"Price\"]").click()
        self.assertTrue(driver.find_element_by_css_selector(".price-dropdown .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector("h2[title=\"Type\"]").click()
        self.assertFalse(driver.find_element_by_css_selector(".price-dropdown .ui-dropdown-menu").is_displayed())
        self.assertTrue(driver.find_element_by_css_selector(".type-dropdown .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector("h2[title=\"Beds\"]").click()
        self.assertTrue(driver.find_element_by_css_selector(".beds-dropdown .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector("h2[title=\"Baths\"]").click()
        self.assertTrue(driver.find_element_by_css_selector(".baths-dropdown .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector("h2[title=\"More\"]").click()
        self.assertTrue(driver.find_element_by_css_selector("#powersearch-menu").is_displayed())
        driver.find_element_by_css_selector("h2[title=\"More\"]").click()
        self.assertFalse(driver.find_element_by_css_selector("#powersearch-menu").is_displayed())
        driver.find_element_by_css_selector(".results-controls .btn.sort-results").click()
        self.assertTrue(driver.find_element_by_css_selector(".results-sort .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector(".results-controls .btn.sort-results").click()
        self.assertFalse(driver.find_element_by_css_selector(".baths-dropdown .ui-dropdown-menu").is_displayed())
        driver.find_element_by_css_selector(".btn.sidebar-toggle").click()
   
    
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
    test = WdSearchBar('test_wd_search_bar')
    test.inject()