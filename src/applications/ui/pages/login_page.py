class LoginPage:
    # URL of the page
    URL = "https://github.com/login"
    # Elements of the page
    LOGIN_FLD = '//*[@id="login_field"]'
    PASSWORD_FLD = '//*[@id="password"]'
    SIGNIN_BTN = '//*[@id="login"]/div[4]/form/div/input[13]'
    ERROR_MSG_LOCATOR = '//*[@id="js-flash-container"]/div/div' # need to be updated
    
    def __init__(self, app) -> None:
        self.app = app

    # user methods
    def try_login(self, username: str, password: str):
       self.app.enter_text(self.LOGIN_FLD, username)
       self.app.enter_text(self.PASSWORD_FLD, password)
       self.app.wait_and_click(self.SIGNIN_BTN)
    
    def navigate_to(self):
        self.app.navigate_to(self.URL)

    # check functions
    def check_wrong_creds_message(self):
        # find error message
        error_message = self.app.find_element(self.ERROR_MSG_LOCATOR).text
        # check if message is equal to "BLA" text
        return error_message == "BLA"
    
    def check_documentation_link(self):
        pass