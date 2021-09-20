from constants import *

from requests_html import HTMLSession

session = HTMLSession()


def get_body(link):
    # Article page text
    r = session.get(link, headers=headers)
    article_page = r.html.find("#clanok", first=True)
    article_text = "".join([item.text for item in article_page.find("p")])

    return article_text

print("Fetching Interez...")
r = session.get(url=interez_url, headers=headers)
item_list = r.html.find(interez_css)


articles = []
# GET ARTICLES
print("Compiling articles...")
for item in item_list:
    title = item.text
    link = item.attrs["href"]
    body = get_body(link)
    article = {
        "title": title,
        "body": body
    }
    articles.append(article)

print(f"Number of articles: {len(articles)}")

# articles: [{"title": "title_text", "body": "body_text"}, ...]
# for article in articles:
#     print(article)



