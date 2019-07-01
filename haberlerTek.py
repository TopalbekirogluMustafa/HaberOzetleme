from newspaper import Article
import random
import haberlerToplu
try:
    url = random.choice(haberlerToplu.list)
    haber = Article(url, language='tr')
    haber.download()
    haber.parse()
    haberLinki = haber.text
    print(haberLinki, "\n")

    while len(haberLinki) <= 700:
        url = random.choice(haberlerToplu.list)
        haber = Article(url, language='tr')
        haber.download()
        haber.parse()
        haberLinki = haber.text
        print(haberLinki, "\n")
except:
    hataLinki = open("hataLinki.txt", "r")
    hataLinki.write(url)
    hataLinki.write("\n")