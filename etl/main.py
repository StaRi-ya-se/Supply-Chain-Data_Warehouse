from generate_data import generate_products
from load_data import load_products

products_df = generate_products(100)

load_products(products_df)