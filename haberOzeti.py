import haberlerTek
from gensim.summarization import summarize



text =haberlerTek.haberLinki

try:
    print('Özet: %20')
    yuzdeYirmi = summarize(text)
    print(yuzdeYirmi)

    print('\nÖzet: %50')
    print(summarize(text, ratio=0.5))

    print('\nÖzet: %35')
    print(summarize(text, ratio=0.35))

    print('\n50 Kelimelik Özet:')
    print(summarize(text, word_count=50))

    from gensim.summarization import keywords

    print('\nAnahtar Kelimeler:')
    print(keywords(text))
except:
    hataLinki = open("hataLinki.txt","r")
    hataLinki.write(haberlerTek.url)
    hataLinki.write("\n")
