from framework.pages.base_page import BasePage

class CheckoutPage_STEP_TWO(BasePage):
    FINISH_SELECTOR = 'button:has-text("Finish")'
    ITEM_NAME_SELECTOR = '[data-test="inventory-item-name"]'
    COMPLETE_SELECTOR = '[data-test="complete-header"]'


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'

    def finish_form(self):
        self.assert_to_have_url("https://www.saucedemo.com/checkout-step-two.html") # добавляю проверку на URL
        self.assert_element_is_enabled(self.ITEM_NAME_SELECTOR) # проверяю кликабельность элемента
        self.wait_for_selector_and_click(self.FINISH_SELECTOR) # нажимаю на Finish
        self.assert_element_is_visible(self.COMPLETE_SELECTOR)
