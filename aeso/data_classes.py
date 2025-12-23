"""
Data classes (legacy module for backward compatibility)

Note: This module is maintained for backward compatibility.
New code should import from aeso.models.pool_price instead.
"""
from aeso.models.pool_price import PoolPrice

__all__ = ["PoolPrice"]
