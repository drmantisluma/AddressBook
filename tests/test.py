# -*- coding: utf-8 -*-
import pytest

from fixture.fixture import Fixture
from model.group import Group
from model.user import User


@pytest.fixture()
def fixture(request):
    fixture = Fixture()
    request.addfinalizer(fixture.quit_browser)
    return fixture


def test_group_create(fixture):
    fixture.session.login()
    fixture.group.create(Group("Name", "Head", "Foot"))
    fixture.session.logout()


def test_user_create(fixture):
    fixture.session.login()
    fixture.user.create(User("First", "Middle", "Last", "Eff-tech", "Nizhniy"))
    fixture.session.logout()
