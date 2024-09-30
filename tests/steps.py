import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytics_page import AnalyticsPage
from dit.qa.pages.department_page import DepartmentPage
from dit.qa.pages.dt_page import DtPage
from dit.qa.pages.odh_page import OdhPage
from dit.qa.pages.oo_page import OoPage
from dit.qa.pages.start_monitoring_page import StartMonitoringPage
from dit.qa.pages.system_monitoring_page import SystemMonitoringPage
from dit.qa.pages.tk_page import TkPage

__all__ = [
    'authorization_odh_page',
    'authorization_oo_page',
    'authorization_dt_page',
    'authorization_tk_page',
    'authorization_analytic_page',
    'authorization_department_page',
    'open_department_page',
    'logout_department_page',
    'open_analytics_page',
    'open_catalog',
    'open_odh_page',
    'open_oo_page',
    'open_dt_page',
    'open_map_page',
    'open_registry',
    'open_start_monitoring_page',
    'sign_in_monitoring_page',
    'open_monitoring_page',
    'open_registry_territories',
    'open_contracts_list',
    'open_place_garbage',
    'open_registry_passport',
    'open_contracts_odh',
    'open_data_title_list',
]


def authorization_odh_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = OdhPage(app)
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def authorization_oo_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = OoPage(app)
            page.base_url = 'https://ods.mos.ru/garbage/login?0'
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def authorization_dt_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = DtPage(app)
            page.base_url = 'https://ods.mos.ru/udo-yard/index.html'
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def authorization_tk_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = TkPage(app)
            page.base_url = 'https://ods.mos.ru/udo-telemetry/index.html?0'
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def authorization_analytic_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = AnalyticsPage(app)
            page.base_url = 'https://ods.mos.ru/analytics/saw.dll?bieehome'
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def authorization_department_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = DepartmentPage(app)
            page.base_url = 'http://ods.mos.ru/udo-dept/'
            page.open()

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        page.submit.click()


def open_department_page(app: Application) -> None:
    with allure.step('Opening Department page'):
        try:
            DepartmentPage(app).wait_for_loading()

            screenshot_attach(app, 'department_page')
        except Exception as e:
            screenshot_attach(app, 'department_page_error')

            raise e


def logout_department_page(app: Application) -> None:
    with allure.step('Logout Department page'):
        try:
            page = DepartmentPage(app)
            page.nav.logout.click()

            page.wait_main_page()

            screenshot_attach(app, 'logout_department_page')
        except Exception as e:
            screenshot_attach(app, 'logout_department_page_error')

            raise e


def open_analytics_page(app: Application) -> None:
    with allure.step('Opening Analytic page'):
        try:
            AnalyticsPage(app).wait_for_loading()

            screenshot_attach(app, 'analytic_page')
        except Exception as e:
            screenshot_attach(app, 'analytic_page_error')

            raise e


def open_catalog(app: Application) -> None:
    with allure.step('Opening Catalog'):
        try:
            page = AnalyticsPage(app)
            page.header.catalog.click()

            page.wait_catalog()

            screenshot_attach(app, 'catalog')
        except Exception as e:
            screenshot_attach(app, 'catalog_error')

            raise e


def open_odh_page(app: Application) -> None:
    with allure.step('Opening Odh page'):
        try:
            OdhPage(app).wait_for_loading()

            screenshot_attach(app, 'odh_page')
        except Exception as e:
            screenshot_attach(app, 'odh_page_error')

            raise e


def open_oo_page(app: Application) -> None:
    with allure.step('Opening Oo page'):
        try:
            page = OoPage(app)
            page.modal.close.click()

            page.wait_for_loading()

            screenshot_attach(app, 'oo_page')
        except Exception as e:
            screenshot_attach(app, 'oo_page_error')

            raise e


def open_dt_page(app: Application) -> None:
    with allure.step('Opening Dt page'):
        try:
            DtPage(app).wait_for_loading()

            screenshot_attach(app, 'dt_page')
        except Exception as e:
            screenshot_attach(app, 'dt_page_error')

            raise e


def open_map_page(app: Application) -> None:
    with allure.step('Opening Map page'):
        try:
            TkPage(app).wait_for_loading()

            screenshot_attach(app, 'map_page')
        except Exception as e:
            screenshot_attach(app, 'map_page_error')

            raise e


def open_registry(app: Application) -> None:
    with allure.step('Opening Registry'):
        try:
            page = TkPage(app)
            page.menu.registry.click()

            page.wait_registry()

            screenshot_attach(app, 'registry')
        except Exception as e:
            screenshot_attach(app, 'registry_error')

            raise e


def open_start_monitoring_page(app: Application) -> None:
    with allure.step('Opening Start monitoring page'):
        try:
            page = StartMonitoringPage(app)
            page.base_url = 'https://monitor.mos.ru/'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_monitoring_page')
        except Exception as e:
            screenshot_attach(app, 'start_monitoring_page_error')

            raise e


def sign_in_monitoring_page(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_page = StartMonitoringPage(app)

            auth_page.login.send_keys(login)
            auth_page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_page.submit.click()


def open_monitoring_page(app: Application) -> None:
    with allure.step('Opening Monitoring page'):
        try:
            SystemMonitoringPage(app).wait_for_loading()

            screenshot_attach(app, 'monitoring_page')
        except Exception as e:
            screenshot_attach(app, 'monitoring_page_error')

            raise e


def open_registry_territories(app: Application) -> None:
    with allure.step('Opening Registry territories'):
        try:
            page = DtPage(app)
            page.header.territories.click()

            page.wait_registry_territories()

            screenshot_attach(app, 'registry_territories_page')
        except Exception as e:
            screenshot_attach(app, 'registry_territories_page_error')

            raise e


def open_contracts_list(app: Application) -> None:
    with allure.step('Opening Contracts list'):
        try:
            page = DtPage(app)
            page.header.contracts.click()

            page.wait_contracts_list()

            screenshot_attach(app, 'contracts_list_page')
        except Exception as e:
            screenshot_attach(app, 'contracts_list_page_error')

            raise e


def open_place_garbage(app: Application) -> None:
    with allure.step('Opening Place garbage'):
        try:
            page = OoPage(app)
            app.move_to_element(page.menu.place_garbage.webelement)
            page.menu.map_garbage.click()

            page.wait_place_garbage()

            screenshot_attach(app, 'place_garbage_page')
        except Exception as e:
            screenshot_attach(app, 'place_garbage_page_error')

            raise e


def open_registry_passport(app: Application) -> None:
    with allure.step('Opening Registry passport'):
        try:
            page = OdhPage(app)
            app.move_to_element(page.menu.registry.webelement)
            page.menu.registry_passport.click()

            page.wait_registry_passport()

            screenshot_attach(app, 'registry_passport_page')
        except Exception as e:
            screenshot_attach(app, 'registry_passport_page_error')

            raise e


def open_contracts_odh(app: Application) -> None:
    with allure.step('Opening Contracts odh'):
        try:
            page = OdhPage(app)
            app.move_to_element(page.menu.contracts.webelement)
            page.menu.contracts_odh.click()

            page.wait_contracts_odh()

            screenshot_attach(app, 'contracts_odh_page')
        except Exception as e:
            screenshot_attach(app, 'contracts_odh_page_error')

            raise e


def open_data_title_list(app: Application) -> None:
    with allure.step('Opening Data title list'):
        try:
            page = OdhPage(app)
            app.move_to_element(page.menu.title_list.webelement)
            page.menu.data_title_list.click()

            page.wait_data_title_list()

            screenshot_attach(app, 'data_title_list_page')
        except Exception as e:
            screenshot_attach(app, 'data_title_list_page_error')

            raise e
