from model.group import Group


def test_group_modify(fixture):
    fixture.session.login()
    fixture.group.modify_first(Group("It's me", head="Leha", foot="Help me to get out from dog"))
    fixture.session.logout()


def test_user_modify(fixture):
    fixture.session.login()
    fixture.user.modify_first()
    fixture.session.logout()

