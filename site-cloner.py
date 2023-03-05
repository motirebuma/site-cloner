import wget
import urllib.request
import os
from banner import banner

banner.banner()
name = input("Enter target name: ")
url = input("Enter target url: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'timeout': 5,
    'tries': 5,
    }
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)


directory = f'{name}'
if not os.path.exists(directory):
    os.makedirs(directory)

path = f'{name}/' + f'{name}.html'
wget.download(response.geturl(), out=path)
