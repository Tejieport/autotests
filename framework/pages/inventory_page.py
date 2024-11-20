from framework.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR_1 = "#add-to-cart-sauce-labs-bike-light" # меняю селектор на закупочную позицию
    ADD_TO_CART_SELECTOR_2 = "#add-to-cart-sauce-labs-onesie" # добавляю селектор на еще одну закупочную позицию
    SHOPPING_CART_LINK_SELECTOR = '[data-test="shopping-cart-link"]'
    SHOPPING_CART_BADGE_SELECTOR = '[data-test="shopping-cart-badge"]' # добавляю селектор на отображаемую цифру в корзине
    DETAL_ITEM_SELECTOR = '[data-test="inventory-item-sauce-labs-backpack-img"]' # добавляю новый селектор, чтобы провалиться в деталку айтема
    DETAL_ITEM_ADD_TO_CART_SELECTOR = '[data-test="add-to-cart"]' # добавляю новый селектор кнопки add to cart в деталке айтема

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_two_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR_1)
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR_2) # добавляю еще одну закупочную позицию
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.assert_text_in_element(self.SHOPPING_CART_BADGE_SELECTOR, "2") #здесь добавляю проверку на цифру в корзине
        # тут может немного некорректно, так как мы должны сначала должны выполнить wait_for_selector, а потом проверить цифру,
        # то есть проверка должна быть между wait и click, но они у нас заложены в одну функцию
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def add_one_item_in_detal_cart_to_cart(self): # добавляю новую функцию на добавление позиции через детальную карточку
        self.wait_for_selector_and_click(self.DETAL_ITEM_SELECTOR)
        self.wait_for_selector_and_click(self.DETAL_ITEM_ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.assert_text_in_element(self.SHOPPING_CART_BADGE_SELECTOR, "1") #здесь добавляю проверку на цифру в корзине
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)


