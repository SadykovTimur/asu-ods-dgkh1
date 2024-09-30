from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartMonitoringPage']


class StartMonitoringPage(Page):
    login = TextField(name="username")
    password = TextField(name="password")
    submit = Button(css='[class*="button"]')
    logo = Component(tag="img")
    title = Text(tag="h2")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.login.visible
                assert self.password.visible
                assert self.title == (
                    'СИСТЕМА МОНИТОРИНГА РАБОТЫ\nЗАКАЗЧИКОВ И ПОДРЯДЧИКОВ В\nКОМПЛЕКСЕ ГОРОДСКОГО ' 'ХОЗЯЙСТВА'
                )

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Стартовая страницы АРМ "Мониторинг" не загружена')
        self.app.restore_implicitly_wait()
