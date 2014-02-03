from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import string
import random
import names


#This decides which test to run and run said test
def runTests(url, email):
    pass



    
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

class PageLoad(unittest.TestCase):
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
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
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

class RegWD(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 900)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    
    def test_reg_w_d(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
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
        driver.find_element_by_css_selector(".modal-section.register #email").send_keys(email)
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

class WdSearchBar(unittest.TestCase):
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
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
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

class Seller(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1440, 900)
        self.base_url = "http://beta.cobblestonegroup.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_seller(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("user_login").send_keys("cobblestone")
        driver.find_element_by_id("user_pass").send_keys("4m7Md6UOcb9i")
        driver.find_element_by_id("wp-submit").click()
        driver.find_element_by_link_text("Finance").click()
        driver.find_element_by_link_text("Sell").click()
        driver.find_element_by_link_text("Contact Us").click()
        driver.find_element_by_name("sqft").clear()
        driver.find_element_by_name("sqft").send_keys("1356")
        driver.find_element_by_name("txtFeatures").clear()
        driver.find_element_by_name("txtFeatures").send_keys("stuff and stuff and stuff and 1234567 and !@#$%^&*()")
        driver.find_element_by_id("frm-sl-fn").clear()
        driver.find_element_by_id("frm-sl-fn").send_keys(firstname)
        driver.find_element_by_name("txtLastName").clear()
        driver.find_element_by_name("txtLastName").send_keys(lastname)
        driver.find_element_by_name("txtEmail").clear()
        driver.find_element_by_name("txtEmail").send_keys(email)
        driver.find_element_by_name("txtPhone").clear()
        driver.find_element_by_name("txtPhone").send_keys("5555555555")
        driver.find_element_by_name("txtPrice").clear()
        driver.find_element_by_name("txtPrice").send_keys("200000")
        driver.find_element_by_link_text("Submit Now!").click()
        driver.find_element_by_css_selector("div.contactus-content-inner")
    
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


from selenium import webdriver


if __name__ == "__main__":
    unittest.main()
