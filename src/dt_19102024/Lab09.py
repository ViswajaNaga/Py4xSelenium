from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By
@allure.description("Verify Start a free trial is working properly and able to navigate")
def test_positive_vwo_Start_Free_Trail_project3():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #<a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # LINK_TEXT = EXACT MATCH
    anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.back()

    # PARTIAL_LINK_TEXT = contains
    anchor_tag_element=driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    anchor_tag_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
