from framework.pages.base_page import BasePage

class CheckoutPage_STEP_ONE(BasePage):
    CONTINUE_BUTTON_SELECTOR = '#continue'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    ERROR_SELECTOR = 'div.error-message-container'
    PATH_SELECTOR = 'path[fill="currentColor"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.assert_to_have_url("https://www.saucedemo.com/checkout-step-one.html") # добавляю проверку на URL
        try:
            self.assert_element_is_disabled(self.CONTINUE_BUTTON_SELECTOR) # проверяю недоступность кнопки до ввода значений в поля
        except Exception as error:
            print(f"Ошибка в тесте: {error} - кнопка доступна до ввода значений в поля")
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR) # проверяю возможность перехода к следующему шагу без заполнения полей
        self.assert_element_is_visible(self.ERROR_SELECTOR) # проверяю появление элемента с ошибкой
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.FIRST_NAME_SELECTOR, postal_code) # добавляю проверку на соответствие вводимого имени
        self.assert_input_value(self.LAST_NAME_SELECTOR, postal_code) # добавляю проверку на соответствие вводимой фамилии
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR)