from get_states_list import *

states = get_states()

# loop through the list of states for robustness
for state in states:
    # choose state by clicking on button
    dropdown_state_btn = driver.find_element_by_id("dropdownState")
    dropdown_state_btn.click()
    # choose li item
    state_btn = driver.find_element_by_link_text(f"{state}")
    state_btn.click()
    # click View search results
    results_link = driver.find_element_by_id("btnHomeTRI")
    results_link.click()
    # Wait for button to be available and navigate to releases left tab
    try:
        sleep(3)
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Releases"))
        ).click()
    except Exception as e:
        print(e)
    # allow data to load
    sleep(10)
    # click download button
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "download-releases"))
    ).click()
    sleep(7)  # allow download time
    print(f"<><><><>DATA DOWNLOADED for {state}<><><><><>")
    # repeat for next state
    driver.refresh()

    try:
        sleep(4)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "fsrFocusFirst"))
        ).click()

    except TimeoutException:
        print("Pop up not encountered")
    # navigate to state tab
    try:
        sleep(25)  # page load
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.LINK_TEXT, "State, County, City or ZIP Code")
            )
        ).click()

    except TimeoutException as e:
        print(e)
        print("<<<<<<<<<<<")
