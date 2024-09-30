from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.oo_page.components.content import Content
from dit.qa.pages.oo_page.components.header import Header
from dit.qa.pages.oo_page.components.menu import Menu
from dit.qa.pages.oo_page.components.modal import Modal

__all__ = ['OoPage']


class OoPage(Page):
    login = TextField(name="username")
    password = TextField(name="password")
    submit = Button(class_name='button')
    modal = Modal(class_name="wicket-modal")
    header = Header(class_name="header")
    menu = Menu(class_name='nav')
    content = Content(css='[class*="section"]')
    breadcrumbs = Text(class_name="breadcrumbs")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert self.menu.items[0].visible
                assert self.breadcrumbs == '  Реестр договоров между субъектами ССО'

                return self.content.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(
            condition, timeout=70, msg='Форма "Реестр договоров субъектов системы санитарной очистки" не загружена'
        )
        self.app.restore_implicitly_wait()

    def wait_place_garbage(self) -> None:
        def condition() -> bool:
            try:
                assert self.content.title == 'Карта мест сбора отходов'
                assert self.content.legend.visible
                assert self.breadcrumbs == '  Карта мест сбора отходов'

                return self.content.filters.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Карта мест сбора отходов не отображена')
        self.app.restore_implicitly_wait()
