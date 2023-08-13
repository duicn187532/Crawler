import urllib.request as req
import getprice
import time

title_list=[]
nextlink_list=[]
price_set=set()
titles=None
prices=None
num=None

def getClass(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="Ta(s) W(20%)")

    for title in titles:
        if title.a !=None:
        #print(title.a.string)
            title_list.append(title.a.string)
            #file.write(title.a.string+"\n")
            #print(title_list)
    nextlinks=root.find_all("a",string=title_list)
    for nextlink in nextlinks:
        #print(nextlink)
        nextlink_list.append("https://tw.stock.yahoo.com"+nextlink["href"])
        #print(nextlink_set)

    return

def stockChase():
    pageURL="https://tw.stock.yahoo.com/class/"
    getClass(pageURL)
    start_time = time.time()
    for i in nextlink_list:
        titles,prices,num=getprice.getPrice(i)
        for num,price,title in zip(num,prices,titles):
            price_set.add(num.string+" "+title.string+" 現價:"+price.string)
    with open("pricenow.txt", "w", encoding="utf-8") as file:
        pass
    with open("pricenow.txt","a",encoding="utf-8")as file:
        for i in price_set:
            file.write(str(i)+"\n")  

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
stockChase()