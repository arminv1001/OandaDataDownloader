import json
import time
import pandas as pd
import requests
from dateutil.relativedelta import relativedelta
import datetime


def json_to_pandas(json):
    json_file = json.json()
    price_json = json_file["candles"]
    times = []
    close_price, high_price, low_price, open_price = [], [], [], []

    for candle in price_json:
        times.append(candle["time"])
        close_price.append(float(candle["mid"]["c"]))
        high_price.append(float(candle["mid"]["h"]))
        low_price.append(float(candle["mid"]["l"]))
        open_price.append(float(candle["mid"]["o"]))

    dataframe = pd.DataFrame({"close": close_price, "high": high_price, "low": low_price, "open": open_price})
    dataframe.index = pd.to_datetime(times)
    return dataframe


def getHistoricalData(from_dt, to_dt, INSTRUMENT, ACCESS_TOKEN, ACCOUNT_ID, API_URL, timeFrame):
    # 01/01/2019
    from_time = time.mktime((from_dt).timetuple())
    to_time = time.mktime((to_dt).timetuple())
    header = {"Authorization": "Bearer " + ACCESS_TOKEN}
    query = {"from": str(from_dt), "to": str(to_dt), "granularity": timeFrame}
    CANDLES_PATH = f"/v3/accounts/{ACCOUNT_ID}/instruments/{INSTRUMENT}/candles"
    response = requests.get("https://" + API_URL + CANDLES_PATH, headers=header, params=query)
    hist_df = json_to_pandas(response)
    hist_df["Year"] = hist_df.index.year
    hist_df["Month"] = hist_df.index.month
    hist_df["Day"] = hist_df.index.day
    hist_df["Hour"] = hist_df.index.hour
    hist_df["Minute"] = hist_df.index.minute
    hist_df.reset_index(drop=True, inplace=True)
    return hist_df