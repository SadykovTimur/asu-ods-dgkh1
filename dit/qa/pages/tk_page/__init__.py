from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.tk_page.components.menu import Menu

__all__ = ['TkPage']


class TkPage(Page):
    login = TextField(css='[id*="username"]')
    password = TextField(css='[id*="password"]')
    submit = Button(class_name='button')
    header = Component(id="logo")
    menu = Menu(id="menu")
    left_menu = Component(class_name="left_menu")
    maps = Component(id="mapViewerContainer")
    title = Text(tag="h4")
    form_table = Component(css='[class*="form-table"]')
    table_list = Component(class_name="list")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.menu.is_visible
                assert self.maps.visible

                return self.left_menu.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Cтартовая страница АРМ "Телеметрический контроль" не загружена')
        self.app.restore_implicitly_wait()

    def wait_registry(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Реестр техники'
                assert self.form_table.visible

                return self.table_list.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Вкладка Реестры не загружена')
        self.app.restore_implicitly_wait()
