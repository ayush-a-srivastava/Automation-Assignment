import pytest
import os
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.form_page import FormPage

@pytest.mark.usefixtures("setup")
class TestCreateForm:
    def test_create_form_with_file_upload(self):
        login_page = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        form_page = FormPage(self.driver)

        login_page.open_url("https://community.cloud.automationanywhere.digital/#/login")
        login_page.login("your_username", "your_password")

        dashboard.go_to_form_creation()
        form_page.set_form_name("My Form")
        form_page.click_create_edit()
        form_page.drag_and_drop_textbox()
        form_page.set_default_value("MyForm")

        file_path = os.path.abspath("shared/testfile.txt")
        form_page.upload_file(file_path)

        form_page.save_form()
        form_page.close_form()
