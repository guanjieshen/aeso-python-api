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
