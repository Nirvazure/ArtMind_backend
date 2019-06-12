import os
import requests
import urllib
from bs4 import BeautifulSoup

url = 'https://www.sohu.com/a/221728304_541698'

image_dir = './leinuoa/'
if not os.path.exists(image_dir):
    os.mkdir(image_dir)

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
images = soup.select('img')
for image in images:
    print(image, type(image))
    src_url = image.attrs['src']
    tar_url=image_dir+src_url.split('/')[-1]+'.jpg'
    print(src_url)
    print(tar_url)
    urllib.request.urlretrieve(src_url,tar_url)
print('DONE')
