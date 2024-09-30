from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Nav']


class NavWrapper(ComponentWrapper):
    home = Component(xpath='//a[text()="Главная"]')
    repair = Component(xpath='//a[text()="Ремонт"]')
    reductions = Component(xpath='//a[text()="Снижения"]')
    nsi = Component(xpath='//a[text()="НСИ"]')
    snow = Component(xpath='//span[text()="СНЕГ"]')
    logout = Button(xpath='//a[text()="Выход"]')
    title_list = Component(xpath="//a[contains(text(),'Титульный список')]")
    recovery_pass = Component(xpath="//a[contains(text(),'Смена пароля')]")

    @property
    def is_visible(self) -> bool:
        assert self.home.visible
        assert self.repair.visible
        assert self.reductions.visible
        assert self.nsi.visible
        assert self.snow.visible
        assert self.title_list.visible
        assert self.recovery_pass.visible

        return self.logout.visible


class Nav(Component):
    def __get__(self, instance, owner) -> NavWrapper:
        return NavWrapper(instance.app, self.find(instance), self._locator)
