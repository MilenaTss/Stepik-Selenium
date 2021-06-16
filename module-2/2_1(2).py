from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_tag_name("img")
    x = x.get_attribute("valuex")
    x = calc(x)

    inp = browser.find_element_by_css_selector('[id="answer"]')
    inp.send_keys(x)

    inp = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    inp.click()

    inp = browser.find_element_by_css_selector('[id="robotsRule"]')
    inp.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
