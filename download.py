import requests
import urllib
from urllib.parse import urlparse


def dw_vid(url):
    name = urlparse(url).path[-25:]
    resource = urllib.request.urlopen(url)
    f_name = "/root/Downloads/f/"+name
    output = open(f_name, "wb")
    output.write(resource.read())
    output.close
    print("video : ", f_name, 'download success')


url_a = str(input("Enter url : "))
dw_vid(url_a)


