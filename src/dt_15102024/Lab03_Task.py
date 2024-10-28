from selenium import webdriver
import allure


def test_katalon_demo():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.title
    driver.current_url
    print(driver.page_source)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
 #   assert driver.page_source == "CURA Healthcare Service"


