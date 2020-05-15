class GroupHelper:
    def __init__(self, fixture):
        self.fixture = fixture

    def create(self, group):
        self.open_group_page()
        self.open_group_creation()
        self.fill_group_form(group)

    def open_group_page(self):
        wd = self.fixture.driver
        wd.find_element_by_link_text("groups").click()

    def open_group_creation(self):
        wd = self.fixture.driver
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()

    def fill_group_form(self, group):
        wd = self.fixture.driver
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.head)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.foot)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def delete_first(self):
        self.open_group_page()
        wd = self.fixture.driver
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

    def modify_first(self, group):
        self.open_group_page()
        wd = self.fixture.driver
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.head)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.foot)
        wd.find_element_by_name("update").click()
