from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import authorization_dt_page, open_contracts_list, open_dt_page, open_registry_territories


@allure.epic('ASU-ODS-DGKH')
@allure.title('АРМ "Учет дворовых территорий"')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_accounting_dt(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    authorization_dt_page(app, request.config.option.username, request.config.option.password)

    open_dt_page(app)

    open_registry_territories(app)

    open_contracts_list(app)
