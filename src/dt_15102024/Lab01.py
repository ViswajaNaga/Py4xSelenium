from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title of the webpage google.com")
def test_sample():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    driver.current_url
    assert driver.current_url == "https://www.google.com/"
    driver.title
    assert driver.title == "Google"
