import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response=requests.get(url)

html_content=response.text

soup=BeautifulSoup(html_content,"html.parser")

titles=soup.find_all("span",class_="titleline")

for index,title in enumerate(titles,start=1):
    article=title.get_text()
    print(index,article)