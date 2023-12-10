from bs4 import BeautifulSoup as bs
import requests as req
import time
import pandas as pd
data={}#創建一個空字典
#定義爬蟲函式
def Getview(url):
    try:
        res=req.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"})
        print("成功")
    except:#失敗則回傳訊息
        print("臭蟲")
    soup=bs(res.text,"html.parser")#bs讀取網站
    viewa_tag=soup.find_all("div",class_="theme-img-block")#找到影片資訊標籤
    namep_tag=soup.find_all("p",class_="theme-name")#找到影片名稱標籤
    for (all_viewa,all_name) in zip(viewa_tag,namep_tag):
        viewp_tag=all_viewa.find("p")#在影片資訊中找到觀看次數字串
        data[all_name.string]=viewp_tag.string#定義字典內容並寫入
    return data#回傳
#迴圈進行爬蟲
for count in range(1,58):
    result=Getview("https://ani.gamer.com.tw/animeList.php?page="+str(count))
    time.sleep(1)#避免被鎖IP
# 創建 DataFrame
df = pd.DataFrame(list(result.items()), columns=['Name', 'View'])
# 寫入 Excel
df.to_excel('result.xlsx', index=False)