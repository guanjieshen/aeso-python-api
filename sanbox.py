# Databricks notebook source
# MAGIC %md ##### Class Defintion

# COMMAND ----------

import requests
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class PoolPrice:
    begin_datetime_utc: datetime
    begin_datetime_mpt: datetime
    pool_price: float
    forecast_pool_price: float
    rolling_30day_avg: float


class aeso:
    def __init__(self, api_key):
        self.api_root_uri = "https://api.aeso.ca/"
        self.api_key = api_key
        self.header = {"X-API-Key": "{}".format(self.api_key)}

    def __generate_api_uri(self, api_endpoint: str) -> str:
        return f"{self.api_root_uri}{api_endpoint}"

    def __submit_get_request(self, uri: str):
        resp = requests.get(uri, headers=self.header)
        return resp

    def __parse_pool_price(self, response: str) -> List[PoolPrice]:
        date_format = "%Y-%m-%d %H:%M"
        list_of_pool_prices: List[PoolPrice] = []
        for item in pool_price_data:
            begin_datetime_utc = datetime.strptime(
                item["begin_datetime_utc"], date_format
            )
            begin_datetime_mpt = datetime.strptime(
                item["begin_datetime_mpt"], date_format
            )
            pool_price = item["pool_price"]
            forecast_pool_price = item["forecast_pool_price"]
            rolling_30day_avg = item["rolling_30day_avg"]

            pool_price_object: PoolPrice = PoolPrice(
                begin_datetime_utc=begin_datetime_utc,
                begin_datetime_mpt=begin_datetime_mpt,
                pool_price=float(pool_price),
                forecast_pool_price=float(forecast_pool_price),
                rolling_30day_avg=float(rolling_30day_avg),
            )
            list_of_pool_prices.append(pool_price_object)
        return list_of_pool_prices

    def get_pool_price_report(self, start_date: str, end_date: str) -> List[PoolPrice]:
        pool_price_endpoint: str = (
            f"report/v1.1/price/poolPrice?startDate={start_date}&endDate={end_date}"
        )
        url = self.__generate_api_uri(pool_price_endpoint)
        pool_price_resp = self.__submit_get_request(url)
        return self.__parse_pool_price(
            pool_price_resp.json()["return"]["Pool Price Report"]
        )


# COMMAND ----------

# MAGIC %md Testing Class

# COMMAND ----------

aeso_api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJvaXNrM2EiLCJpYXQiOjE2Nzc2OTMyOTh9.wojWs2r9ecH88GbPpy34FShwhkjXPJXBAijY8S3rNAw'
aeso_instance = aeso(aeso_api_key)
resp = aeso_instance.get_pool_price_report(start_date="2023-05-30",end_date= "2023-05-31")
print(resp[0].forecast_pool_price)

# COMMAND ----------

import pandas as pd
df = pd.DataFrame(resp)
display(df)

# COMMAND ----------


