from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.dt_page.components.content import Content
from dit.qa.pages.dt_page.components.header import Header

__all__ = ['DtPage']


class DtPage(Page):
    login = TextField(css='[id*="username"]')
    password = TextField(css='[id*="password"]')
    submit = Button(css='[class*="apply"]')
    header = Header(class_name="header")
    content = Content(class_name="content")
    footer = Component(tag="footer")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert self.content.is_visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(
            condition,
            timeout=70,
            msg='Форма "Сводка по дворовым территориям и внутриквартальным проездам" не ' 'загружена',
        )
        self.app.restore_implicitly_wait()

    def wait_registry_territories(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title == 'Список дворовых территорий и внутриквартальных проездов'
                assert self.content.search_setting.visible

                return self.content.table_list.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Паспорт дворовых территорий не загружен')
        self.app.restore_implicitly_wait()

    def wait_contracts_list(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.title == (
                    'Список договоров на выполнение работ по содержанию и благоустройству ' 'дворовых территорий'
                )
                assert self.content.search_setting.visible
                assert self.content.search.visible

                return self.content.table_list.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Паспорт дворовых территорий не загружен')
        self.app.restore_implicitly_wait()
