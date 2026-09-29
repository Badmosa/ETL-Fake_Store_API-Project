import pandas as pd

def transform_product(product_df):
    df = product_df.copy()

    df = df.rename(columns= {
        'id':           'product_id',
        'title':        'product_name',
        'price':        'product_price',
        'category':     'product_category',
        'description':  'product_description'
    }
                   )

    df = df[[
        'product_id', 'product_name', 'product_price', 'product_category', 'product_description'
    ]]
df['produict_price'] = df['product_price'].astype(float)