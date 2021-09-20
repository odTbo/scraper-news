from constants import *

from requests_html import HTMLSession

session = HTMLSession()

print("Fetching Interez...")
r = session.get(url=interez_url, headers=headers)
item_list = r.html.find(interez_css)


articles = []
# GET ARTICLES
print("Compiling articles...")
for item in item_list:
    title = item.text
    link = [item.attrs["href"]]
    article = {
        "title": title,
        "links": link
    }
    articles.append(article)
print(f"Number of articles: {len(articles)}")
print(articles)