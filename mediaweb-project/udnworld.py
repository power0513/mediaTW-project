#聯合報全球頭條新聞
import requests, bs4
url='https://udn.com/news/cate/2/7225' #全球頭條
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')
items = objSoup.find('div', 'context-box__content')

news = items.find_all('a')
for new in news:
    print(new.text)

