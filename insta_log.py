import os
from selenium import webdriver
import pickle5 as pickle
from os.path import join, dirname
from dotenv import load_dotenv


class cookies:
    try:
        def get_cookie(self):

            dotenv_path = join(dirname(__file__), '.env')
            load_dotenv(dotenv_path)

            user_name = os.environ.get("INSTA_USER_NAME")
            insta_pass = os.environ.get("INSTA_PASS")

            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0")

            driver = webdriver.Chrome(options=options)

            try:
                 driver.get('https://www.instagram.com/accounts/login/')
            except:
                driver.quit()

            driver.implicitly_wait(10)

            try:
                name = driver.find_elements_by_name("username")
                name[0].send_keys(user_name)
                password =  driver.find_elements_by_name("password")
                password[0].send_keys(insta_pass)
                driver.find_element_by_css_selector('button.y3zKF').click()
            except:
                print("Erorr")
                driver.quit()

            cookies = driver.get_cookies()
            pickle.dump(cookies, open("cookies.pkl", "wb"))
            driver.quit()
    except:
        print("Erorr: Login failed")


def main():
    cookie = cookies()
    cookie.get_cookie()


if __name__ == "__main__":
    main()