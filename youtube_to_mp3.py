
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time

import sys

if __name__ == '__main__':

	autor = sys.argv[1]

	options = Options()
	options.headless = True

	fp = webdriver.FirefoxProfile()
	fp.set_preference('browser.download.folderList',2)
	fp.set_preference("browser.download.manager.showWhenStarting", False)
	fp.set_preference("browser.download.dir", f'/home/upflo/Music/{autor}')
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mpeg")
	fp.set_preference("browser.download.useDownloadDir", True);
	fp.set_preference("pdfjs.disabled",True)

	driver = webdriver.Firefox(firefox_profile=fp)

	f = open('songs')
	songs = f.readlines()


	for idx, song in enumerate(songs):
		print(f'{idx + 1}.Downloading song: {song}...')
		url = 'https://www.youtube.com/'
		driver.get(url)
		
		#youtube part
		search_form = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'//form[@id="search-form"]')))
		input_field = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'//form/div/div/input')))
		input_field.send_keys(autor + ' ' + song)
		search_form.submit()
		time.sleep(2)
		song_link = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'//div/div/h3/a')))
		link = song_link.get_attribute('href')

		#converter
		mp3_converter = 'https://ytmp3.cc/en13/'
		driver.get(mp3_converter)
		
		input_field = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,'//form/input')))
		input_field.send_keys(link)

		submit_button = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,"//form/input[@id='submit']")))
		submit_button.click()

		WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Download']"))).click()

		time.sleep(2)

	time.sleep(20)
	driver.close()

