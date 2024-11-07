from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

@allure.description("App.vwo.com--> Fluent Wait")
def test_negative_vwo_login_fluent_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("abc@gmail.com")

    signin_web_element = driver.find_element(By.ID, "js-login-btn")
    signin_web_element.click()

    # wait for some time

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    # Fluent wait
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list)
     .until(EC.visibility_of_element_located
            ((By.CLASS_NAME, "notification-box-description"))
            )
     )
# Smart Logic to wait for the element
# Condition based Logic

# Verify that message is visible.
    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    driver.quit()
