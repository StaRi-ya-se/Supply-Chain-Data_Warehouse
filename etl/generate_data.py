from faker import Faker
import pandas as pd
import random

fake = Faker()

PRODUCT_CATEGORIES = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Food",
    "Automotive"
]

def generate_products(num_products=100):

    products = []

    for i in range(num_products):

        products.append({
            "product_name": fake.word().title(),
            "category": random.choice(PRODUCT_CATEGORIES),
            "unit_price": round(random.uniform(10, 1000), 2)
        })

    return pd.DataFrame(products)

SUPPLIER_COUNTRIES = [
    "India",
    "USA",
    "Germany",
    "China",
    "Japan",
    "UK",
    "Canada",
    "Australia"
]

def generate_suppliers(num_suppliers=20):

    suppliers = []

    for _ in range(num_suppliers):

        suppliers.append({
            "supplier_name": fake.company(),
            "country": random.choice(SUPPLIER_COUNTRIES)
        })

    return pd.DataFrame(suppliers)

WAREHOUSE_CITIES = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

def generate_warehouses(num_warehouses=10):

    warehouses = []

    for i in range(num_warehouses):

        warehouses.append({
            "warehouse_name": f"Warehouse_{i+1}",
            "city": random.choice(WAREHOUSE_CITIES),
            "capacity": random.randint(1000, 10000)
        })

    return pd.DataFrame(warehouses)

from datetime import datetime, timedelta

def generate_dates(num_days=365):

    start_date = datetime(2026, 1, 1)

    dates = []

    for i in range(num_days):

        current_date = start_date + timedelta(days=i)

        dates.append({
            "date_id": int(current_date.strftime("%Y%m%d")),
            "full_date": current_date.date(),
            "day": current_date.day,
            "month": current_date.month,
            "quarter": (current_date.month - 1) // 3 + 1,
            "year": current_date.year,
            "day_name": current_date.strftime("%A"),
            "month_name": current_date.strftime("%B")
        })

    return pd.DataFrame(dates)

if __name__ == "__main__":

    df = generate_products()

    print(df.head())
    print(f"\nGenerated {len(df)} products")