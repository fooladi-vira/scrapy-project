import requests
from bs4 import BeautifulSoup 
url='https://www.skysports.com/premier-league-table/2022'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find('table')
rows=table.find_all('tr')

for row in rows:
    data=[]
    for head in row.find_all('th'):
        data.append(head.text)
    for body in row.find_all('td'):
        data.append(body.text.replace('\n',''))
    print(data)