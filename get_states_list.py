from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import os
from glob import glob

PATH = "driver/chromedriver"
BASE_URL = "https://edap.epa.gov/public/extensions/newTRIsearch/newTRIsearch.html#"
DOWNLOAD_LOCATION = "/home/macbuntu/PycharmProjects/TRI/data"
chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {"download.default_directory": DOWNLOAD_LOCATION}
)
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
driver.get(BASE_URL)
# navigate to state tab


def get_states():

    try:
        sleep(25)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.LINK_TEXT, "State, County, City or ZIP Code")
            )
        ).click()

    except TimeoutException as e:
        print(e)
        print("<<<<<<<<<<<")

    states = [
        item.get_attribute("text")
        for item in driver.find_elements_by_xpath("//ul[@id='listState']/li/a")
    ]
    return states
