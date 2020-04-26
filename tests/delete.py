def test_group_delete(fixture):
    fixture.session.login()
    fixture.group.delete_first()
    fixture.session.logout()
