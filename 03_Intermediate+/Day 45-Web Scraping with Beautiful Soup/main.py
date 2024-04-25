from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select(".title a")

articles_texts = []
articles_links = []
for article in articles:
    articles_texts.append(article.text)
    articles_links.append(article.get("href"))

article_upvotes = [int(score.text.split()[0]) for score in soup.select(".subline .score")]

# print(articles_texts)
# print(articles_links)
# print(article_upvotes)

high = 0
index = 1
for i in range(len(article_upvotes) - 1):
    vote = article_upvotes[i]
    if vote > high:
        high = vote
        index = i

print(articles_texts[index])
print(articles_links[index])
print(article_upvotes[index])

# with open("website.html", encoding="utf8") as webpage:
#     html = webpage.read()

# soup = BeautifulSoup(html, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)

# anchor = soup.find_all(name="a")
# for tag in anchor:
# print(tag.getText())
# print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# heading_section = soup.find(name="h3", class_="heading")

# print(heading)
#e print(heading_section.getText())

# company_url = soup.select_one("p a") # name -> select id
# print(company_url)

# heading_select = soup.select(".heading")
# print(heading_select)
