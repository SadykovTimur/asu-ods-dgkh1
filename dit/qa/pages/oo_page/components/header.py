from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Text(tag='h1')
    logo = Component(class_name="logo")
    contact = Component(css='[class*="Contact"]')
    feedback = Component(css='[class*="Feedback"]')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'Сбор, вывоз и утилизация отходов'
        assert self.logo.visible
        assert self.contact.visible

        return self.feedback.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
