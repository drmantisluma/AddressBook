class SessionHelper:
    def __init__(self, fixture):
        self.fixture = fixture

    def login(self):
        wd = self.fixture.driver
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.fixture.driver
        wd.find_element_by_link_text("Logout").click()
