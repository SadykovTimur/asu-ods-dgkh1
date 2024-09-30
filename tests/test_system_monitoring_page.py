from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_monitoring_page, open_start_monitoring_page, sign_in_monitoring_page


@allure.epic('ASU-ODS-DGKH')
@allure.title('АРМ Система мониторинга')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_system_monitoring_page(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_start_monitoring_page(app)

    sign_in_monitoring_page(app, request.config.option.username, request.config.option.password)

    open_monitoring_page(app)
