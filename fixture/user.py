class UserHelper:
    def __init__(self, fixture):
        self.fixture = fixture

    def create(self, user):
        self.open_user_creation()
        self.fill_user_form(user)

    def open_user_creation(self):
        wd = self.fixture.driver
        wd.find_element_by_link_text("add new").click()

    def fill_user_form(self, user):
        wd = self.fixture.driver
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

    def delete_first(self):
        wd = self.fixture.driver
        wd.find_element_by_name("selected[]").click()
        # probably it should be better to beautify this one
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first(self):
        wd = self.fixture.driver
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a").click()
        wd.find_element_by_name("title").send_keys("QA")
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
