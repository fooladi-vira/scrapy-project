import requests
from bs4 import BeautifulSoup
import pandas
import re
url = 'https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
data=soup.find_all(['a'])
# data=soup.find_all(re.compile('^a|div'))
# data=soup.find_all('div', class='name...')
# data=soup.find_all('div',re.compile('(^name class)'))

for d in data:
    print(d.text)

# pattern = r'<div[^>]*>(?:(?!<\/?div[^>]*>).)*<\/div>'

html = response.text
pattern = r'<img\s+.*?src=(["\'])(.*?)\1'
matches = re.findall(pattern, html)
print(matches)