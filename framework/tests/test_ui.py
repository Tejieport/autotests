from framework.pages.login_page import LoginPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.checkout_page_2 import CheckoutPage_STEP_ONE
from framework.pages.checkout_page_3 import CheckoutPage_STEP_TWO
from framework.pages.complete_page import CompletePage

# @pytest.mark.xfail(reason="Тесты падают - по причинам:"
#                           "1. Активная кнопка Checkout при пустой корзине;"
#                           "")
def test_checkout_order(custom_browser):
    page = custom_browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_page_1 = CheckoutPage_STEP_ONE(page)
    checkout_page_2 = CheckoutPage_STEP_TWO(page)
    complete_page = CompletePage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_two_item_to_cart()
    checkout_page.start_checkout_one()
    inventory_page.add_one_item_in_detal_cart_to_cart()
    checkout_page.start_checkout_two()
    checkout_page_1.fill_checkout_form('-1 baba клава !', '-1 baba клава !', '-1 baba клава !')
    checkout_page_2.finish_form()
    complete_page.complete_form()

















# # Создаем экземпляр Playwright и запускаем его
# automation_project = sync_playwright().start()
#
# # Далее, используя объект automation_project, можно запускать браузер и работать с ним
# browser = automation_project.chromium.launch(headless=False, slow_mo=1000)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
# page.type(selector='[id="user-name"]', text="standard_user", delay=100)
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button') # [class='submit-button']
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
# page.wait_for_selector('#inventory_container')
#
# button_add_cart= '[data-test="add-to-cart-sauce-labs-backpack"]'
# alt_locator_for_card='.inventory_item a:has-text("Sauce Labs Backpack")'
# card_button='.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
#
# page.is_visible(selector=button_add_cart)
# page.is_enabled(selector=button_add_cart)
# # page.click(selector=button_add_cart)
# # page.click(selector=alt_locator_for_card)
# page.click(card_button)
# page.is_visible('[data-test="shopping-cart-link"]')
# page.click('[data-test="shopping-cart-link"]')
# page.wait_for_url('https://www.saucedemo.com/cart.html', timeout=10000)
# button_checkout = '#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(button_checkout)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html', timeout=10000)
#
# page.fill(selector='#first-name', value='First Name')
# page.fill(selector='#last-name', value='Last Name')
# page.fill(selector='#postal-code', value='67896789')
#
# page.click('[id="continue"][type="submit"]')
# page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html', timeout=10000)
# page.wait_for_selector('button:has-text("Finish")')
# page.click('button:has-text("Finish")')
# page.wait_for_url('https://www.saucedemo.com/checkout-complete.html', timeout=10000)
# page.wait_for_selector('#back-to-products')
# page.click('button:has-text("Back Home")')
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
#
# time.sleep(5)
#
# # После выполнения необходимых действий, следует явно закрыть браузер
# browser.close()
#
# # И остановить Playwright, чтобы освободить ресурсы
# automation_project.stop()