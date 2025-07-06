import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['quantity'] * df['unit_price']
    return df

def add_region(df):
    region_map = {
        'Austin': 'Central',
        'Dallas': 'North',
        'Houston': 'South'
    }
    df['region'] = df['city'].map(region_map)
    return df

def final_transform(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    df = add_region(df)
    return df
