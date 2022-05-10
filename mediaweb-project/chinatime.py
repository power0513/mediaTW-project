#爬取中國時報國際新聞
import requests, bs4

url = 'https://www.chinatimes.com/world/?chdtv'
newshtml = requests.get(url)
objSoup=bs4.BeautifulSoup(newshtml.text, 'lxml')
itemobj = objSoup.find('section', 'article-list')
itemobj = itemobj.find('ul', 'verticle-list list-style-none')

items = itemobj.find_all('/div')
for item in items:
    txt = item.h1.text
    print(txt)