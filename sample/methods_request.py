import requests
url='https://www.python.org/'
response=requests.get(url)
print(response)
print('*********************')
print(response.status_code)
print('*********************')
print(response.reason)
print('*********************')
print(response.request)
print('*********************')
print(response.request.headers)
print('*********************')
# print(response.content)
# print('*********************')

# print(response.text)
# print('*********************')
print(response.headers)

print('******************************************')

url_pic='https://www.python.org/static/img/python-logo@2x.png'
with open('1.png','wb') as file:
    file.write(response.content)
