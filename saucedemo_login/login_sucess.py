from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


    browser.close()