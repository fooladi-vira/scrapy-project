import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.select('.jsx-2514672dc9197d80')
#print(products)
name_product=[]
price_product=[]
for product in products:
    name = product.select_one('.product-name')
    price = product.select_one('.product-price-text')
    if name or price:
        print(f' product : {name.text}')
        name_product.append(name.text.strip())
        print(f'price : {price.text} ')
        price_product.append(price.text.strip())
        print('------------------')

products={'Name':name_product,'Price':price_product}
data=pandas.DataFrame(products)
writer=pandas.ExcelWriter('product.xlsx')
data.to_excel(writer, sheet_name='Sheet1', index=False)
writer._save()

