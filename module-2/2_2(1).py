from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("num1")
    x2 = browser.find_element_by_id("num2")
    x1 = int(x1.text)
    x2 = int(x2.text)
    x = x1 + x2
    print(x)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
