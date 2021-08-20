
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import datetime
import time

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList',2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
m = 'muzika_leto21'
fp.set_preference("browser.download.dir", f'/home/upflo/Music/{m}')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mpeg")
fp.set_preference("browser.download.useDownloadDir", True);
fp.set_preference("pdfjs.disabled",True)
driver = webdriver.Firefox(firefox_profile=fp)


mp3_converter = 'https://ytmp3.cc/en13/'
f = open('./song_urls', 'r')
for song_url in f:
    
    driver.get(mp3_converter)

    input_field = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'//form/input')))
    input_field.send_keys(song_url)

    submit_button = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,"//form/input[@id='submit']")))
    submit_button.click()

    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Download']"))).click()

    time.sleep(2)