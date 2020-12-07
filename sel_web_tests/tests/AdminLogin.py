from sel_web_tests.Definitions          import Sel_Definitions
from sel_web_tests.pages.LoginPage      import LoginPage
from sel_web_tests.BaseTestCase         import BaseTestCase
import unittest
from nose.plugins.attrib import attr

class SendRequestTest(BaseTestCase, unittest.TestCase):

  def setUp(self):
    super(SendRequestTest, self).setUp()
    self.navigate_to_page(Sel_Definitions['Base_URL'] + "login.asp")
    
    
  @attr(priority="high")
  def test_LoginAdminTest(self):
    login_page_obj = LoginPage(self.driver)
    login_page_obj.admin_login()


  def tearDown(self):
    super(SendRequestTest, self).tearDown()
        

if __name__ == "__main__":
   nose.main()

