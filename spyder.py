import os
import requests
import urllib
from bs4 import BeautifulSoup

url = 'http://www.360doc.com/content/18/0812/16/39567030_777704048.shtml'

image_dir = './mengke/'
if not os.path.exists(image_dir):
    os.mkdir(image_dir)

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
images = soup.select('img')
for image in images:
    print(image, type(image))
    src_url = image.attrs['src']
    tar_url = image_dir+src_url.split('/')[-1]+'.jpg'
    print(src_url)
    print(tar_url)
-
    urllib.request.urlretrieve(src_url,tar_url)
print('DONE')
