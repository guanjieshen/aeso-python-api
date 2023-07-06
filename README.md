# aeso-python-api

[![image](https://img.shields.io/pypi/v/cloudprice.svg)](https://pypi.org/project/cloudprice/)
[![image](https://pepy.tech/badge/cloudprice)](https://pepy.tech/project/geodemo)
[![image](https://github.com/guanjieshen/cloud-compute-pricing/workflows/build/badge.svg)](https://github.com/giswqs/geodemo/actions?query=workflow%3Abuild)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


### Using the API
This API is a python wrapper around the [AESO REST API](https://api.aeso.ca/web/api); therefore, you will first to need to get an [API key from AESO](https://api.aeso.ca/web/api/register).

```python
from aeso import AESOAPI

aeso_api_key = "APIKEY-GOES-HERE"

# Instantiate the AESOAPI Class
aeso_instance = AESOAPI(aeso_api_key)
```


### Supported API Requests


###### Pool Price Report


```python
from aeso import AESOAPI

aeso_api_key = "APIKEY-GOES-HERE"

# Instantiate the AESOAPI Class
aeso_instance = AESOAPI(aeso_api_key)


# Get Pool Price for a set date range
resp = aeso_instance.get_pool_price_report(
    start_date="2023-06-12", end_date="2023-06-13"
)

print(resp)

```

### Helpful Tips

The response from the API can be easily converted to:

__Pandas DataFrame__:

```python
import pandas as pd

resp = aeso_instance.get_pool_price_report(
    start_date="2023-06-12", end_date="2023-06-13"
)
df = pd.DataFrame(resp)
```

__Spark DataFrame__:
```python
import pandas as pd

resp = aeso_instance.get_pool_price_report(
    start_date="2023-06-12", end_date="2023-06-13"
)
pdf = pd.DataFrame(resp)
sparkDF=spark.createDataFrame(pdf) 
```