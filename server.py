import os
import requests
import sys


def get():
    url = input("[*] input url\n")

    r = requests.get(url)
    if r == r.raise_for_status():
        print ("Error: file not found\n")

    path = input("[*] input the location where you want to save the file\n")
    os.chdir(path)

    name = input("[*] input name of file to save the web file\n")
    open(name, 'wb').write(r.content)



 

