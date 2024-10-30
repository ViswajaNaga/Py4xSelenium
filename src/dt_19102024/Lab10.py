from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
@allure.description("Find all Buttons and links in a vwo web page")
def test_to_find_buttons_and_links_in_page():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #tag_name
    buttons=driver.find_elements(By.TAG_NAME,"button")
    print(len(buttons))

    for i in buttons:
        print(i.text)


    links=driver.find_elements(By.TAG_NAME,"a")
    print(len(links))

    for i in links:
        print(i.text)

    driver.back()
