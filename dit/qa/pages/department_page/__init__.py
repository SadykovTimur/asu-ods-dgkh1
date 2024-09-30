from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.department_page.components.content import Content
from dit.qa.pages.department_page.components.header import Header
from dit.qa.pages.department_page.components.nav import Nav

__all__ = ['DepartmentPage']


class DepartmentPage(Page):
    login = TextField(css='[name*="username"]')
    password = TextField(css='[name*="password"]')
    submit = Button(name='submit')
    top_area = Component(class_name='topArea')
    header = Header(class_name='header')
    city = Content(class_name='city')
    nav = Nav(class_name="topNavContainer")
    title = Text(css='[class*="Subtitle"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.top_area.visible

                return self.nav.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Вкладка "Главная" не отображена')
        self.app.restore_implicitly_wait()

    def wait_main_page(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                return self.city.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()
