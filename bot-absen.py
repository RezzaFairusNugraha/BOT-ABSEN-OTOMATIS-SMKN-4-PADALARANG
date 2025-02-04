from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://lms.smkn4padalarang.sch.id/login/index.php")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("")
password.send_keys("")
password.send_keys(Keys.RETURN)

time.sleep(3)

driver.get("https://lms.smkn4padalarang.sch.id/mod/attendance/view.php?mode=0&id=990")

submit_button = driver.find_element(By.LINK_TEXT, "Submit attendance")
submit_button.click()

hadir_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='116']")
hadir_radio.click()

submit_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save changes']")
submit_btn.click()

time.sleep(3)
print("Berhasil Absen")
