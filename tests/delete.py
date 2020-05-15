def test_group_delete(fixture):
    fixture.session.login()
    fixture.group.delete_first()
    fixture.session.logout()

def test_user_delete(fixture):
    fixture.session.login()
    fixture.user.delete_first()
    fixture.session.logout()

