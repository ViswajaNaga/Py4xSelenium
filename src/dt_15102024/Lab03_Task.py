from selenium import webdriver
import allure

def test_katalon_demo():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.title
    driver.current_url
    page_source_data=driver.page_source
    print(page_source_data)
    assert "CURA Healthcare Service" in page_source_data
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"



