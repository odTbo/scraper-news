import json

start = """
<!DOCTYPE html>
<html>
    <body>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <div style="text-align:left;">
"""
end = """
                </div>
            </div>
        </div>
    </body>
</html>
"""
fill = """
<h1 style="font-size:180%;">{}</h1>
<p>{}</p>
"""


def create_message(articles):
    msg = start
    for article in articles:
        title = article["title"]
        try:
            body = article["body"]
        except KeyError:
            body = ""# json.dumps(article["links"])

        try:
            link = article["link"]
        except KeyError:
            pass
        else:
            body += "\n" + link

        msg += fill.format(title, body)
    msg += end

    return msg
