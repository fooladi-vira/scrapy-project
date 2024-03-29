import requests
from bs4 import BeautifulSoup 
url='https://www.python.org/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
# link=soup.find('a')
# print(link)

# links=soup.findAll('a')
# for l in links:
#     print(l['href'])

# link_select=soup.select_one('p')
# print(link_select)
link_all_select=soup.select('button')

# for l in link_all_select:
#     print(l)
# link_all_select=soup.select('button.search-button')
# for l in link_all_select:
#     print(l.text)
#     print(l.text.strip())
    
link_f=soup.select('button#submit')   
print(link_f)
link=soup.find('button',{'id':'submit'})
print(link.text)