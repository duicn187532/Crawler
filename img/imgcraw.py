import requests as req
from bs4 import BeautifulSoup as bs

url="https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/091/10/0010911014.jpg&v=61b0893ak&w=348&h=348"
result=req.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})

with open('books6.jpg',mode='wb') as file:
    file.write(result.content)