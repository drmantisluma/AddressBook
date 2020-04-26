# -*- coding: utf-8 -*-
import pytest

from fixture import Fixture


@pytest.fixture()
def fixture(request):
    fixture = Fixture()
    request.addfinalizer(fixture.quit_browser)
    return fixture


def test_group_create(fixture):
    fixture.login()
    fixture.create_group()
    fixture.logout()


def test_user_create(fixture):
    fixture.login()
    fixture.create_user()
    fixture.logout()
