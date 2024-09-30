from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.odh_page.components.content import Content
from dit.qa.pages.odh_page.components.menu import Menu

__all__ = ['OdhPage']


class OdhPage(Page):
    login = TextField(name="username")
    password = TextField(name="password")
    submit = Button(class_name='button')
    header = Component(id="header")
    menu = Menu(css='[class*="menu_container"]')
    content = Content(class_name="workspace")
    footer = Component(class_name="footer")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.menu.is_visible
                assert self.content.is_visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Главная страница АРМ "Учет ОДХ" не загружена')
        self.app.restore_implicitly_wait()

    def wait_registry_passport(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.title_form == 'Реестр паспортов ОДХ'
                assert self.content.category_object.visible
                assert self.content.form.visible

                return self.content.district.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Форма "Реестр паспортов ОДХ" не отображена')
        self.app.restore_implicitly_wait()

    def wait_contracts_odh(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.title_form == 'Контракты на содержание ОДХ'
                assert self.content.form.visible

                return self.content.table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Список контрактов на содержание ОДХ не отображен')
        self.app.restore_implicitly_wait()

    def wait_data_title_list(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.title_form == 'Данные утвержденного титульного списка'
                assert self.content.form.visible

                return self.content.table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Список утвержденных титульных списков не отображен')
        self.app.restore_implicitly_wait()
