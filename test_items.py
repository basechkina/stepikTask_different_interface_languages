link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_should_be_on_the_page(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert add_to_basket_button, "Button 'Add to basket' not found"
