import requests
import bs4

URL = input()
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html')

infobox=soup.find_all(class_ = "infobox")

my_list = []


for x in infobox:
    my_list.append(str(infobox))

word = my_list[0]

n = word.find('Genre')

word = word[n:]
t = word.find('title')
word = word[t:]
k = word.find('>')
word = word[k+1:]
a = word.find('</a')
word = word[:a]


print(word)