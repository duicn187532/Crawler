import urllib.request as req
price_set2=set()
def getPrice2(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    import json
    Idata=json.loads(data)
    Rdatas=Idata.get("data",[]).get("list", [])
    if not Rdatas:
        return set()
    for key in Rdatas:
        symbol = key.get("symbol", "N/A")
        symbolName = key.get("symbolName", "N/A")
        price = key.get("price", "-")
        price_set2.add(symbol + " " + symbolName + " 現價:" + str(price))
    return price_set2