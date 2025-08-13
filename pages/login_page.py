from selenium.webdriver.common.by import By
from utilities.assertions import assert_element_visible

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")  # Adjust locator if needed

    def open_url(self, url):
        self.driver.get(url)

    def login(self, username, password):
        user_elem = self.driver.find_element(*self.username_input)
        assert_element_visible(user_elem, "Username input")
        user_elem.clear()
        user_elem.send_keys(username)

        pass_elem = self.driver.find_element(*self.password_input)
        assert_element_visible(pass_elem, "Password input")
        pass_elem.clear()
        pass_elem.send_keys(password)

        try:
            self.driver.find_element(*self.login_button).click()
        except:
            pass
