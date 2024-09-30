from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    setting_line = Component(class_name="setting_line")
    search_setting = Component(class_name="search__setting")
    table = Component(id="dataTableMainStatPref")
    search = Component(class_name="button_save")
    table_list = Component(class_name="list")

    @property
    def is_visible(self) -> bool:
        assert self.setting_line.visible

        return self.table.visible


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
