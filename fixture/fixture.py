from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.user import UserHelper


class Fixture:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def quit_browser(self):
        self.driver.quit()
