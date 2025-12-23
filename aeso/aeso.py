"""Main AESO API client"""
from typing import List
from aeso.constants import AESO_ROOT_URL
from aeso.resources.pool_price import PoolPriceResource
from aeso.models.pool_price import PoolPrice


class AESOAPI:
    """
    Main client for AESO API
    
    This client provides access to various AESO market data through a resource-based
    interface. Each resource (pool_price, load, generation, etc.) encapsulates
    related API endpoints.
    
    Args:
        api_key: Your AESO API key from https://api.aeso.ca/web/api/register
    
    Example:
        >>> from aeso import AESOAPI
        >>> client = AESOAPI("your-api-key")
        >>> 
        >>> # New resource-based interface
        >>> prices = client.pool_price.get_report("2023-06-12", "2023-06-13")
        >>> 
        >>> # Legacy method (still supported)
        >>> prices = client.get_pool_price_report("2023-06-12", "2023-06-13")
    
    Resources:
        pool_price: Pool price related endpoints
        
    Future Resources:
        load: Load/demand endpoints (coming soon)
        generation: Generation endpoints (coming soon)
        intertie: Intertie flow endpoints (coming soon)
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the AESO API client
        
        Args:
            api_key: Your AESO API key
        """
        self.api_key = api_key
        self.base_url = AESO_ROOT_URL
        self.headers = {"API-KEY": api_key}
        
        # Initialize resources
        self.pool_price = PoolPriceResource(self)
        
        # Future resources will be added here:
        # self.load = LoadResource(self)
        # self.generation = GenerationResource(self)
        # self.intertie = IntertieResource(self)
    
    # Backward compatibility methods
    def get_pool_price_report(
        self, 
        start_date: str, 
        end_date: str
    ) -> List[PoolPrice]:
        """
        Fetch pool price report (legacy method)
        
        Note: This method is maintained for backward compatibility.
        New code should use: client.pool_price.get_report()
        
        Args:
            start_date: Start date in format YYYY-MM-DD
            end_date: End date in format YYYY-MM-DD
            
        Returns:
            List of PoolPrice objects
        """
        return self.pool_price.get_report(start_date, end_date)
