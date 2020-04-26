import pytest

from fixture.fixture import Fixture


@pytest.fixture()
def fixture(request):
    fixture = Fixture()
    request.addfinalizer(fixture.quit_browser())
    return fixture
