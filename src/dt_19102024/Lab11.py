from selenium import webdriver
import allure
import time

from selenium.webdriver.common.by import By
@allure.description("Find all Buttons and links in a vwo web page")
def test_to_find_buttons_and_links_in_page():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
