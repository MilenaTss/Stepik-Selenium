from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_name("firstname")
    x.send_keys("AAA")

    x = browser.find_element_by_name("lastname")
    x.send_keys("AAA")

    x = browser.find_element_by_name("email")
    x.send_keys("AAA")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'a.txt')

    f = browser.find_element_by_id("file")
    f.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
