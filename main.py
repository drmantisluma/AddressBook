# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from classess.group import Group
from classess.user import User


class GroupCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_group_create(self):
        wd = self.driver
        self.login(wd)
        self.open_group_page(wd)
        self.open_group_creation(wd)
        self.fill_group_form(wd, Group("Name", "Head", "Foot"))
        self.logout(wd)

    def login(self, driver):
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self, driver):
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()

    def open_group_creation(self, driver):
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()

    def fill_group_form(self, driver, group):
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.head)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.foot)
        driver.find_element_by_name("submit").click()

    def logout(self, driver):
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


class UserCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_user_create(self):
        wd = self.driver
        self.login(wd)
        self.open_user_creation(wd)
        self.fill_user_form(wd, User("First", "Middle", "Last", "Eff-tech", "Nizhniy"))
        self.logout(wd)

    def login(self, driver):
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_user_creation(self, driver):
        driver.find_element_by_link_text("add new").click()

    def fill_user_form(self, driver, user):
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(user.name)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(user.middle)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(user.last)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(user.company)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(user.address)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, driver):
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
