import os
from selenium import webdriver
import pickle5 as pickle
from os.path import join, dirname
from dotenv import load_dotenv
import time


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

user_name = os.environ.get("INSTA_USER_NAME")
insta_pass = os.environ.get("INSTA_PASS")
print(type(user_name),type(insta_pass))

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(10)

name = driver.find_elements_by_name("username")
name[0].send_keys(user_name)
password = driver.find_elements_by_name("password")
password[0].send_keys(insta_pass)
driver.find_element_by_css_selector('button.y3zKF').click()

cookies = driver.get_cookies()
pickle.dump(cookies, open("cookies.pkl", "wb"))

driver.quit()
