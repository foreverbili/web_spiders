import requests
import threading
import urllib.request
from bs4 import BeautifulSoup

h = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
      'referer': 'https://stevenlawguitar.com/2015/03/19/%e9%9b%b6%e4%b9%8b%e4%bd%bf%e9%ad%94-i-say-yes-wedding-version-zero-no-tsukaima/'

}

gtped = []
nexgtp = ['https://stevenlawguitar.com/2014/10/26/only-my-railgun-%e7%a7%91%e5%ad%a6%e3%81%ae%e8%b6%85%e9%9b%bb%e7%a3%81%e7%a0%b2/']
a = ''

def download(soup):
    try:
        response = soup.find_all('p')
        for i in response:
            res = i.find_all('a', target="_blank")
            if res:
                data = res[0].get('href')
                name = data.split('/')[-1]
                pdf = data.split('.')[-1]
                if data not in gtped and pdf == 'pdf':
                    try:
                        urllib.request.urlretrieve(data, 'downloads/' + name)
                        gtped.append(data)
                    except:
                        print(name, 'failed')
    except:
        print(nexgtp)

def spider(url):
    global gtped  , gtping , a
    times = 0
    while times <= 3:
        try:
            a += (url+'/n')
            req = requests.get(url,headers=h, timeout=15)
            html = req.text
            soup = BeautifulSoup(html,'lxml')
            return soup
        except requests.exceptions.RequestException as e:
            print(url ,'  error')
            times+=3
def next(next_url):
    soup = spider(next_url)
    download(soup)
    nextpage = soup.find('a', rel="next").get('href')
    nexgtp.append(nextpage)

while len(nexgtp)>0 :
    nex = nexgtp.pop()
    next(nex)
    down = spider(nex)
    t = threading.Thread(target=download,args=(down,))
    t.start()
    print (nex)












