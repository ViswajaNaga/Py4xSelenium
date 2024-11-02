from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By

@allure.description("awesomeqa login page")
def test_to_login_awesomeqa():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()
    first_name_element=driver.find_element(By.XPATH,'//input[@id="input-firstname"]')
    first_name_element.send_keys("Viswaja")
    last_name_element=driver.find_element(By.ID,"input-lastname")
    last_name_element.send_keys("Naga")
    email_element=driver.find_element(By.NAME,"email")
    email_element.send_keys("abrfqg@gmail.com")
    phone_element=driver.find_element(By.XPATH,'//input[@type="tel"]')
    phone_element.send_keys("8907896789")
    password_element=driver.find_element(By.XPATH,"//input[@type='password']")
    password_element.send_keys("qwertyui")
    confirm_password_element=driver.find_element(By.XPATH,"//input[@class='form-control' and @id='input-confirm']")
    confirm_password_element.send_keys("qwertyui")
    subscribe_element=driver.find_element(By.XPATH,"//input[@type='radio' and @value='0']")
    subscribe_element.click()
    checkbox_element=driver.find_element(By.XPATH,"//input[@type='checkbox' and @value='1']")
    checkbox_element.click()
    submit_element=driver.find_element(By.XPATH,"//input[@type='submit']")
    submit_element.click()
    source_page=driver.page_source
    assert "Your Account Has Been Created!" in source_page
    time.sleep(3)
    # account_created_element=driver.find_elements(By.TAG_NAME,"h1")
    # assert account_created_element == "Your Account Has Been Created!"

