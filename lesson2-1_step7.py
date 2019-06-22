'''
Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке",
точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука
с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x
для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "Подтверждаю, что являюсь роботом".
Выбрать radiobutton "Роботы рулят!".
Нажать на кнопку "Отправить".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из
предыдущей задачи.



Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже
и нажмите кнопку "Отправить", чтобы получить баллы за задание.
'''
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('[valuex]')
x = x_element.get_attribute('valuex')
y = calc(x)

element1 = browser.find_element_by_id('answer')
element1.send_keys(y)

option1 = browser.find_element_by_id('robotCheckbox')
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()
option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()
