from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def test_chrome_options():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,900")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-infobars") --now not in use

    driver=webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/") # navigate to url
    # chrome opens in incognito mode
    time.sleep(5)