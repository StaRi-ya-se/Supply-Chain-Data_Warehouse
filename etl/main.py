from generate_data import generate_warehouses
from load_data import load_warehouses

warehouses_df = generate_warehouses(10)

load_warehouses(warehouses_df)