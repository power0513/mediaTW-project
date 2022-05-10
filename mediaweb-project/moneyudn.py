#抓取經濟日報產業新聞+加上headers 
import requests, bs4
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
url='https://money.udn.com/money/cate/5591?from=edn_ham' #經濟日報

newshtml = requests.get(url, headers=headers)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')
itemobj = objSoup.find('div', 'story__title')

items = itemobj.find_all('div', 'story-headline')
for item in items:
   txt = item.a.text.strip()
   print(txt)
