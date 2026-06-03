from playwright.sync_api import sync_playwright, expect

#Login with empty field
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test=\"login-button\"]").click()

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username is required")

    browser.close()

#Login without password
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"username\"]").fill("testeabc")
    page.locator("[data-test=\"login-button\"]").click()

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Password is required")

    browser.close()

#Login without username
with sync_playwright() as p:

    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"password\"]").fill("1234")
    page.locator("[data-test=\"login-button\"]").click()

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username is required")

    browser.close()

#Invalid Login
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test=\"username\"]").fill("teste123")
    page.locator("[data-test=\"password\"]").fill("12345")
    page.locator("[data-test=\"login-button\"]").click()

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service")

    browser.close()

#Sucess Login
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    browser.close()