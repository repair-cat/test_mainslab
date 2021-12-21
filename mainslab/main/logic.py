import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data(word):
    mass = {}
    count = 1
    index = 0
    mass[index] = {}

    chromedriver = r"D:\downloads\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://audatex.ru")
    input_form = driver.find_element(By.XPATH, '//input[@class="txt"]')
    input_form.send_keys(word)
    driver.find_element(By.XPATH, '//input[@value="ПОИСК"]').click()
    data = driver.find_element(By.XPATH, '//ul[@class="searchres"]')

    for item in data.text.split('\n'):
        if count % 2 == 0 and len(item) > 0:
            mass[index].update({'description': item})

        elif re.search(r"http", item):
            mass[index].update({'url': item})

        else:
            if len(item) > 0:
                mass[index].update({'title': item})

        if len(mass[index]) == 3:
            index += 1
            mass[index] = {}
        count += 1

    return mass


# for key, val in get_data("bmw").items():
#     print(key, val)