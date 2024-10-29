from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By

@allure.title("check if user able to click on Make appointment")
def test_chrome_katalon_make_appointment():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

# 1.Find the element by anchor tag
    # <a ----> open tag
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a> ----> close tag
# Find the element by Strategy and locator
# 2.we need to find the unique attribute which can find the web element
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
# 3.Click element
    make_appointment_element.click()
# 4.Verify that url changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    driver.quit()



