from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import authorization_department_page, logout_department_page, open_department_page


@allure.epic('ASU-ODS-DGKH')
@allure.title('АРМ "Департамент"')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_open_department(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    authorization_department_page(app, request.config.option.username, request.config.option.password)

    open_department_page(app)

    logout_department_page(app)
