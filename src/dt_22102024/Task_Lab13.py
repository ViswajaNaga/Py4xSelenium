from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By

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
    list_of_items_price=driver.find_elements(By.CSS_SELECTOR,  ".s-item__price")
    # for i in len(list_of_items):
    #     print(list_of_items[i].text + "-" + list_of_items_price[i].text)
    #
    # len_items=len(list_of_items)
    # len_items_price=len(list_of_items_price)
    # min_items=min(len_items,len_items_price)
    # print(min_items)
    # print(list_of_items[1].text)
    # print(len(list_of_items))
    for i in list_of_items:
        print(i.text)

    assert len(list_of_items)==62
    time.sleep(3)