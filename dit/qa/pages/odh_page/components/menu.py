from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    home = Component(xpath='//a[text()="Главная"]')
    registry = Component(xpath='//a[text()="Реестры"]')
    registry_passport = Button(xpath='//a[text()="Реестр паспортов ОДХ"]')
    title_list = Component(xpath='//a[text()="Титульные списки"]')
    data_title_list = Button(xpath='//a[text()="Данные титульного списка"]')
    contracts = Component(xpath='//a[text()="Контракты"]')
    contracts_odh = Button(xpath='//a[text()="Контракты на содержание ОДХ"]')
    journal = Component(xpath='//a[text()="Журнал"]')
    directory = Component(xpath='//a[text()="Справочники"]')

    @property
    def is_visible(self) -> bool:
        assert self.home.visible
        assert self.registry.visible
        assert self.title_list.visible
        assert self.contracts.visible
        assert self.journal.visible

        return self.directory.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
