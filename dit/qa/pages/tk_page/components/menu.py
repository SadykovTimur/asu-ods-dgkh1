from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    map = Component(xpath='//em[text()="Карта"]')
    routes = Component(xpath='//a[text()="Маршруты"]')
    registry = Button(xpath='//a[text()="Реестры"]')
    report = Component(xpath='//a[text()="Отчеты"]')
    protocol = Component(xpath='//a[text()="Протокол"]')
    nsi = Component(xpath='//a[text()="НСИ"]')
    change_pass = Component(xpath='//a[text()="Смена пароля"]')
    logout = Component(xpath='//a[text()="Выход"]')

    @property
    def is_visible(self) -> bool:
        assert self.map.visible
        assert self.routes.visible
        assert self.registry.visible
        assert self.report.visible
        assert self.protocol.visible
        assert self.nsi.visible
        assert self.change_pass.visible

        return self.logout.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
