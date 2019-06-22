'''
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной
странице мы добавили капчу для роботов, то есть тест, являющийся простым
для компьютера, но сложным для человека.

Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "Подтверждаю, что являюсь роботом".
Выбрать radiobutton "Роботы рулят!".
Нажать на кнопку Отправить.
Для этой задачи вам понадобится использовать атрибут .text для найденного
элемента. Обратите внимание, что скобки здесь не нужны:

x_element = browser.find_element_by_*(selector)
x = x_element.text
y = calc(x)
Атрибут text возвращает текст, который находится между открывающим
и закрывающим тегами элемента. Например, text для данного элемента
<div class="message">У вас новое сообщение.</div> вернёт строку:
"У вас новое сообщение".

Используйте функцию calc(), которая рассчитает и вернет вам значение функции,
которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало
вашего скрипта:

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом.
'''
import math, time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

element1 = browser.find_element_by_css_selector('#answer')
element1.send_keys(y)

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()

time.sleep(5)
browser.quit()
