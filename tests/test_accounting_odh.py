from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    authorization_odh_page,
    open_contracts_odh,
    open_data_title_list,
    open_odh_page,
    open_registry_passport,
)


@allure.epic('ASU-ODS-DGKH')
@allure.title('АРМ "Учет ОДХ"')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_accounting_odh(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    authorization_odh_page(app, request.config.option.username, request.config.option.password)

    open_odh_page(app)

    open_registry_passport(app)

    open_contracts_odh(app)

    open_data_title_list(app)
