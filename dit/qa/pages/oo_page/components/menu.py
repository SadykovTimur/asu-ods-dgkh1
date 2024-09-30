from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    items = Components(css='[id="cssmenu"] td')
    place_garbage = Component(xpath='//a[contains(text(),"Места сбора")]')
    map_garbage = Button(xpath='//a[text()="Карта мест сбора отходов"]  ')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
