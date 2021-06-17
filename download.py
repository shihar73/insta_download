import requests
import urllib
from urllib.parse import urlparse


class insta_download:
    # This is download videos and images use source url
    def dw_vid(self, url, root):
        try:
            name = urlparse(url).path[-25:]
            resource = urllib.request.urlopen(url)

            if root:
                f_name = root + name
            else:
                f_name = "/root/Downloads/" + name

            output = open(f_name, "wb")
            output.write(resource.read())
            output.close
            print(f_name, 'download success')
        except:
            print("Error: Download Failed check url or location")


def main():
    dw = insta_download()
    loc = str(input("Enter location (Default : /root/Downloads/): "))
    url_a = str(input("Enter url : "))
    dw.dw_vid(url_a, loc)


if __name__ == '__main__':
    main()
