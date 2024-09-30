from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Text(tag='h2')
    logo = Component(class_name="logo")
    menu_item = Components(class_name="head-menu__item")
    territories = Button(xpath='//a[text()="Дворовые территории"]')
    contracts = Button(xpath='//a[text()="Договоры"]')
    submenu = Component(class_name="head-submenu")
    change_pass = Component(css='[class*="change-pass"]')
    exit = Component(css='[class*="exit"]')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'Сводка по дворовым территориям и внутриквартальным проездам'
        assert self.logo.visible
        assert self.menu_item[0].visible
        assert self.change_pass.visible
        assert self.exit.visible

        return self.submenu.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
