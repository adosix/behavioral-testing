from behave import *
from account import fill_credentials, check_if_logged_in,delete_all_users
from selenium.webdriver.support.ui import WebDriverWait

@given('user is logged in')
def step(context):
    driver = context.browser.get(context.login)
    fill_credentials(context, "adrej@gmail.com", 'asda123.A')
    context.browser.find_element_by_xpath("//input[@value='Login']").click()
    WebDriverWait(context.driver, 10)
    check_if_logged_in(context)

@given('a web browser is at the home page of opencart')
def step(context):
    driver = context.browser.get(context.homepage)

@given('user has empty cart')
def step(context):
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//*[contains(text(), '0 item(s) - $0.00')]")

@when('user clicks on "ADD TO CART" under item')
def step(context):
    context.browser.find_element_by_css_selector(".product-layout:nth-child(1) button:nth-child(1)").click()

@then('user has one item in the cart')
def step(context):
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//*[contains(text(), '1 item(s)')]")

@given('one item is in the cart')
def step(context):
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//*[contains(text(), '1 item(s)')]")

@then('there are two items in the cart')
def step(context):
    driver = context.browser.get(context.homepage)
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//*[contains(text(), '2 item(s)')]")

@given('there are two items in the cart')
def step(context):
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//*[contains(text(), '2 item(s)')]")

@when('user clicks on the "checkout"')
def step(context):
    driver = context.browser.get(context.cart)
    WebDriverWait(context.driver, 5)
    context.browser.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()

@then("user is redirected to the checkout page")
def step(context):
    WebDriverWait(context.driver, 5)
    url = context.browser.current_url
    assert("http://mys01.fit.vutbr.cz:8041/index.php?route=checkout/checkout" == url)

@given("a web browser is at the checkout page")
def step(context):
    WebDriverWait(context.driver, 5)
    driver = context.browser.get(context.cart)
    url = context.browser.current_url
    assert("http://mys01.fit.vutbr.cz:8041/index.php?route=checkout/checkout" == url)

@when('user fills billing details')
def step(context):
    pass

@when('user clicks on the "continue"')
def step(context):
    context.browser.find_element_by_id("button-payment-address").click()

@then('order is created')
def after(context):
    delete_all_users(context)