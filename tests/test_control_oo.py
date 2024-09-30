from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import authorization_oo_page, open_oo_page, open_place_garbage


@allure.epic('ASU-ODS-DGKH')
@allure.title('Контроль обработки отходов')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_control_oo(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    authorization_oo_page(app, request.config.option.username, request.config.option.password)

    open_oo_page(app)

    open_place_garbage(app)
