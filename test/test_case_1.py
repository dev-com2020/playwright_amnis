def test_home_page_title(page):
    page.goto('http://demo-store.seleniumacademy.com/')
    assert page.title() == "Madison Island", "Tytuł strony nie odpowiada zależności"


def test_navigation(page):
    page.goto('http://demo-store.seleniumacademy.com/')
    men_button = page.query_selector('//*[@id="nav"]/ol/li[2]/a')
    men_button.hover()
    page.click('//*[@id="nav"]/ol/li[2]/ul/li[2]/a')
    page.wait_for_timeout(2000)
    products = page.query_selector_all('.products-grid .item')
    page.screenshot(path='zrzut1.png')
    assert len(products) > 0, "nie znaleziono produktów"


def test_search_functional(page):
    page.goto('http://demo-store.seleniumacademy.com/')
    search_box = page.locator('input#search')
    search_box.fill('shirt')
    search_box.press('Enter')
    page.wait_for_timeout(2000)
    products = page.query_selector_all('.products-grid .item')
    page.screenshot(path='zrzut2.png')
    assert len(products) > 0

# "user@seleniumacademy.com"
# "tester"


