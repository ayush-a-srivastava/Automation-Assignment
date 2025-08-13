from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities.assertions import assert_element_visible

class TaskBotPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.XPATH, "//div[@data-label='Name']")
        self.create_edit_btn = (By.XPATH, "//span[@title='Create & edit']")
        self.search_box = (By.XPATH, "//input[@placeholder='Search actions']")
        self.message_box_action = (By.XPATH, "//div[text()='Message Box']")
        self.message_content_field = (By.XPATH, "//div[@name='content']")
        self.save_button = (By.XPATH, "//span[@title='Save']")

    def set_bot_name(self, name):
        name_elem = self.driver.find_element(*self.name_field)
        assert_element_visible(name_elem, "Name field")
        name_elem.clear()
        name_elem.send_keys(name)

    def click_create_edit(self):
        btn = self.driver.find_element(*self.create_edit_btn)
        assert_element_visible(btn, "Create & edit button")
        btn.click()

    def search_and_add_message_box(self, search_text):
        search_elem = self.driver.find_element(*self.search_box)
        assert_element_visible(search_elem, "Search actions box")
        search_elem.clear()
        search_elem.send_keys(search_text)
        msg_elem = self.driver.find_element(*self.message_box_action)
        assert_element_visible(msg_elem, "Message Box action")
        ActionChains(self.driver).double_click(msg_elem).perform()

    def enter_message_content(self, message):
        content_elem = self.driver.find_element(*self.message_content_field)
        assert_element_visible(content_elem, "Message content field")
        content_elem.clear()
        content_elem.send_keys(message)

    def save_task(self):
        save_elem = self.driver.find_element(*self.save_button)
        assert_element_visible(save_elem, "Save button")
        save_elem.click()
