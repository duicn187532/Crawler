import time
import Getrid
import Getdata
TAIId=[
    1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 19, 20, 21, 22, 24, 30, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
        49, 93, 94, 95, 96]#上市公司
TWOId=[
    97, 98, 121, 122, 123, 124, 125, 126, 130, 138, 139, 140, 141, 142, 145, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161,
         169, 170, 171]#上櫃公司
rid_value=None
price_set2=set()
def getCompanyPrice():
    start_time = time.time()
    for TAIIds in TAIId:
        for offset in range(0,120, 30):
            url1="https://tw.stock.yahoo.com/class-quote?sectorId="+str(TAIIds)+"&exchange=TAI"
            rid_value =Getrid.getrid(url1)
            nurl = ("https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TAI;"
                    "offset="+str(offset)+";sectorId="+str(TAIIds)+"?bkt=&device=desktop&ecma=modern&"
                    "feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid="+str(rid_value)+
                    "&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1979&returnMeta=true")            
            price_set2.update(Getdata.getPrice2(nurl))
    for TWOIds in TWOId:
        
        for offset in range(0,120,30):
            url2="https://tw.stock.yahoo.com/class-quote?sectorId="+str(TWOIds)+"&exchange=TWO"
            rid_value =Getrid.getrid(url2)
            nnurl=("https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TWO;"
                   "offset="+str(offset)+";sectorId="+str(TWOIds)+"?bkt=&device=desktop&ecma=modern&"
                   "feature=useNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid="+str(rid_value)+
                   "&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1979&returnMeta=true")
            price_set2.update(Getdata.getPrice2(nnurl))
    price_list = list(price_set2)
    sorted_price_list = sorted(price_list, key=lambda x: x.split()[0])
    with open("pricenow.txt","w",encoding="utf-8")as file:
        for i in sorted_price_list:
            file.write(str(i)+"\n")  

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")