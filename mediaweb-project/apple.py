#爬取蘋果日報焦點新聞標題
import requests, bs4
url='https://tw.appledaily.com/realtime/recommend/'
applehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(applehtml.text,'lxml')

times = objSoup.select('.timestamp')
news = objSoup.select('.headline')
counts = len(times)
for i in range(counts):
    print(f'{times[i].text}:{news[i].text}')

