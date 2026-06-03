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
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator(".shopping_cart_link").click()

    #Checkout
    page.locator('[data-test="checkout"]').click()

    page.locator('[data-test="firstName"]').fill("Fulano")
    page.locator('[data-test="lastName"]').fill("De Tal")
    page.locator('[data-test="postalCode"]').fill("123456")

    page.locator('[data-test="continue"]').click()

    # Check Itens
    expect(page.locator('[data-test="item-4-title-link"]')).to_contain_text("Sauce Labs Backpack")
    expect(page.locator('[data-test="item-1-title-link"]')).to_contain_text("Sauce Labs Bolt T-Shirt")

    #Finish
    page.locator('[data-test="finish"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

    page.locator('[data-test="back-to-products"]').click()