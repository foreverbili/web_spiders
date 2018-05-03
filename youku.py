# -*- coding:utf8 -*-
import requests
from lxml import etree
url = 'http://www.soku.com/search_video/q_butterfly++%E6%8C%87%E5%BC%B9_orderby_1_limitdate_0?spm=a2h0k.8191407.0.0&site=14&page=1'
cook = dict(cna='z74IEucOcncCAXPI6pOnv3cN',
            cnaui='865763163',
            cdpid='W89JWGOPSPkU',
            aui='865763163',
            sca='2aa12d41',
            atpsida='325cf1b2210639bb00f4bed2_1520410748_3')
h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
for i in range(2):
    r = requests.get(url,cookies = cook,headers = h)
    tree = etree.HTML(r.text)
    result = tree.xpath('//div/div[@class="v-link"]/a/@href')
    print(result)
    for a in result:
        print ('http:'+a)
        print ('=====================')
    next = tree.xpath('//div//li[@class="current"]/span/text()')
    nextpage = int(next[0])+1
    url = 'http://www.soku.com/search_video/q_butterfly++%%E6%%8C%%87%%E5%%BC%%B9_orderby_1_limitdate_0?spm=a2h0k.8191407.0.0&site=14&page=%d' % nextpage







