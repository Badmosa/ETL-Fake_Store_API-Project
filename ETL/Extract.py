import pandas as pd
import requests

base_url = 'https://fakestoreapi.com'

def extract_product():
    url = f'{base_url}/products'
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    product_df = pd.DataFrame(data)

    return product_df