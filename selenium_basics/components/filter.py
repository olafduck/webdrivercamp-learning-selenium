from components.base import Base


class LeftFilter(Base):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATOR = "// *"

    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)
        print(self.LOCATOR)
        print(option)
        print(visible)
