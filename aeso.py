from datetime import datetime
from constants import AESO_ROOT_URL
from typing import List
from data_classes import PoolPrice
import requests


class AESOAPI:
    def __init__(self, api_key):
        self.api_root_uri = AESO_ROOT_URL
        self.api_key = api_key
        self.header = {"X-API-Key": "{}".format(self.api_key)}

    def __try_float(self, v):
        try:
            return float(v)
        except Exception:
            return None

    def __generate_api_uri(self, api_endpoint: str) -> str:
        return f"{self.api_root_uri}{api_endpoint}"

    def __submit_get_request(self, uri: str):
        resp = requests.get(uri, headers=self.header)
        return resp

    def __parse_pool_price(self, response: str) -> List[PoolPrice]:
        date_format = "%Y-%m-%d %H:%M"
        list_of_pool_prices: List[PoolPrice] = []
        for item in response:
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
                pool_price=self.__try_float(pool_price),
                forecast_pool_price=self.__try_float(forecast_pool_price),
                rolling_30day_avg=self.__try_float(rolling_30day_avg),
            )
            list_of_pool_prices.append(pool_price_object)
        return list_of_pool_prices

    def get_pool_price_report(self, start_date: str, end_date: str) -> List[PoolPrice]:
        pool_price_endpoint: str = (
            f"report/v1.1/price/poolPrice?startDate={start_date}&endDate={end_date}"
        )
        url = self.__generate_api_uri(pool_price_endpoint)
        pool_price_resp = self.__submit_get_request(url)
        if pool_price_resp.status_code == 200:
            return self.__parse_pool_price(
                pool_price_resp.json()["return"]["Pool Price Report"]
            )
        else:
            raise ValueError(pool_price_resp.raise_for_status())
