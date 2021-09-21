start = """
<!DOCTYPE html>
<html>
    <body>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <div style="text-align:center;">
"""
end = """
                </div>
            </div>
        </div>
    </body>
</html>
"""
fill = """
<h1>{}</h1>
<p>{}</p>
"""


def create_message(articles):
    msg = start
    for article in articles:
        msg += fill.format(article["title"], article["body"])
    msg += end

    return msg
