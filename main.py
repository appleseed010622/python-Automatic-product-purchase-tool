from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
# import mysql.connector
from csv import writer


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#open url in google browser
driver.get("https://www.2ndstreet.jp/user/login")

#enter geo_id in field
userID = driver.find_element(By.ID, "authId")
userID.send_keys("unificationtheory@vivaldi.net")

#enter password in field
userPASS = driver.find_element(By.NAME, "password")
userPASS.send_keys("abcde0123")