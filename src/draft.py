import streamlit as st
import io
import yfinance as yf
import pandas as pd


def mini_app():
    st.markdown(
        """### Stockie - 股票查詢小工具

嗨，我是 Brian。在這個簡單的小工具中，你可以達成以下事項：

1. 查詢股票目前的股價
2. 查詢股票的成交量
3. 查詢股票的資訊
4. 查詢股票特定時間區間下來的報酬率


"""
    )

    st.write("\n")

    symbol = st.text_input("輸入欲查詢的股票", "AAPL")
    st.markdown("""> 💯 像是這種，提供給使用者選擇股票的選項，可以幫你加 1%~20% 的分數～""")
    stock_obj = yf.Ticker(symbol)

    st.write(f"#### 分析 {symbol} ({stock_obj.info['longName']})")
    period = st.selectbox(
        "選擇時間區間", ["5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=4
    )  # 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    st.markdown("""> 💯 或者是像這種，給使用者彈性選擇時間區間，也可以加上分數～""")
    stock_df = stock_obj.history(period=period, auto_adjust=False)  # period="max"
    try:
        st.markdown(f'##### 最新成交價格：**{stock_obj.info["regularMarketPrice"]}**')
    except:
        st.markdown(
            f"##### 最新成交價格：**{stock_obj.history(period='1d', interval='1m', auto_adjust=False).sort_index(ascending=False).head(1).iloc[0, 0]}**"
        )

    st.markdown(f"##### 市場走勢圖")
    st.line_chart(stock_df.Close)
    st.markdown(f"##### 月成交量")
    st.bar_chart(stock_df.resample("MS").sum().Volume)

    p_1_year_ago = stock_df["Adj Close"][0]
    p_now = stock_df["Adj Close"][-1]
    return_rate = (p_now - p_1_year_ago) / p_1_year_ago
    # daily_returns = stock_df["Adj Close"].pct_change()
    # cum_returns = (daily_returns + 1).cumprod()
    # return_rate2 = (cum_returns[-1] - 1) / 1

    st.markdown(
        f"從 {stock_df['Adj Close'].index[0].strftime('%Y 年 %m 月 %d 日')} 到 {stock_df['Adj Close'].index[-1].strftime('%Y 年 %m 月 %d 日')}，{symbol} 的累積報酬率為 {round(return_rate * 100, 2)}%。"
    )


def main():
    # Render the readme as markdown using st.markdown.
    readme_file = io.open("draft.md", mode="r", encoding="utf-8")
    readme_text = st.markdown(readme_file.read())

    st.markdown(
        """
## Phase 01 - 能夠寫出可以正確跑出介紹詞句的網頁程式 (20%)

寫一個 `app.py`（注意：**不能是 Jupyter Notebook 的格式喔**）檔案，裡面要有簡單的網站介紹詞，舉例：

+ 自我介紹
+ 這個網站希望達到的目標、傳遞的資訊
+ 任何你想講的話都可以

所以，只要你的網頁可以達成下面事項即可獲得 20% 的分數 👇🏾
"""
    )

    p01 = st.expander("Phase 01 範例 (20%)", True)
    with p01:
        st.markdown(
            """### Stockie - 股票查詢小工具

嗨，我是 Brian。在這個簡單的小工具中，你可以達成以下事項：

1. 查詢股票目前的股價
2. 查詢股票的成交量
3. 查詢股票的資訊
4. 查詢股票一年下來的報酬率
"""
        )
        st.markdown(
            """> 💯 這邊只要你有簡單的用 `st.markdown` 或是 `st.write` 成功的在網頁上呈現東西，就可以得到 20% 的分數！"""
        )

    st.markdown(
        """
## Phase 02 - 能夠將 Yahoo! Finance 資料正確顯示在網頁上 (35%)

1. 請任選一支股票作為分析的依據 (10%)
2. 將該支股票的資訊顯示在網頁上 (10%)
    + 股票代碼 (5%)
    + 股票全名（英文）(5%)
    + 或其他你在看過 dictionary 後想呈現的資訊或項目
3. 爬取該支股票的歷年資料（任何時間範圍都可以），並將資料結果用 Python 畫出，顯示在網頁上 (15%)

範例如下 👇🏾

"""
    )

    p02 = st.expander("Phase 02 範例 (35%)", True)
    with p02:
        symbol = "AAPL"
        stock_obj = yf.Ticker(symbol)

        st.write(f"#### 分析 {symbol} ({stock_obj.info['longName']})")
        st.markdown(
            """> 💯 這邊只要你有說明你分析的股票，就可以得到 10%（選定一支股票）+ 5%（股票代碼）+ 5%（股票全名） (= 20%) 的分數！"""
        )
        stock_df = stock_obj.history(period="1y", auto_adjust=False)  # period="max"
        st.markdown(f'##### 最新成交價格：**{stock_obj.info["regularMarketPrice"]}**')

        st.markdown(f"##### 市場走勢圖")
        st.line_chart(stock_df.Close)
        st.markdown(f"##### 月成交量")
        st.bar_chart(stock_df.resample("MS").sum().Volume)

        st.markdown(
            """> 💯 這邊只要你有將 Yahoo! Finance 上面的資訊，用圖表的方式**正確**畫出，就可以得到 15% 的分數！"""
        )

    st.markdown(
        """

## Phase 03 - 能夠提供網站閱讀者有幫助的資訊 (25%)

比如說，*累積報酬率*或是*「如果當初投入 XXX 元，中間都不賣出的話，現在會有 YYY 元」*等等。可能必須動腦想一下，需要執行什麼函式？

將「有用的」資訊呈現在 app 中。如果可以的話，希望你能夠把提供了什麼資訊以及為什麼提供也一起呈現在網頁上。

*累積報酬率（或廣義的投資報酬率）的範例如下*：
"""
    )

    p03 = st.expander("Phase 03 範例 (25%)", True)
    with p03:

        p_1_year_ago = stock_df["Adj Close"][0]
        p_now = stock_df["Adj Close"][-1]
        return_rate = (p_now - p_1_year_ago) / p_1_year_ago
        # daily_returns = stock_df["Adj Close"].pct_change()
        # cum_returns = (daily_returns + 1).cumprod()
        # return_rate2 = (cum_returns[-1] - 1) / 1

        st.markdown(
            f"從 {stock_df['Adj Close'].index[0].strftime('%Y 年 %m 月 %d 日')} 到 {stock_df['Adj Close'].index[-1].strftime('%Y 年 %m 月 %d 日')}，{symbol} 的累積報酬率為 {round(return_rate * 100, 2)}%。"
        )

        st.markdown(
            """> 💯 這邊需要請大家動動腦 🧠，哪些資訊是你（或你爸爸媽媽 xD）可能會想看到的？只要你能夠提供這些資訊，並寫下有邏輯的敘述，則可以得到 25% 的分數。
                    
> 如果有提供資訊，但邏輯不夠清楚的話，我們會斟酌給分～
> 你可以用一樣的資訊（累積報酬率），但可能僅能得到最高 20% 的分數。加入其他訊息讓我們眼睛為之一亮吧！"""
        )

    st.markdown(
        """

## Bonus - 使用者互動 (20%)

這個部分上課沒有教，但網路上有非常多的資源，想考考看大家能不能有效的查詢想要的資訊，並實際運用（實際上寫程式時很常發生的例子）。以下提供幾個想法：


1. 用戶可能想要看到不同股票的資訊，但你的網站目前只能顯示一支股票
2. 用戶可能想要看當初投入的金額如果不同的話，現在的獲利會是多少
3. 用戶可能想要看到不同區間的股價

請自由發揮，並確保使用者知道怎麼使用（亦即，可能有些地方需要 `label` 或是詳細的說明）。

這邊也提供一個小小的範例 👇🏾
                """
    )

    bonus = st.expander("Bonus 範例 (20%)", True)
    with bonus:
        mini_app()
