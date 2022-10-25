
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation


url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/?ref=shm"

headers = {
     "Accept": "*/*",
     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

req = requests.get(url, headers=headers)
src = req.text
print(src)
with open("index.html", "w") as file:
     file.write(src)
with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
# поиск всех ссылок

for link in soup.findAll('a'):
    print(link.get('href'))
print("Количество всех ссылок",len(soup.findAll('a')))
#поиск слов
find_all_clothes = soup.find_all(text=re.compile("( [Aa]lgorithm )"))
print("Количество слова 1",len(find_all_clothes))
find_all_clothes = soup.find_all(text=re.compile("([Qq]uiz )"))
print("Количество слова 2",len(find_all_clothes))
find_all_clothes = soup.find_all(text=re.compile("([Ll]oops )"))
print("Количество слова 3",len(find_all_clothes))



def loopit():
    NUM = 0
    for TAG in soup.find_all():
        if TAG.string is not None:
           NUM = NUM + len(TAG.string.split())

           # print(TAG.string.split())
    print("Общее количество слов в параграфах", NUM)

loopit()
# ##########
stop_list = [ "|", ":", "-", "/", ".", ",", "”", "▲", "“", "+", "Б", "]","!","–","<","&"]
word_count = Counter()
all_words = soup.get_text(" ", strip=True).lower().split()

#count words
for i in range(1,8):
    word_count.clear()
    for word in all_words:
       cln_word = word.strip('.,?')

       if len(cln_word) == i:

           if cln_word in stop_list:
              continue
           word_count[cln_word] += 1


    print("Количество слов из ",i,len(word_count.keys()))

#
# list=[1,2,3,4,5,6,7]
# list2=[20,44,98,152,167,144,151]