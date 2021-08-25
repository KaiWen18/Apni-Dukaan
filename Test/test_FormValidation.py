import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Check that the validation for name and email is working fine
class TestFormValidation(unittest.TestCase):
  def test_FormValidation(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://sia0.github.io/Apni-Dukaan/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) > .nav-link").click()
    nameInput = self.driver.find_element(By.ID, "validationCustom01") #Obtain name text input
    emailInput = self.driver.find_element(By.ID, "validationCustom02") #Obtain email text input
    self.driver.find_element(By.ID, "validationCustom01").click()
    self.driver.find_element(By.ID, "validationCustom01").clear()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng5")
    element = self.driver.find_element(By.ID, "validationCustom03")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    self.driver.find_element(By.ID, "validationCustom01").click()
    invalid = "is-invalid" in nameInput.get_attribute("class")
    self.assertTrue(invalid, "Should have display invalid name message") #Check whether the name input have class 'is-invalid'
    self.driver.find_element(By.ID, "validationCustom01").clear()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng")
    element = self.driver.find_element(By.ID, "validationCustom03")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    invalid = "is-invalid" in nameInput.get_attribute("class")
    self.assertFalse(invalid, "Should not display invalid name message")#Check whether the name input no class 'is-invalid'
    self.driver.find_element(By.ID, "validationCustom02").click()
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperng")
    element = self.driver.find_element(By.ID, "validationCustom03")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    invalid = "is-invalid" in emailInput.get_attribute("class")
    self.assertTrue(invalid, "Should have display invalid email message") #Check whether the email input have class 'is-invalid'
    self.driver.find_element(By.ID, "validationCustom02").click()
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperngsia@hotmail.com")
    element = self.driver.find_element(By.ID, "validationCustom03")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    invalid = "is-invalid" in emailInput.get_attribute("class")
    self.assertFalse(invalid, "Should not display invalid email message") #Check whether the name input no class 'is-invalid'
    self.driver.quit()


if __name__ == "__main__":
  unittest.main()
