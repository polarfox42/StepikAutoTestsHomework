import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element_by_css_selector("[name='firstname']")
element1.send_keys('Name')
element2 = browser.find_element_by_css_selector("[name='lastname']")
element2.send_keys('LastName')
element3 = browser.find_element_by_css_selector("[name='email']")
element3.send_keys('e@mai.l')
element4 = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
element4.send_keys(file_path)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()
