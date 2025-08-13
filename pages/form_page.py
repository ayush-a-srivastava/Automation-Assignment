from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities.assertions import assert_element_visible

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.XPATH, "//div[@data-label='Name']")
        self.create_edit_btn = (By.XPATH, "//span[@title='Create & edit']")
        self.textbox_field = (By.XPATH, "//span[@title='Text Box']")
        self.canvas_area = (By.XPATH, "//div[@class='formbuilder-formcanvas']")
        self.default_value_input = (By.XPATH, "//input[@aria-label='Default value']")
        self.file_upload_control = (By.XPATH, "//input[@type='file']")
        self.save_button = (By.XPATH, "//span[@title='Save']")
        self.close_button = (By.XPATH, "//span[@data-text='Close']")

    def set_form_name(self, name):
        name_elem = self.driver.find_element(*self.name_field)
        assert_element_visible(name_elem, "Form Name field")
        name_elem.clear()
        name_elem.send_keys(name)

    def click_create_edit(self):
        btn = self.driver.find_element(*self.create_edit_btn)
        assert_element_visible(btn, "Create & edit button")
        btn.click()

    def drag_and_drop_textbox(self):
        source_elem = self.driver.find_element(*self.textbox_field)
        target_elem = self.driver.find_element(*self.canvas_area)
        assert_element_visible(source_elem, "Textbox element")
        assert_element_visible(target_elem, "Form canvas area")
        ActionChains(self.driver).drag_and_drop(source_elem, target_elem).perform()

    def set_default_value(self, value):
        default_elem = self.driver.find_element(*self.default_value_input)
        assert_element_visible(default_elem, "Default value input")
        default_elem.clear()
        default_elem.send_keys(value)

    def upload_file(self, file_path):
        upload_elem = self.driver.find_element(*self.file_upload_control)
        assert_element_visible(upload_elem, "File upload control")
        upload_elem.send_keys(file_path)

    def save_form(self):
        save_elem = self.driver.find_element(*self.save_button)
        assert_element_visible(save_elem, "Save button")
        save_elem.click()

    def close_form(self):
        close_elem = self.driver.find_element(*self.close_button)
        assert_element_visible(close_elem, "Close button")
        close_elem.click()
