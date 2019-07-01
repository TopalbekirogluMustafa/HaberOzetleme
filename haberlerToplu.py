from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

try:
    news_url = "http://www.milliyet.com.tr/rss/rssNew/dunyaRss.xml"
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")

    list = []
    for news in news_list:
        list.append(news.link.text)


except:
    print("HATA VERDİ HABERLER TOPLU")