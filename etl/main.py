from generate_data import generate_suppliers
from load_data import load_suppliers

suppliers_df = generate_suppliers(20)

load_suppliers(suppliers_df)