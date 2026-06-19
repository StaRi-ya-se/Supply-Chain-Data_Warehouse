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


if __name__ == "__main__":

    df = generate_products()

    print(df.head())
    print(f"\nGenerated {len(df)} products")