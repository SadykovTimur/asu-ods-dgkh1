from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    title = Text(class_name="section_header")
    filters = Component(class_name="filter")
    table = Component(class_name="list")
    search = Component(class_name="buttonsSearch")
    legend = Component(tag='fieldset')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'Реестр договоров субъектов системы санитарной очистки'
        assert self.filters.visible
        assert self.search.visible

        return self.table.visible


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
