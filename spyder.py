import os
import requests
import urllib
from bs4 import BeautifulSoup

url = 'http://www.sohu.com/a/314432722_559488?scm=1019.e000a.v1.all&spm=smpc.csrpage.news-list.2.1560319936429k7bcgdz'

image_dir = './lusuo/'
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
