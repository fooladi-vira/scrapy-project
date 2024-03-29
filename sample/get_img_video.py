import requests
from bs4 import BeautifulSoup
import re
import random

def download_video(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links=soup.find_all('link',href=re.compile('.mp4'))
    print(len(links))
    for info in links:
        link=info.get('href')
        with requests.get(link,stream=True) as r:
            with open ('video.mp4','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)
                    
                    
 #download with different quality
def download_video_q(url,q):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links=soup.find_all('a',href=re.compile(f'{q}p'+'\.mp4$'))
    for info in links:
        link=info.get('href')
        with requests.get(link,stream=True) as r:
            with open ('video.mp4','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)
 
 
 
def download_img(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links=soup.find_all('img',src=re.compile('.jpg'))
    for info in links:
        link=info.get('src')
        name=random.randrange(1,1000)
        with requests.get(link,stream=True) as r:
            with open (str(name)+'.jpg','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)


def download_video_youtub(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links=soup.find_all('a',id='video-title-link')
    print(links)
    for info in links:
        link=info.get('href')
        with requests.get(link,stream=True) as r:
            with open ('video.mp4','wb') as file:
                for pack in r.iter_content(chunk_size=1024):
                    file.write(pack)
 
    
# url='https://video.varzesh3.com/video/304788/'
# download_video(url)
url2='https://torob.com/browse/99/'
url_v='https://youtu.be/qMMRnY1Ba0s'
download_video_youtub(url_v)
# download_video(url_v)
#download_img(url2)
print('done')