from urllib.request import urlopen
from bs4 import BeautifulSoup

count = 0
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class" : "green"})
for name in nameList:
    if (name.get_text() == "Anna Pavlovna"):
        newName = "sam minkin was here"
        count += 1
        print(newName)
    else:
        print(name.get_text())

print("Sam Minkin was here", count, "times")
