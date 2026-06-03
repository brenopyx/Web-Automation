from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    #Add item no carrinho
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator(".shopping_cart_link").click()
    
    #Verificar item no carinho e validar
    carrinho_itens = page.locator('[data-test="inventory-item"]')
    assert carrinho_itens.count() == 2
    expect(page.locator('[data-test="item-4-title-link"]')).to_contain_text("Sauce Labs Backpack")
    expect(page.locator('[data-test="item-0-title-link"]')).to_contain_text("Sauce Labs Bike Light")
    
    #Remover Bike light do carrinho
    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
    assert carrinho_itens.count() == 1

    #Volta para lista de produtos
    page.locator(".bm-burger-button").click()
    page.locator('[data-test="inventory-sidebar-link"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    #Volta para o carrinho e verifica
    page.locator(".shopping_cart_link").click()
    expect(page.locator('[data-test="item-4-title-link"]')).to_contain_text("Sauce Labs Backpack")
    expect(page.locator('[data-test="item-1-title-link"]')).to_contain_text("Sauce Labs Bolt T-Shirt")
    assert carrinho_itens.count() == 2

    browser.close()
