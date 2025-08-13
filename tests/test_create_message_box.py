import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.task_bot_page import TaskBotPage

@pytest.mark.usefixtures("setup")
class TestCreateMessageBox:
    def test_create_message_box_task(self):
        login_page = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        task_bot = TaskBotPage(self.driver)

        login_page.open_url("https://community.cloud.automationanywhere.digital/#/login")
        login_page.login("your_username", "your_password")

        dashboard.go_to_task_bot_creation()
        task_bot.set_bot_name("My Bot")
        task_bot.click_create_edit()
        task_bot.search_and_add_message_box("Message Box")
        task_bot.enter_message_content("My bot is running")
        task_bot.save_task()
