from BasicPage                          import BasicPage
from BasicPage                          import IncorrectPageException
from sel_web_tests.objects.ObjectsMap   import LoginPageMap


class LoginPage(BasicPage):

  def __init__(self, driver):
    super(LoginPage, self).__init__(driver)
  

  def _verify_page(self):
    try:
      self.wait_for_element_visibility(10, 
                                       "xpath", 
                                       LoginPageMap['UsernameFieldXpath']
    )
    except:   
      raise IncorrectPageException
   

  def admin_login(self):
    self.fill_out_field("xpath",
                        LoginPageMap['UsernameFieldXpath'],
                        "admin"
    )
    self.fill_out_field("xpath",
                        LoginPageMap['PasswordFieldXPath'],
                        "admin"
    )
    self.click(10, "xpath",
               LoginPageMap['LoginButtonXPath']
    )
    self.wait_for_element_visibility(10, 
                                     "xpath", 
                                     LoginPageMap['TitlePageMsgXpath']
    )


  def submit_request(self):
    self.fill_out_field("xpath", 
                        ContactPageMap['FirstNameFieldXpath'], 
                        "Paul"
    )
    self.fill_out_field("xpath", 
                        ContactPageMap['LastNameFieldXpath'], 
                        "Pierce"
    )
    self.fill_out_field("xpath", 
                        ContactPageMap['EmailFieldXpath'], 
                        "contactemail@test.com"
    )
    self.fill_out_field("xpath",
                        ContactPageMap['CommentFieldXpath'],
                        "My comment"
    )
    self.click(10, 
               "xpath", 
               ContactPageMap['SubmitButtonXpath']
    )
    self.wait_for_element_visibility(10, 
                                     "xpath", 
                                     ContactPageMap['ThankYouMessageXpath']
    )


  def validation_check(self):
    self.fill_out_field("xpath", 
                        ContactPageMap['FirstNameFieldXpath'], 
                        "Paul"
    )
    self.fill_out_field("xpath", 
                        ContactPageMap['LastNameFieldXpath'], 
                        "Pierce"
    )
    self.fill_out_field("xpath", 
                        ContactPageMap['EmailFieldXpath'], 
                        "contactemail@"
    )
    self.fill_out_field("xpath", 
                        ContactPageMap['CommentFieldXpath'], 
                        "My comment"
    )
    self.click(10, 
               "xpath", 
               ContactPageMap['SubmitButtonXpath']
    )
    return self

