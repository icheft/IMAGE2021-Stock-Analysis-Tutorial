# 初搞

| 章節  | 內容                                |
| :---: | ----------------------------------- |
|   1   | 網路爬蟲 / 抓取 Yahoo! Finance 資料 |
|   2   | 介紹 Python 畫圖工具                |
|   3   | 介紹 Streamlit                      |
|   4   | 實作                                |

## 網路爬蟲 / 抓取 Yahoo! Finance 資料
先來介紹一下網路爬蟲是什麼。網路爬蟲（Web Scraping）為一種透過 Python 程式碼抓取網頁上資料的一種方式。通常會用到一些其他 Python 的 Libraries，比如說 `Beautiful Soup`。

最後我們會使用 Yahoo! Finance 上面的資料作為例子。（怕這部分講太久，就變成只能講到爬蟲）

```py
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def parsePrice():
    url = 'https://finance.yahoo.com/quote/0050.TW?p=0050.TW&.tsrc=fin-srch'
    page = urlopen(url)
    soup = bs4.BeautifulSoup(page, 'html.parser')
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

while True:
    print('目前成交價格為：'+str(parsePrice()))
```

今天，我們也會介紹一個很方便的爬蟲工具——可以讓我們快速抓取 Yahoo! Finance 上面所存放的資料。

```py
import yfinance as yf
import pandas as pd

symbol = '0050.TW'
stock_obj = yf.Ticker(symbol)
stock_df = stock_obj.history(start='2011-3-12', end='2021-3-12')
```
此時我們將一個像是 Excel 資料的東西存放到名為`stock_df`的變數裡面。此變數型別為一種叫做`DataFrame`的型別，以後如果要接觸大量資料時也會很常用到。
## 介紹 Python 畫圖工具                
## 介紹 Streamlit                      
## 實作