import time

from selene.support.shared import browser


def open_page(link):
    browser.open(link)


def set_data(a=None, b=None, c=None):
    browser.element('[class="js_a"]').type(a)
    browser.element('[class="js_b"]').type(b)
    browser.element('[class="js_c"]').type(c)


def submit():
    browser.element('[class="btn btn-submit"]').click()


def clear_data():
    browser.element('[class="js_a"]').clear()
    browser.element('[class="js_b"]').clear()
    browser.element('[class="js_c"]').clear()


def set_big_data(arg_a, arg_b, arg_c):
    for a, b, c in zip(arg_a, arg_b, arg_c):
        set_data(a=a, b=b, c=c)
        submit()
        clear_data()
