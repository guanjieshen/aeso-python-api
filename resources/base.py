"""Base resource class with shared functionality"""
from typing import Optional, Dict, Any
import requests


class BaseResource:
    """Base class for all AESO API resources"""
    
    def __init__(self, client):
        """
        Initialize the resource with a reference to the parent client
        
        Args:
            client: The AESOAPI client instance
        """
        self.client = client
    
    def _make_request(
        self, 
        endpoint: str, 
        method: str = "GET", 
        params: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make HTTP request to AESO API
        
        Args:
            endpoint: API endpoint path
            method: HTTP method (default: GET)
            params: Query parameters
            
        Returns:
            Parsed JSON response
            
        Raises:
            ValueError: If HTTP request fails
        """
        url = f"{self.client.base_url}{endpoint}"
        
        if method == "GET":
            response = requests.get(url, headers=self.client.headers, params=params)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    @staticmethod
    def _try_float(value) -> Optional[float]:
        """
        Safely convert value to float
        
        Args:
            value: Value to convert
            
        Returns:
            Float value or None if conversion fails
        """
        try:
            return float(value)
        except (ValueError, TypeError):
            return None
    
    @staticmethod
    def _try_int(value) -> Optional[int]:
        """
        Safely convert value to int
        
        Args:
            value: Value to convert
            
        Returns:
            Integer value or None if conversion fails
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            return None

