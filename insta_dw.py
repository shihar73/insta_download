from selenium import webdriver
import pickle5 as pickle
from bs4 import BeautifulSoup
import requests
import urllib
import json

if __name__ == "__main__":
    import insta_log
    import download
else:
    from . import insta_log
    from . import download

class DownloadLink:

    def find_url(self):
        try:

            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            driver = webdriver.Chrome(options=options)
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})

            dw = download.insta_download()
            driver.get('https://www.instagram.com/')
            try:
                cookies = pickle.load(open("cookies.pkl", "rb"))
                for cookie in cookies:
                    driver.add_cookie(cookie)
            except:
                print("get cookies")
                log = insta_log.cookies()
                log.get_cookie()
                cookies = pickle.load(open("cookies.pkl", "rb"))
                for cookie in cookies:
                    driver.add_cookie(cookie)

            print(self.url)
            driver.get(self.url)
            print(driver.title)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            main_data = json.loads(soup.find("body").text)
            data = main_data['graphql']['shortcode_media']

            is_video = data['is_video']

            if is_video:
                dw_url = data['video_url']
                dw.dw_vid(dw_url, self.loc)
            else:
                dw_url = data['display_url']
                dw.dw_vid(dw_url, self.loc)
        except:
            print("Error: Didi't get download link")
            driver.quit()


    def get_link(self, url, loc):
        self.loc = loc
        if url[0:25] == "https://www.instagram.com":
            url_1 = urllib.parse.urlparse(url)
            if len(url_1.path) >= 30:
                print("Error: This is a privet account")
            else:
                url = "https://www.instagram.com"+url_1.path+"?__a=1"
                self.url = url
        else:
            print('Error: Check url')
            exit()

        self.find_url()


def main():
    loc =str(input("Enter location (Default : /root/Downloads/): "))
    url = str(input("Enter url : "))
    download = DownloadLink()
    download.get_link(url, loc)


if __name__ == "__main__":
    main()
