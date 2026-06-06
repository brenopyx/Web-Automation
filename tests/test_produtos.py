from playwright.sync_api import sync_playwright, expect

def login(page, username, password):
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

def add_to_cart(page):
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator(".shopping_cart_link").click()

def validate_cart(page, expected_products):
    carrinho_itens = page.locator('[data-test="inventory-item"]')
    assert carrinho_itens.count() == len(expected_products)

    for produto in expected_products:
        expect(page.locator("body")).to_contain_text(produto)

def remove_product(page):
    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
    carrinho_itens = page.locator('[data-test="inventory-item"]')
    assert carrinho_itens.count() == 1

def return_home(page):
    page.locator(".bm-burger-button").click()
    page.locator('[data-test="inventory-sidebar-link"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator(".shopping_cart_link").click()

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page, "standard_user", "secret_sauce")

    #Add item no carrinho
    add_to_cart(page)
    
    #Verificar item no carinho e validar
    validate_cart(page, ["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    
    #Remover Bike light do carrinho
    remove_product(page)

    #Volta para lista de produtos
    return_home(page)

    #Volta para o carrinho e verifica
    validate_cart(page, ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"])
    
    browser.close()
