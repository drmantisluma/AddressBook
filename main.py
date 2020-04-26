# -*- coding: utf-8 -*-
import pytest

from classess.group import Group
from classess.user import User
from fixture import Fixture


@pytest.fixture()
def fixture(request):
    fixture = Fixture()
    request.addfinalizer(fixture.quit_browser)
    return fixture


def test_group_create(fixture):
    fixture.login()
    fixture.create_group(Group("Name", "Head", "Foot"))
    fixture.logout()


def test_user_create(fixture):
    fixture.login()
    fixture.create_user(User("First", "Middle", "Last", "Eff-tech", "Nizhniy"))
    fixture.logout()
