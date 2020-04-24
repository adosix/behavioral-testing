#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from behave import *

def before_scenario(context, feature):
    # Connect selenium Remote server
    context.browser = webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub",
                                       desired_capabilities=DesiredCapabilities.FIREFOX)
    context.browser.set_page_load_timeout(15)
    context.homepage = "http://mys01.fit.vutbr.cz:8041"
    context.cart = "http://mys01.fit.vutbr.cz:8041/index.php?route=checkout/cart"
    context.login = "http://mys01.fit.vutbr.cz:8041/index.php?route=account/login"
    context.login_admin = "http://mys01.fit.vutbr.cz:8041/admin"
    context.checkout = "http://mys01.fit.vutbr.cz:8041/index.php?route=checkout/checkout"