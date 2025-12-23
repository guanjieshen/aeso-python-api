"""Pool Price data models"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PoolPrice:
    """
    Pool price data point
    
    Attributes:
        begin_datetime_utc: Start time in UTC
        begin_datetime_mpt: Start time in Mountain Time
        pool_price: Pool price in $/MWh
        forecast_pool_price: Forecasted pool price
        rolling_30day_avg: 30-day rolling average
    """
    begin_datetime_utc: datetime
    begin_datetime_mpt: datetime
    pool_price: float
    forecast_pool_price: float
    rolling_30day_avg: float

