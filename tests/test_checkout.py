from playwright.sync_api import sync_playwright, expect

def login(page, username, password):
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

def add_to_cart(page):
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator(".shopping_cart_link").click()

def checkout(page, first_name= "", last_name= "", code= ""):
    page.locator('[data-test="checkout"]').click()

    page.locator('[data-test="firstName"]').fill(first_name)
    page.locator('[data-test="lastName"]').fill(last_name)
    page.locator('[data-test="postalCode"]').fill(code)

    page.locator('[data-test="continue"]').click()

def verify_itens(page, final_products):
    checkout = page.locator('[data-test="inventory-item"]')
    assert checkout.count() == len(final_products)

    for produto in final_products:
        expect(page.locator("body")).to_contain_text(produto)

def finish(page):
    page.locator('[data-test="finish"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

    page.locator('[data-test="back-to-products"]').click()

def verify_error(page, message):
    error = page.locator(".error-message-container")
    expect(error).to_have_text(message)

# Checkout withou FirstName
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page,"standard_user", "secret_sauce")
    
    #Add item no carrinho
    add_to_cart(page)

    #Checkout
    checkout(page, "", "de Tal", "123456") 

    verify_error(page, "Error: First Name is required")

# Checkout without LastName
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page,"standard_user", "secret_sauce")
    
    #Add item no carrinho
    add_to_cart(page)

    #Checkout
    checkout(page, "Fulano", "", "123456") 

    verify_error(page, "Error: Last Name is required")

# Checkout without Postal Code
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page,"standard_user", "secret_sauce")
    
    #Add item no carrinho
    add_to_cart(page)

    #Checkout
    checkout(page, "Fulano", "de Tal", "") 

    verify_error(page, "Error: Postal Code is required")

# Checkout Success
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
  
    page.goto("https://www.saucedemo.com/")

    # Login
    login(page,"standard_user", "secret_sauce")
    
    #Add item no carrinho
    add_to_cart(page)

    #Checkout
    checkout(page, "Fulano", "de Tal", "123456")

    # Check Itens
    verify_itens(page, ["Sauce Labs Backpack","Sauce Labs Bolt T-Shirt"])

    #Finish
    finish(page)