from behave import *

def fill_credentials(context, username, password):
    driver = context.browser
    driver.find_element_by_id("input-email").send_keys(username)
    driver.find_element_by_id("input-password").send_keys(password)
    

def invalid_login(context):
    warning = context.browser.find_element_by_xpath("//body/div[2]/div").text
    assert("Warning: No match for E-Mail Address and/or Password." == warning)

def registration_url(context):
    driver = context.browser
    driver.get(context.registration_url)

def registration_fields(context, first_name, last_name, email, telephone, address_1, city, post_code, password):
    #filling fields
    context.browser.find_element_by_id("input-firstname").send_keys(first_name)
    context.browser.find_element_by_id("input-lastname").send_keys(last_name)
    context.browser.find_element_by_id("input-email").send_keys(email)
    context.browser.find_element_by_id("input-telephone").send_keys(telephone)
    context.browser.find_element_by_id("input-address-1").send_keys(address_1)
    context.browser.find_element_by_id("input-city").send_keys(city)
    context.browser.find_element_by_id("input-postcode").send_keys(post_code)
    context.browser.find_element_by_id("input-country").click()
    context.browser.find_element_by_css_selector("option:nth-child(240)").click()
    context.browser.find_element_by_id("input-zone").click()
    context.browser.find_element_by_css_selector("#input-zone > option:nth-child(3)").click()
    context.browser.find_element_by_id("input-password").send_keys(password)
    context.browser.find_element_by_id("input-confirm").send_keys(password)

def check_if_logged_in(context):
    dropdownMenu = context.browser.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click()
    register_button = context.browser.find_element_by_xpath("//a[contains(text(),'My Account')]")
    register_button.click()
    url = context.browser.current_url
    assert("http://mys01.fit.vutbr.cz:8041/index.php?route=account/account" == url)

@given('a web browser is at the register page of opencart')
def step(context):
    driver = context.browser.get(context.homepage)
    dropdownMenu = context.browser.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click()
    register_button = context.browser.find_element_by_xpath("//a[contains(text(),'Register')]")
    register_button.click()
    url = context.browser.current_url
    assert("http://mys01.fit.vutbr.cz:8041/index.php?route=account/register" == url)

@given('a web browser is at the login page of opencart')
def step(context):
    driver = context.browser.get(context.homepage)
    dropdownMenu = context.browser.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click()
    loginButton = context.browser.find_element_by_xpath("//a[contains(text(),'Login')]")
    loginButton.click()


@given('registered user')
def step(context):
    pass

@when('user fills all required login fields correctly')
def step(context):
    fill_credentials(context, "adrej@gmail.com", 'asda123.A')

@when('user fills all login fields with invalid credentials')
def step(context):
    fill_credentials(context, "wronguser@gmail.com", 'asd')

@when('user fills correct username and incorrect password')
def step(context):
    fill_credentials(context, "andrejkojezik@gmail.com", '84112sa')

@when('user does not fill all login required fields')
def step(context):
    fill_credentials(context, "andrejkojezik@gmail.com", '')

@given('unregistered user')
def step(context):
    pass

@when('user fills all required registration fields correctly')
def step(context):
    registration_fields(context, "Andrej", "AJ", "adrej@gmail.com", "+421950444222", "machackova 35", "Bratislava", "04712" ,"asda123.A" )

@when('user fills required registration fields with incorrect data')
def step(context):
    registration_fields(context, "adulienko", "aj", "ajassmail.com", "+421950444222", "machackova 35", "Bratislava", "04712" ,"asda123.A" )

@when('user does not fill all required registration fields')
def step(context):
    registration_fields(context, "adulienko", "aj", "", "+421950444222", "machackova 35", "Bratislava", "04712" ,"asda123.A" )

@when('user presses "Continue"')
def step(context):
    context.browser.find_element_by_xpath("//input[@value='Continue']").click()

@when('user presses "Login"')
def step(context):
    context.browser.find_element_by_xpath("//input[@value='Login']").click()

@when('user accepts terms of privacy policy')
def step(context):
    context.browser.find_element_by_xpath("//input[@name='agree']").click()

@then('account is created')
def step(context):
    message = context.browser.find_element_by_xpath("//div[@id='content']/h1").text
    assert("Your Account Has Been Created!" == message)

@then('account is not created')
def step(context):
    message = context.browser.find_element_by_xpath("//div[@id='content']/h1").text
    assert("Your Account Has Been Created!" != message)

@then('user is logged in')
def step(context):
    check_if_logged_in(context)

@then('user is not logged in')
def step(context):
    driver = context.browser.get(context.homepage)
    dropdownMenu = context.browser.find_element_by_xpath("//span[contains(.,'My Account')]")
    dropdownMenu.click()
    register_button = context.browser.find_element_by_xpath("//a[contains(text(),'My Account')]")
    register_button.click()
    url = context.browser.current_url
    assert("http://mys01.fit.vutbr.cz:8041/index.php?route=account/account" != url)

def delete_all_users(context):
    fill_credentials_admin(context)
    context.browser.find_element_by_xpath("//button[@type='submit']").click()
    #get to customers
    customersButton = context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div[3]/div/div[3]/a")
    customersButton.click()
    #select all
    context.browser.find_element_by_xpath("//form[@id='form-customer']/div/table/thead/tr/td").click()
    #delete
    context.browser.find_element_by_xpath("//button[@type='button']").click()    
    alert = context.browser.switch_to.alert
    alert.accept()
    
def fill_credentials_admin(context):
    driver = context.browser
    context.browser.get(context.login_admin)
    driver.find_element_by_id("input-username").send_keys("admin")
    driver.find_element_by_id("input-password").send_keys("admin")

