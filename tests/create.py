# -*- coding: utf-8 -*-

from model.group import Group
from model.user import User


def test_group_create(fixture):
    fixture.session.login()
    fixture.group.create(Group("Name", "Head", "Foot"))
    fixture.session.logout()


def test_user_create(fixture):
    fixture.session.login()
    fixture.user.create(User("First", "Middle", "Last", "Eff-tech", "Nizhniy"))
    fixture.session.logout()
