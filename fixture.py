from selenium import webdriver

from classess.group import Group
from classess.user import User


class Fixture:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def create_group(self):
        wd = self.driver
        self.open_group_page()
        self.open_group_creation()
        self.fill_group_form(Group("Name", "Head", "Foot"))

    def create_user(self):
        wd = self.driver
        self.open_user_creation()
        self.fill_user_form(User("First", "Middle", "Last", "Eff-tech", "Nizhniy"))

    def login(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self):
        wd = self.driver
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()

    def open_group_creation(self):
        wd = self.driver
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()

    def open_user_creation(self):
        wd = self.driver
        wd.find_element_by_link_text("add new").click()

    def fill_group_form(self, group):
        wd = self.driver
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.head)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.foot)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def fill_user_form(self, user):
        wd = self.driver
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middle)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.last)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(user.address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def logout(self):
        wd = self.driver

        wd.find_element_by_link_text("Logout").click()

    def quit_browser(self):
        self.driver.quit()
