# Generated by Selenium IDE
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


class TestFormValidation(unittest.TestCase):
  def test_FormValidation(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://sia0.github.io/Apni-Dukaan/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) > .nav-link").click()
    self.driver.find_element(By.ID, "validationCustom01").click()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng5")
    element = self.driver.find_element(By.ID, "validationCustom02")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2)").click()
    nameInput = self.driver.find_element(By.ID, "validationCustom01").get_attribute("class")
    invalid = "is-invalid" in nameInput
    self.assertTrue(invalid, "Should have display invalid name message")
    self.driver.find_element(By.ID, "validationCustom01").click()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng")
    element = self.driver.find_element(By.ID, "validationCustom02")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "invalidEmailMsg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2)").click()
    self.driver.find_element(By.ID, "validationCustom02").click()
    nameInput2 = self.driver.find_element(By.ID, "validationCustom01").get_attribute("class")
    print(nameInput2)
    invalid2 = "is-invalid" in nameInput2
    self.assertFalse(invalid2, "Should not display invalid name message")
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperngsia")
    self.driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2)").click()
    self.driver.find_element(By.ID, "validationCustom02").click()
    invEmail = self.driver.find_element(By.ID, "invalidEmailMsg").is_displayed()
    print(invEmail)
    self.assertTrue(invEmail, "Should have display invalid email message")
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperngsia@hotmail")
    self.driver.find_element(By.CSS_SELECTOR, ".input-container:nth-child(2)").click()
    invEmail = self.driver.find_element(By.ID, "invalidEmailMsg").is_displayed()
    print(invEmail)
    self.assertTrue(invEmail, "Should have display invalid email message")
    self.driver.find_element(By.ID, "validationCustom02").click()
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperngsia@hotmail.com")
    self.driver.find_element(By.ID, "validationCustom03").click()
    invEmail = self.driver.find_element(By.ID, "invalidEmailMsg").is_displayed()
    print(invEmail)
    self.assertFalse(invEmail, "Should have display invalid email message")
    self.driver.quit()

if __name__ == "__main__":
 unittest.main()