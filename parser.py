import requests
from bs4 import BeautifulSoup

from link_list import link_list

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.939 YaBrowser/24.1.1.939 (beta) Yowser/2.5 Safari/537.36",
    }

with open('headers.txt', 'a', encoding='utf-8') as f:
    for link in link_list:
        res = se.get(link).text
        soup = BeautifulSoup(res, 'lxml')
        text = soup.find_all('h1', {'class': 'tn-atom'})

        text = str(text[0]).replace(
            '<br/>', ' '
        ).replace(
            '</h1>', ''
        ).split('>')[1].replace(
            '\xa0', ' '
        ).replace(
            '\u200e', ''
        )

        f.write(f'{text}\n')

