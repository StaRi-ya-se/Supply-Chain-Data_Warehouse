import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def load_products(df):
    df.to_sql(
        "dim_product",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} products into Dim_Product")

def load_suppliers(df):

    df.to_sql(
        "dim_supplier",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} suppliers into Dim_Supplier")