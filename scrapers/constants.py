import json

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "accept": "*/*",
    "accept-language": "en-US;q=0.7,en;q=0.6",
}
# https://www.w3schools.com/cssref/css_selectors.asp

# Wiki
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
wiki_selector = "#mp-itn > ul > li"

# Interez
interez_url = "https://www.interez.sk/spravy-zo-sveta/"
interez_selector = "#den > div > div > div.col-11.title > a"

# NDTV
ndtv_url = "https://www.ndtv.com/world-news"
ndtv_selector = "div.lisingNews > div.news_Itm > div.news_Itm-cont" # div.news_Itm-img > a

# Reuters
reuters_url = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1"
query = {
    "fetch_type": "collection",
    "orderby": "last_updated_date:desc",
    "section_id": "/breakingviews",
    "size": 15,
    "website": "reuters"
}
reuters_query = {
    "query": json.dumps(query)
    # "d": 53,
    # "_website": "reuters"
}