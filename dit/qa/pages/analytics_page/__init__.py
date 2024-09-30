from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.analytics_page.components.content import Content
from dit.qa.pages.analytics_page.components.header import Header

__all__ = ['AnalyticsPage']


class AnalyticsPage(Page):
    login = TextField(css='[id*="user"]')
    password = TextField(css='[id*="pwd"]')
    submit = Button(class_name='button')
    header = Header(class_name='HeaderContainer')
    content = Content(css='[class*="HeaderNoSecondary"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                return self.content.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Cтартовая страница АРМ "Аналитика" не загружена')
        self.app.restore_implicitly_wait()

    def wait_catalog(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.toolbar.visible
                assert self.content.folders.visible

                return self.content.filters.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Вкладка Реестры не загружена')
        self.app.restore_implicitly_wait()
