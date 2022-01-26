import requests
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
from bs4 import BeautifulSoup


def get_price(stock_id="0050.TW"):
    url = f"https://tw.stock.yahoo.com/d/s/dividend_{stock_id.split('.')[0]}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("div", {"class": "D(f) Ai(fe) Mb(4px)"}).find("span").text
    return price


def get_dividend_yield(stock_id="0050.TW", year=None):
    url = f"https://tw.stock.yahoo.com/d/s/dividend_{stock_id.split('.')[0]}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    div_table = soup.find_all("div", {"class": "table-body-wrapper"})[0].find("ul")

    all_years_raw = div_table.find_all("li")
    first_date = all_years_raw[0].find_all("div")[6].text
    if year == None:
        first_year = first_date.split("/")[0]
    else:
        first_year = str(year)

    # 開始進行加總
    total_div = 0
    for year_raw in all_years_raw:
        tmp_year = year_raw.find_all("div")[6].text.split("/")[0]
        if tmp_year == first_year:
            total_div += float(year_raw.find_all("div")[3].text)

    # 利用剛剛的函式幫我們取得現價
    div_yield = total_div / float(get_price(stock_id))
    return first_year, div_yield, total_div
