from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test=\"login-button\"]").click()

    error = page.locator(".error-message-container")
    expect(error).to_have_text("Epic sadface: Username is required")


    browser.close()