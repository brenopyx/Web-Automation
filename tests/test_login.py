from playwright.sync_api import sync_playwright, expect

def login(page, username= "", password= ""):
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

#Login with empty field
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    login(page)

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username is required")

#Login without password
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    login(page, "teste123", "")

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Password is required")

    browser.close()

#Login without username
with sync_playwright() as p:

    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    login(page, "", "12345")

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username is required")

    browser.close()

#Invalid Login
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    login(page, "teste123", "12345")

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service")

    browser.close()

#Sucess Login
with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    login(page, "standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    browser.close()