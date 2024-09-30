from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Components
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.system_monitoring_page.components.header import Header

__all__ = ['SystemMonitoringPage']


class SystemMonitoringPage(Page):
    header = Header(tag="nav")
    menu = Text(class_name="menu")
    box_item = Components(css='[class*="index-box-item"] ')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert (
                    self.menu == 'ОПЕРАТИВНЫЕ ДАННЫЕ СВОДНАЯ ИНФОРМАЦИЯ ЭФФЕКТИВНОСТЬ ДОРОГИ ДВОРЫ ОТХОДЫ ОЦЕНКИ ОАТИ'
                )

                return self.box_item[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(
            condition, timeout=70, msg='Главная страница АРМ "Мониторинг работы заказчиков и подрядчиков" не загружена'
        )
        self.app.restore_implicitly_wait()
