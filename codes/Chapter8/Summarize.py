# 8장 고급 NLP 레시피 - 텍스트 요약
from gensim.summarization import summarize
from bs4 import BeautifulSoup
import requests

# 예제에 주어진 url 사이트가 현재 존재하지 않음
urls = {
    'Daff: Unproven Unification of Suffix Trees and Redundancy':
    'http://scigen.csail.mit.edu/scicache/610/scimakelatex.21945.none.html',
    'CausticIslet: Exploration of Rasterization':
    'http://scigen.csail.mit.edu/scicache/790/scimakelatex.1499.none.html'
}

for key in urls.keys():
    url = urls[key]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.get_text()
    pos1 = data.find("1 Introduction") + len("1 Introduction")
    pos2 = data.find("2 Related Work")
    text = data[pos1:pos2].strip()
    print("PAPER URL: {}".format(url))
    print("TITLE: {}".format(key))
    print("GENERATED SUMMARY: {}".format(summarize(text)))
    print()
