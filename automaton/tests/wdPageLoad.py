import sys, argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from test_configs.config import ConfigurationMixin
import unittest, time, re

class PageLoad(unittest.TestCase, ConfigurationMixin):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.driver.set_window_size(1440, 900)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_page_load(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("user_login").send_keys(self.wp_login)
        driver.find_element_by_id("user_pass").send_keys(self.wp_password)
        driver.find_element_by_id("wp-submit").click()
        driver.get(self.base_url + "/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.global-header"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.global-footer-inner.inner"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img.vwhl-img"))
        driver.get(self.base_url + "/buy/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.content-header"))
        self.assertTrue(self.is_element_present(By.ID, "footer"))
        driver.get(self.base_url + "/sell/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.content-header"))
        self.assertTrue(self.is_element_present(By.ID, "footer"))
        driver.get(self.base_url + "/finance/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.content-header"))
        self.assertTrue(self.is_element_present(By.ID, "footer"))
        driver.get(self.base_url + "/results/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.global-header"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.ui-content"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h3.ui-sidebar-header"))
        # driver.get(self.base_url + "/seller-form/")
        # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.bg-image-screen"))
        # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.slc-landing-content"))
        # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.disclaimer-text.slc-landing-disclaimer"))
        # driver.get(self.base_url + "/sitemap.xml/")
        # self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "sitemapindex"))
        driver.get(self.base_url + "/blog/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.main-content"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.global-footer-inner.inner"))
        driver.get(self.base_url + "/agents/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "header.content-header"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.global-footer-inner.inner"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "article.content-page"))
        driver.get(self.base_url + "/guides/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.global-header-inner"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.global-footer-inner.inner"))
        driver.get(self.base_url + "/results-gallery/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.results-summary"))
        driver.get(self.base_url + "/results-map/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.ui-sidebar"))
    
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
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('email')
    parser.add_argument('--beta', action='store_true')
    parser.add_argument('wp_login')
    parser.add_argument('wp_password')
    args = parser.parse_args()
    test = PageLoad('test_page_load')
    test.inject(args)
    result = unittest.TestResult()
    test.run(result)