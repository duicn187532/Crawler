import urllib.request as req
import re
import bs4
def getrid(url1):
    request = req.Request(url1, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    script_tag = root.find("script", string=re.compile("window.YAHOO.context ="))

    script_content = script_tag.string
    rid_match = re.search(r'"rid":\s*"([^"]+)"', script_content)
    rid_value = rid_match.group(1)
    return rid_value