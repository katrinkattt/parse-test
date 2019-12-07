import requests
from bs4 import BeautifulSoup

global str
str = str(map)

r = requests.get('https://www.avito.ru/tyumen/transport')
print(r.status_code)


if r.status_code == 200:
    print("it's ok")
elif r.status_code == 404:
    print('not found')


res = r.content
e = r.encoding = 'utf-8'
he = r.headers
# text_res = r.text        #NO WORK

print(res)
print(e)
print(he)

# print(text_res)


# soup = BeautifulSoup('https://www.avito.ru/tyumen/transport')
# s = soup.prettify()         #POCHTI WORK return tag:HTML, BODY, DIV

# soup = BeautifulSoup(res)         #POKA NE WORK TK LXML no supports

# https:api.github.com

# DA BLYAT' POCHEMU WORK TOL'KO S ETIM SAITOM-.-
# url = 'https://www.icc-ccs.org/index.php'

# page = requests.get(url)
# print(page.status_code)
# print(page.text)

# soup = BeautifulSoup(page.text, 'html.parser')

# print(soup.prettify())




