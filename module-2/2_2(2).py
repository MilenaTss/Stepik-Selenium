from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x = x.text
    x = calc(x)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    print("aaaa")
    # browser.execute_script("window.scrollBy(0, 100);")

    y = browser.find_element_by_class_name("form-control")
    y.send_keys(x)

    y = browser.find_element_by_id("robotCheckbox")
    y.click()

    y = browser.find_element_by_id("robotsRule")
    y.click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
