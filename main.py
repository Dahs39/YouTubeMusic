# Testing creating a script that plays music playlist
# Takes in one parameter to use for search
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\Python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://music.youtube.com")
actions = ActionChains(driver)

searchQuery = sys.argv[1]

driver.find_element(By.CSS_SELECTOR, "body > ytmusic-app:nth-child(6) > ytmusic-app-layout:nth-child(2) > ytmusic-nav-bar:nth-child(3) > div:nth-child(2) > ytmusic-search-box:nth-child(3) > div:nth-child(1) > div:nth-child(1) > tp-yt-paper-icon-button:nth-child(1) > tp-yt-iron-icon:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "body > ytmusic-app:nth-child(6) > ytmusic-app-layout:nth-child(2) > ytmusic-nav-bar:nth-child(3) > div:nth-child(2) > ytmusic-search-box:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)").send_keys(searchQuery)
driver.find_element(By.CSS_SELECTOR, "body > ytmusic-app:nth-child(6) > ytmusic-app-layout:nth-child(2) > ytmusic-nav-bar:nth-child(3) > div:nth-child(2) > ytmusic-search-box:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)").send_keys(Keys.ENTER)

try:
    playButton = driver.find_element(By.CSS_SELECTOR, "button[aria-label='PLAY ALL']")
    print("Is Play button available? " + str(playButton.is_displayed()))
    playButton.click()
except:
    print("Unable to click on the button.")

time.sleep(7)
# wait = WebDriverWait(driver, 7)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".ytp-ad-skip-button-container")))

# Checks if skip add button is available.  Ad sometimes is not skippable
try:
    skipAdBtn1 = driver.find_element(By.CSS_SELECTOR, ".ytp-ad-skip-button-container")
    print("Is Skip Ad button visible? " + str(skipAdBtn1.is_displayed()))
    skipAdBtn1.click()
except:
    print("No ad was skipped")
# skipAdBtn2 = driver.find_element(By.CSS_SELECTOR, ".ytp-ad-skip-button")
# print("Element is visible? " + str(skipAdBtn2.is_displayed()))
# skipAdBtn2.click()

nowPlaying = driver.find_element(By.CSS_SELECTOR, "yt-formatted-string[class='title style-scope ytmusic-player-bar']")
print("Now playing: " + nowPlaying.text)

# List to later output all the songs that were played
songsPlayedList = []
songsPlayedList.append(nowPlaying)