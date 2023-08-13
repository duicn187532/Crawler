import urllib.request as req

def getPrice(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
    prices=root.find_all("span",class_=["Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)","Jc(fe) Fw(600) D(f) Ai(c)","Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-down)"])
    num=root.find_all("span",class_="Fz(14px) C(#979ba7) Ell")
    
    return titles,prices,num