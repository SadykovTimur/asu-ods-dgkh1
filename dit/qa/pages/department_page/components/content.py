from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

from dit.qa.pages.constants import title

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    map = Component(class_name="map")
    title = Components(tag='h2')

    @property
    def is_visible(self) -> bool:
        assert self.map.visible

        return title == [m.webelement.text for m in self.title]


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
