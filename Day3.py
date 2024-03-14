import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {
    'over18': '1'
}
article_list = []

with open('ptt-articles.txt','w',encoding='utf-8') as f:
    for i in range(3):
        resp = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(resp.text, 'html.parser')
        arts = soup.select('div.r-ent')
        u=soup.select('div.btn-group.btn-group-paging a')
        print('本頁的url為' + url)
        url='https://www.ptt.cc' + u[1]['href']
        for art in arts:
            titl = art.find('div', class_='title').getText().strip()
            auth = art.find('div', class_='author').getText()
            link = 'https://www.ptt.cc' + art.find('div', class_='title').a['href']
            article={
                'title' : titl,
                'author' : auth,
                'link' : link
            }
            article_list.append(article)
            print(f' title: {titl}\n author: {auth}\n link: {link}')
            f.write(f' title: {titl}\n author: {auth}\n link: {link}'+'\n')

with open('ptt-articles.json','w',encoding='utf-8') as f:
    json.dump(article_list, f, indent=2, sort_keys=True, ensure_ascii=False)