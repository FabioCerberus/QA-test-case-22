#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Click on 'Products' button
#4. Verify that Brands are visible on left side bar
#5. Click on any brand name
#6. Verify that user is navigated to brand page and brand products are displayed
#7. On left side bar, click on any other brand link
#8. Verify that user is navigated to that brand page and can see products

from playwright.sync_api import sync_playwright, expect

def test_view_category_products():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        expect(page).to_have_title("Automation Exercise")

        page.get_by_role("link", name=" Products").click()

        expect(page.locator(".left-sidebar")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Brands")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Polo")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("H&M")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Madame")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Mast & Harbour")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Babyhug")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Allen Solly Junior")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Kookie Kids")).to_be_visible()
        expect(page.locator(".left-sidebar").get_by_text("Biba")).to_be_visible()

        #I should write a variable for these functions so that I don't have to write a code for each of the brands
        page.locator('.left-sidebar a[href="/brand_products/Polo"]').click()
        expect(page.locator(".title.text-center").get_by_text("Polo")).to_be_visible()

        page.locator('.left-sidebar a[href="/brand_products/H&M"]').click()
        expect(page.locator(".title.text-center").get_by_text("H&M")).to_be_visible()

        browser.close()
