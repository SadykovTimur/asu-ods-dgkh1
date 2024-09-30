from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(class_name="logo")
    contact = Component(id="open-modal-contact")
    access = Component(id="open-modal-access")
    appeal = Component(id="open-modal-appeal")
    review = Component(css='[class*="sold-link"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.contact.visible
        assert self.access.visible
        assert self.appeal.visible

        return self.review.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
