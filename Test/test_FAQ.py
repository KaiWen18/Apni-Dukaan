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
class TestFAQ(unittest.TestCase):
  def test_FAQ(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://sia0.github.io/Apni-Dukaan/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "FAQ").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(1) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(1) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(2) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(2) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(3) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(3) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(4) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(4) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(5) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(5) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(6) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(6) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(7) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(7) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(8) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(8) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(9) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(9) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(10) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, "details:nth-child(10) > summary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mid2-sz").click()
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()