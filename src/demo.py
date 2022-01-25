import streamlit as st
from bs4 import BeautifulSoup

# from urllib.request import urlopen
import requests
import yfinance as yf
import pandas as pd
from dateutil.relativedelta import relativedelta

from . import pws


def stock_price():
    symbol = st.text_input(label="輸入想要查詢的股票代碼", value="0050.TW")
    stock_obj = yf.Ticker(symbol)

    st.write(f"## 分析 {stock_obj.info['longName']}")
    st.write(f"### 目前成交價格為：**{pws.get_price(symbol)}**")
    stock_df = stock_obj.history(
        start="2011-3-12", end="2021-3-12", auto_adjust=False
    )  # period="max"

    st.line_chart(stock_df.Close)
    st.bar_chart(stock_df.Volume)

    stock_daily_return = stock_df["Adj Close"].ffill().pct_change()
    start = stock_daily_return.index[0]
    end = stock_daily_return.index[-1]  # 以 stock 的最後一天為結束日期.

    year_difference = (
        relativedelta(end, start).years
        + (relativedelta(end, start).months) / 12
        + (relativedelta(end, start).days) / 365.2425
    )

    init_balance = balance = 3000
    total_balance = stock_daily_return.copy()
    total_balance[0] = 0

    for i in range(len(stock_daily_return)):
        balance = balance * (1 + total_balance[i])
        total_balance[i] = balance

    total_balance.rename("成長變化", inplace=True)

    st.line_chart(total_balance)

    return_rate = (total_balance[-1] - total_balance[0]) / total_balance[0]
    st.write(
        f"如果當初投資 {init_balance} 元，現在會有 {total_balance[-1]} 元。經過約 {year_difference:.2f} 年的變化，投資報酬率為 {return_rate * 100:.2f}%。"
    )

    st.write("股票基本資料：")
    stock_info = stock_obj.info

    st.write(stock_info)


def main():
    st.write("# 成果 - 股票分析")
    st.write("本頁面僅使用台灣地區股票作為例子。")

    stock_price()
    st.button("重新整理")


if __name__ == "__main__":
    main()
