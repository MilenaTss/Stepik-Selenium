from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('[id="input_value"]')
    x = x.text
    x = calc(x)

    inp = browser.find_element_by_css_selector('[class="form-control"]')
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
