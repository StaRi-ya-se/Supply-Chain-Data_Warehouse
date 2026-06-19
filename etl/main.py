from generate_fact_orders import generate_fact_orders
from load_data import load_fact_orders

orders_df = generate_fact_orders(10000)

load_fact_orders(orders_df)