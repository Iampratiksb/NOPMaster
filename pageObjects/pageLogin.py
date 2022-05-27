from selenium.webdriver.common.by import By

class pageLogin:
    textbox_Email_ID = "Email"
    textbox_Password_ID = "Password"
    button_LOG_IN_XPATH = "//button[normalize-space()='Log in']"
    link_Logout_XPATH = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def loginEmail(self, username):
        self.driver.find_element(By.ID, self.textbox_Email_ID).clear()
        self.driver.find_element(By.ID, self.textbox_Email_ID).send_keys(username)

    def loginPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_ID).clear()
        self.driver.find_element(By.ID, self.textbox_Password_ID).send_keys(password)

    def loginClick(self):
        self.driver.find_element(By.XPATH, self.button_LOG_IN_XPATH).click()

    def logoutClick(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Logout_XPATH).click()
