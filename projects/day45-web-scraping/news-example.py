from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []


for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

article_upvotes = []
subtexts = soup.find_all(name="td", class_="subtext")
for subtext in subtexts:
    if subtext.find(name="span", class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

max_index = article_upvotes.index(max(article_upvotes))

print(articles[max_index])