from selenium import webdriver
import unittest
from sel_web_tests.Sel_Definitions import Selenium_Defines

class BaseTestCase(object):
  """
  Choose browser in setUP with webDriver
  And then tearDown and close webDriver
  Use Sel_Definitions file for test dicts.
  """

  def setUp(self):

    if Sel_Definitions['Browser'].lower() == "firefox":
      self.driver = webdriver.Firefox()
    elif Sel_Definitions['Browser'].lower() == "chrome":
      self.driver = webdriver.Chrome()
    elif Sel_Definitions['Browser'].lower() == "ie": 
      self.driver = webdriver.Ie()
    else:
      raise Exception("Your web browser is NOT supported!")

  def navigate_to_page(self, url):
    self.driver.get(url)

  def tearDown(self):
    self.driver.quit()
