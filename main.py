from requests_html import HTMLSession
import smtplib
import os

from_email = os.environ.get("FROM_EMAIL")
to_email = os.environ.get("TO_EMAIL")
e_pass = os.environ.get("PASSWORD")

url = "https://en.wikipedia.org/wiki/Main_Page"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US;q=0.7,en;q=0.6",
}

s = HTMLSession()

css_selector = "#mp-itn > ul > li"

# FETCH WIKI PAGE
r = s.get(url=url, headers=headers)
item_list = r.html.find(css_selector)

# GET ARTICLES
articles = []
for item in item_list:
    title = item.text
    links = [f'https://en.wikipedia.org{a.attrs["href"]}\n' for a in item.find("a")]
    article = {
        "title": title,
        "links": links
    }
    articles.append(article)

# CREATE EMAIL CONTENT/BODY
mail_body = ""
for a in articles:
    mail_body += f'\n{a["title"]}\n'
    for link in a["links"]:
        mail_body += link

# SEND EMAIL
with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    connection.login(user=email, password=e_pass)
    connection.sendmail(
        from_addr=email,
        to_addrs=,
        msg=f"Subject:Happy Birthday!\n\n{letter}"
    )
