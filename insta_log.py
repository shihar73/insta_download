from selenium import webdriver
import pickle5 as pickle
import time

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(10)

name = driver.find_elements_by_name("username")
name[0].send_keys("nisna905")
password = driver.find_elements_by_name("password")
password[0].send_keys("sls306ss")
driver.find_element_by_css_selector('button.y3zKF').click()

cookies = driver.get_cookies()
pickle.dump(cookies, open("cookies.pkl", "wb"))

driver.quit()
