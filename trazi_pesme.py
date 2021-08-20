import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


base_url = 'https://genius.com'


driver = webdriver.Firefox()

# driver.get(base_url)

# driver.find_element(By.XPATH, '//form/input').send_keys('zeljko joksimovic')


# driver.find_element(By.XPATH, '//form').submit()

# time.sleep(5)

# driver.find_element(By.XPATH,'//a[text() = "Show more songs"]').click()

driver.get('https://genius.com/search?q=zeljko%20joksimovic')

a = driver.find_element(By.XPATH,'//a[contains(@class, "full_width_button")]').click()

time.sleep(1)

scrolling

SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



info = driver.find_element_by_css_selector('.modal_window-content')
driver.execute_script("arguments[0].scrollIntoView(true);",info)
time.sleep(1)