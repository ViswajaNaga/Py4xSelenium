from selenium import webdriver


def test_open_vwo_login():
    driver=webdriver.Chrome()  # this will create a POST request to create a new fresh copy of chrome
    # chrome -> sessionid ->
    driver.get("https://app.vwo.com")
    # code -> http request -->chromedriver(selenium manager) -->chrome(sessionId)
    print(driver.title) # Get request to get the title
    assert driver.title == "Login - VWO"
    