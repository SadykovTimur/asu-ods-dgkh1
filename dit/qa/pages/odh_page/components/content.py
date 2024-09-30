from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    title = Text(tag='h3')
    title_form = Text(tag="h1")
    printer = Component(css='[class*="Print"]')
    table = Component(id="tableContainer")
    form = Component(class_name="form-table")
    district = Component(xpath='//label[text()="Округ:"]')
    category_object = Component(xpath='//label[text()="Категория объекта:"]  ')

    @property
    def is_visible(self) -> bool:
        assert 'Сводка по объектам дорожного хозяйства' in self.title
        assert self.title_form == 'Главная'
        assert self.printer

        return self.table.visible


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
