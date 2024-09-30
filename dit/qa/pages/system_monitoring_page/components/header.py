from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(class_name='navbar-brand')
    title = Text(class_name="logo-text")
    support = Component(css='[class*="support-box"]')
    date = Component(css='[class*="current-date-time"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.title == 'СИСТЕМА МОНИТОРИНГА РАБОТЫ ЗАКАЗЧИКОВ И ПОДРЯДЧИКОВ В КОМПЛЕКСЕ ГОРОДСКОГО ХОЗЯЙСТВА'
        assert self.support.visible

        return self.date.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
