from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    panel_left = Component(css='[class*="HomeLeft"]')
    panel_right = Component(css='[class*="HomeRight"]')
    toolbar = Component(id="idCatalogToolbar")
    folders = Component(id="idCatalogFoldersAccordion")
    filters = Component(id="idCatalogFiltersBar")

    @property
    def is_visible(self) -> bool:
        assert self.panel_left.visible

        return self.panel_right.visible


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
