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
    try:
        list_of_items=driver.find_elements(By.XPATH,  '//div[@class="s-item__title"]')
    except NoSuchElementException as NSE :
        print(NSE.msg)

    try:
        list_of_items_price = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    except NoSuchElementException as NSE :
        print(NSE.msg)

    print(type(list_of_items))
    print(type(list_of_items_price))
    # for i in len(list_of_items):
    #     print(list_of_items[i].text + "-" + list_of_items_price[i].text)

    # min_items=min(len_items,len_items_price)
    # print(min_items)
    # for i in list_of_items:
    #     print(i.text)
    # for j in list_of_items_price:
    #         print(j.text)

    titles=[]
    prices=[]

    for i, j in zip(list_of_items,list_of_items_price):
        titles.append(i.text)
        price = (j.text.replace('$', '').replace('to', ','))
        try:
            prices.append(float(price))
            print(f"{i.text} - {j.text}")
        except ValueError as e:
            continue

    print(prices)
    print(titles)
    print(len(titles))
    print(len(prices))
    # text_price = i.text.replace('$', '').replace(',', '')

    max_pval = max(prices)
    min_pval = min(prices)

    print(f"Max value in price list is: {max_pval}")
    print(f"Min value in price list is: {min_pval}")

