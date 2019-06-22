from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector('[type="submit"]')
button1.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element_by_id('input_value')
x = x_element.text

answer = browser.find_element_by_id('answer')
answer.send_keys(calc(int(x)))

button2 = browser.find_element_by_css_selector('[type="submit"]')
button2.click()