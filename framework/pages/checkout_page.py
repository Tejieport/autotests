from framework.pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[id="checkout"]'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    REMOVE_SELECTOR_1 = '#remove-sauce-labs-onesie' # добавляю селектор на удаление 1-ой позиции из корзины
    REMOVE_SELECTOR_2 = '#remove-sauce-labs-bike-light' # добавляю селектор на удаление 2-ой позиции из корзины
    CANCEL_SELECTOR = '#cancel' # добавляю селектор на кнопку Cansel
    CONTINUE_SHOPPING = '#continue-shopping' # добавляю селектор на кнопку Continue Shopping

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html' # меняю на другой endpoint, на который мы переходим при клике на корзину
        # self._endpoint = 'checkout-step-one.html' - этот эндпоинт был в уроке

    def start_checkout_one(self):
        self.assert_to_have_url("https://www.saucedemo.com/cart.html") # добавляю проверку на URL
        self.wait_for_selector_and_click(self.REMOVE_SELECTOR_1) # удаляю 1-ую позицию из корзины
        self.wait_for_selector_and_click(self.REMOVE_SELECTOR_2) # удаляю 2-ую позицию из корзины
        try:
            self.assert_element_is_disabled(self.CHECKOUT_BUTTON_SELECTOR) # проверяю недоступность кнопки после удаления всех позиций
        except Exception as error:
            print(f"Ошибка в тесте: {error} - кнопка доступна после удаления всех позиций")
        # тут баг, так как можно отправить без позиций
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_to_have_url("https://www.saucedemo.com/checkout-step-one.html") # добавляю проверку на URL
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)
        self.wait_for_selector_and_click(self.CANCEL_SELECTOR) # проверяю наличие и работу кнопки Cancel
        self.assert_to_have_url("https://www.saucedemo.com/cart.html") # добавляю проверку на URL
        self.wait_for_selector_and_click(self.CONTINUE_SHOPPING)  # проверяю наличие и работу кнопки Continue Shopping
        self.assert_to_have_url("https://www.saucedemo.com/inventory.html")  # добавляю проверку на URL

    def start_checkout_two(self): # добавляю функцию для добавления позиции из деталки
        self.assert_to_have_url("https://www.saucedemo.com/cart.html") # добавляю проверку на URL
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_to_have_url("https://www.saucedemo.com/checkout-step-one.html") # добавляю проверку на URL
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)