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
            try:
                title = art.find('div', class_='title').getText().strip()
                author = art.find('div', class_='author').getText()
                href = 'https://www.ptt.cc' + art.find('div', class_='title').a['href']
                article={
                    'title' : title,
                    'author' : author,
                    'link' : href
                }
                article_list.append(article)
                print(f' title: {title}\n author: {author}\n link: {href}')
                f.write(f' title: {title}\n author: {author}\n link: {href}'+'\n')
            except:
                print('Not Found')

with open('ptt-articles.json','w',encoding='utf-8') as f:
    json.dump(article_list, f, indent=2, sort_keys=True, ensure_ascii=False)