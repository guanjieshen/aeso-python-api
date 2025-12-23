# AESO Python API

[![image](https://img.shields.io/pypi/v/cloudprice.svg)](https://pypi.org/project/cloudprice/)
[![image](https://pepy.tech/badge/cloudprice)](https://pepy.tech/project/geodemo)
[![image](https://github.com/guanjieshen/cloud-compute-pricing/workflows/build/badge.svg)](https://github.com/giswqs/geodemo/actions?query=workflow%3Abuild)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python wrapper for the [Alberta Electric System Operator (AESO) API](https://api.aeso.ca/web/api). Easily access pool price reports and electricity market data.

## Installation

```bash
pip install aeso
```

## Getting Started

### 1. Get Your API Key

Register for a free API key at the [AESO API Portal](https://api.aeso.ca/web/api/register).

### 2. Basic Usage

```python
import os
from aeso import AESOAPI

# Initialize with your API key from environment variable
api_key = os.environ.get('AESO_API_KEY')

# Or directly (not recommended for production)
# api_key = "your-api-key-here"

aeso = AESOAPI(api_key)

# Fetch pool price data
prices = aeso.get_pool_price_report(
    start_date="2023-06-12",
    end_date="2023-06-13"
)

print(prices)
```

## API Reference

### Pool Price Report

Fetch electricity pool price data for a specified date range.

**Parameters:**
- `start_date` (str, required): Start date in format `YYYY-MM-DD`
- `end_date` (str, optional): End date in format `YYYY-MM-DD`

If `end_date` is omitted, data will include pool price values for all completed settlement hours of the day specified by `start_date`.

**Returns:**

A list of `PoolPrice` objects with the following attributes:

```python
@dataclass
class PoolPrice:
    begin_datetime_utc: datetime  # Start time in UTC
    begin_datetime_mpt: datetime  # Start time in Mountain Time
    pool_price: float            # Pool price in $/MWh
    forecast_pool_price: float   # Forecasted pool price
    rolling_30day_avg: float     # 30-day rolling average
```

**Example:**

```python
from aeso import AESOAPI
import os

aeso = AESOAPI(os.environ.get('AESO_API_KEY'))

# Get prices for a date range
prices = aeso.get_pool_price_report(
    start_date="2023-06-12",
    end_date="2023-06-13"
)

# Access the data
for price in prices:
    print(f"{price.begin_datetime_mpt}: ${price.pool_price}/MWh")
```

## Working with Data

### Convert to Pandas DataFrame

```python
import pandas as pd
from aeso import AESOAPI
import os

aeso = AESOAPI(os.environ.get('AESO_API_KEY'))

prices = aeso.get_pool_price_report(
    start_date="2023-06-12",
    end_date="2023-06-13"
)

# Convert to DataFrame
df = pd.DataFrame(prices)
print(df.head())
```

### Convert to Spark DataFrame

```python
import pandas as pd
from aeso import AESOAPI
import os

aeso = AESOAPI(os.environ.get('AESO_API_KEY'))

prices = aeso.get_pool_price_report(
    start_date="2023-06-12",
    end_date="2023-06-13"
)

# Convert to pandas first
pdf = pd.DataFrame(prices)

# Then to Spark
spark_df = spark.createDataFrame(pdf)
```


## Testing Your Setup

You can test the API by using the example file:

```bash
# Set your API key
export AESO_API_KEY='your-api-key-here'

# Copy and run the example
cp example_template.py example.py
# Edit example.py with your API key, then:
python example.py
```

## Security Note

⚠️ **Keep your API key secure**

- Use environment variables instead of hardcoding your API key
- Never commit your API key to version control
- Files like `example.py`, `test_new_api.py`, and `config.py` are gitignored for your security

## Requirements

- Python 3.6+
- requests >= 2.26.0

## Resources

- [AESO API Documentation](https://api.aeso.ca/web/api)
- [Register for API Key](https://api.aeso.ca/web/api/register)

## License

MIT License
