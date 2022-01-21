<h1 align="center">IMAGE 2022</h1>

<h2 align="center">Stockie - Building a Stock Analysis Web App in Python</h2>


> Time Required: 3 hours    
> Instructor: Brian L. Chen  
> Venue: Online   

## Objective 

本教學主要目標為讓同學知道 Python 可以在短時間內如何做出一個類似 App 的工具。以目前最為流行的股票當作媒介，讓高中生也有機會將資訊與股票市場結合，藉由簡單的分析，給自己未來投資或是家人更多 insights 。

有鑒於教學時程短暫，本課僅能作為初步介紹用，如果要學習更多相關資源請見以下 [Resources](#Resources) 列表。

## Syllabus
| 章節  | 內容                                               |
| :---: | -------------------------------------------------- |
|   1   | 介紹 yfinance Package、Pandas 以及 Python 畫圖工具 |
|   2   | 介紹 Streamlit                                     |
|   3   | 實作                                               |
| Bonus | 網路爬蟲 / 抓取 Yahoo! Finance 資料                |

## Getting Onboard

```sh
pip install pipenv
pipenv shell
pip install -r requirements.txt
```

或可以在 Jupyter Lab 裡面執行：

```sh
!pip install -r requirements.txt
```

## Assignments

這次作業評分標準為三個階段的實作，分別為：

### Phase 01 - 能夠寫出可以正確跑出介紹詞句的網頁程式 (20%)

寫一個 `app.py`（注意：**不能是 Jupyter Notebook 的格式喔**）檔案，裡面要有簡單的網站介紹詞，舉例：

+ 自我介紹
+ 這個網站希望達到的目標、傳遞的資訊
+ 任何你想講的話都可以

### Phase 02 - 能夠將 Yahoo! Finance 資料正確顯示在網頁上 (50%)

1. 請任選一支股票作為分析的依據 (10%)
2. 將該支股票的資訊顯示在網頁上 (20%)
    + 股票代碼
    + 股票全名（英文）
    + 或其他你在看過 dictionary 後想呈現的資訊或項目
3. 爬取該支股票的歷年資料（任何時間範圍都可以），並將資料結果用 Python 畫出，顯示在網頁上 (20%)

### Phase 03 - 能夠提供網站閱讀者有幫助的資訊 (25%)

比如說，*投資報酬率*或是*「如果當初投入 XXX 元，中間都不賣出的話，現在會有 YYY 元」*等等。可能必須動腦想一下，需要執行什麼函式？

將「有用的」資訊呈現在 app 中。如果可以的話，希望你能夠把提供了什麼資訊以及為什麼提供也一起呈現在網頁上。

### Bonus - 使用者互動 (1%-20%)

這個部分上課沒有教，但網路上有非常多的資源，想考考看大家能不能有效的查詢想要的資訊，並實際運用（實際上寫程式時很常發生的例子）。以下提供幾個想法：


1. 用戶可能想要看到不同股票的資訊，但你的網站目前只能顯示一支股票
2. 用戶可能想要看當初投入的金額如果不同的話，現在的獲利會是多少
3. 用戶可能想要看到不同區間的股價

請自由發揮，並確保使用者知道怎麼使用（亦即，可能有些地方需要 `label` 或是詳細的說明）。


## Resources
+ 網路爬蟲 (Web Scraping) / Yahoo! Finance API
    + 程式語言-股票爬蟲：<https://medium.com/台股etf資料科學-程式類/程式語言-股票爬蟲-b502af0e3de7>
    + 超簡單台股每日爬蟲教學：<https://www.finlab.tw/超簡單台股每日爬蟲教學/>
+ Streamlit
    + 官方網站：<https://streamlit.io>
    + TSLA 股票分析 Demo：<https://stock-price-tsla.herokuapp.com>

