from requests_html import HTMLSession
from dotenv import load_dotenv
from datetime import datetime
import smtplib
import os

load_dotenv()

from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")
e_pass = os.getenv("PASSWORD")

today = datetime.now()
today = today.strftime("%d/%m/%Y")

url = "https://en.wikipedia.org/wiki/Main_Page"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US;q=0.7,en;q=0.6",
}

s = HTMLSession()

css_selector = "#mp-itn > ul > li"

print("Fetching wiki page...")
# FETCH WIKI PAGE
r = s.get(url=url, headers=headers)
item_list = r.html.find(css_selector)

# GET ARTICLES
print("Compiling articles...")
articles = []
for item in item_list:
    title = item.text
    links = [f'https://en.wikipedia.org{a.attrs["href"]}\n' for a in item.find("a")]
    article = {
        "title": title,
        "links": links
    }
    articles.append(article)
print(f"Number of articles: {len(article)}")

# CREATE EMAIL CONTENT
print("Creating email...")
mail_body = f"Subject: Wiki News {today}\n\n"
for a in articles:
    mail_body += f'\n{a["title"]}\n'
    for link in a["links"]:
        mail_body += link

# SEND EMAIL
print("Sending...")
with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    connection.login(user=from_email, password=e_pass)
    connection.sendmail(
        from_addr=from_email,
        to_addrs=to_email,
        msg=mail_body
    )
print("Done.")
