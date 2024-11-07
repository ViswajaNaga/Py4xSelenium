from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.description("ebay minimac name and price")
def test_ebay_minimac_details():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Electronics/bn_7000259124")
    driver.maximize_window()
    input_element=driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    input_element.send_keys("minimac")
    search_element=driver.find_element(By.ID,"gh-btn")
    search_element.click()
    # list_of_items_css=driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    list_of_items=driver.find_elements(By.XPATH,  '//div[@class="s-item__title"]')
    list_of_items_price = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    print(type(list_of_items))
    print(type(list_of_items_price))

    titles=[]
    prices=[]

    for i in list_of_items:
        titles.append(i.text)

    for j in list_of_items_price:
        newprice = j.replace("$", " ").replace("to", ",")
        prices.append(j.text)

    for i, j in zip(list_of_items, list_of_items_price):
        print(f"{i.text} - {j.text}")

    print(titles)
    print(prices)

    print(type(titles))
    print(type(prices))

    for value in prices:
        newprice=value.replace("$"," ").replace("to",",")
        print(newprice)
