from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(class_name="HeaderLogo")
    brand_name = Component(css='[class*="BrandName"]')
    catalog = Button(id="catalog")
    search = Component(class_name="HeaderQuickSearch")
    title = Text(id="idHeaderTitleCell")
    menu = Component(css='[class*="NavMenubar"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.brand_name.visible
        assert self.search.visible
        assert self.title == 'Начальная страница'

        return self.menu.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
