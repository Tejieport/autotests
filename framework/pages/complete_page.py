from framework.pages.base_page import BasePage

class CompletePage(BasePage):
    MENU_SELECTOR = '#react-burger-menu-btn'
    BACK_HOME_SELECTOR = '[data-test="back-to-products"]'
    BM_MENU_SELECTOR = 'div.bm-menu'
    CLOSE_MENU_SELECTOR = '#react-burger-cross-btn'
    LOGOUT_SELECTOR = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'

    def complete_form(self):
        self.assert_to_have_url("https://www.saucedemo.com/checkout-complete.html") # добавляю проверку на URL
        self.assert_element_is_enabled(self.BACK_HOME_SELECTOR) # проверяю кликабельность элемента
        self.wait_for_selector_and_click(self.MENU_SELECTOR) # нажимаю на Меню - 3 полоски
        self.assert_element_is_visible(self.BM_MENU_SELECTOR) # проверяю открытие меню
        self.wait_for_selector_and_click(self.CLOSE_MENU_SELECTOR) # закрываю меню
        self.assert_element_is_hidden(self.BM_MENU_SELECTOR)  # проверяю невидимость меню
        self.wait_for_selector_and_click(self.MENU_SELECTOR) # нажимаю на Меню - 3 полоски
        self.wait_for_selector_and_click(self.LOGOUT_SELECTOR)  # нажимаю Logout