from selenium.webdriver.common.by import By
from utilities.assertions import assert_element_visible

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.automation_menu = (By.XPATH, "//span[text()='Automation']")
        self.create_dropdown = (By.XPATH, "(//button[@name='createOptions'])[1]")
        self.task_bot_option = (By.XPATH, "//span[@title='Task Bot…']")
        self.form_option = (By.XPATH, "//span[@title='Form…']")

    def go_to_task_bot_creation(self):
        auto_elem = self.driver.find_element(*self.automation_menu)
        assert_element_visible(auto_elem, "Automation menu")
        auto_elem.click()
        create_elem = self.driver.find_element(*self.create_dropdown)
        assert_element_visible(create_elem, "Create dropdown")
        create_elem.click()
        task_elem = self.driver.find_element(*self.task_bot_option)
        assert_element_visible(task_elem, "Task Bot option")
        task_elem.click()

    def go_to_form_creation(self):
        auto_elem = self.driver.find_element(*self.automation_menu)
        assert_element_visible(auto_elem, "Automation menu")
        auto_elem.click()
        create_elem = self.driver.find_element(*self.create_dropdown)
        assert_element_visible(create_elem, "Create dropdown")
        create_elem.click()
        form_elem = self.driver.find_element(*self.form_option)
        assert_element_visible(form_elem, "Form option")
        form_elem.click()
