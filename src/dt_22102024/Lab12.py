from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By

@allure.description("awesomeqa login page")
def test_to_login_awesomeqa():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()
    first_name_element=driver.find_element(By.CSS_SELECTOR,'input[id="input-firstname"]')
    first_name_element.send_keys("Viswaja")
    time.sleep(3)