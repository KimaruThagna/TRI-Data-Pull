from selenium import webdriver
from time import sleep

PATH = "driver/chromedriver"


def parent_company(tr_id):
    tr_id = tr_id.replace(" ", "")
    facility_url = f"https://enviro.epa.gov/facts/tri/ef-facilities/#/Facility/{tr_id}"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get(facility_url)
    sleep(3)
    parent_co = driver.find_elements_by_xpath(
        "//table/tbody/tr//td[@headers='parentCo']"
    )
    parent_co = parent_co[1].text
    driver.quit()
    if parent_co == "":
        return "NA"
    else:
        return parent_co
