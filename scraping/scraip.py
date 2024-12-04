from bs4 import BeautifulSoup
import urllib.request as req

#url = "https://beauty.hotpepper.jp/"
url = "http://tokidoki-web.com"

html = req.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

menu_block = soup.select("#sideCatBox > ul")

titles = []
for ul_tag in menu_block:
    for li_tag in ul_tag.find_all('li'):
        a_tag = li_tag.find('a')
        titles.append(a_tag.string)

print(titles)