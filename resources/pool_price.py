"""Pool Price resource"""
from datetime import datetime
from typing import List, Optional
from resources.base import BaseResource
from models.pool_price import PoolPrice


class PoolPriceResource(BaseResource):
    """Handle pool price related API calls"""
    
    def get_report(
        self, 
        start_date: str, 
        end_date: Optional[str] = None
    ) -> List[PoolPrice]:
        """
        Fetch pool price report for date range
        
        Args:
            start_date: Start date in format YYYY-MM-DD
            end_date: End date in format YYYY-MM-DD (optional)
                     If omitted, returns all completed settlement hours for start_date
            
        Returns:
            List of PoolPrice objects
            
        Example:
            >>> client = AESOAPI("your-api-key")
            >>> prices = client.pool_price.get_report("2023-06-12", "2023-06-13")
        """
        # Build query parameters
        params = {"startDate": start_date}
        if end_date:
            params["endDate"] = end_date
        
        # Make API request
        endpoint = "v1.1/price/poolPrice"
        response = self._make_request(endpoint, params=params)
        
        # Parse and return results
        return self._parse_pool_prices(response["return"]["Pool Price Report"])
    
    def _parse_pool_prices(self, data: list) -> List[PoolPrice]:
        """
        Parse pool price data from API response
        
        Args:
            data: List of pool price records from API
            
        Returns:
            List of PoolPrice objects
        """
        date_format = "%Y-%m-%d %H:%M"
        pool_prices = []
        
        for item in data:
            pool_price = PoolPrice(
                begin_datetime_utc=datetime.strptime(
                    item["begin_datetime_utc"], date_format
                ),
                begin_datetime_mpt=datetime.strptime(
                    item["begin_datetime_mpt"], date_format
                ),
                pool_price=self._try_float(item["pool_price"]),
                forecast_pool_price=self._try_float(item["forecast_pool_price"]),
                rolling_30day_avg=self._try_float(item["rolling_30day_avg"])
            )
            pool_prices.append(pool_price)
        
        return pool_prices

