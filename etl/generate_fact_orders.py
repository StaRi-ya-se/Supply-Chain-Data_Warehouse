import random
import pandas as pd
from datetime import datetime, timedelta


def generate_fact_orders(num_orders=10000):

    orders = []

    start_date = datetime(2026, 1, 1)

    for _ in range(num_orders):

        # Generate a valid date from Dim_Date
        random_day = random.randint(0, 364)
        selected_date = start_date + timedelta(days=random_day)

        date_id = int(selected_date.strftime("%Y%m%d"))

        # Foreign keys
        product_id = random.randint(1, 100)
        supplier_id = random.randint(1, 20)
        warehouse_id = random.randint(1, 10)

        # Order details
        quantity = random.randint(1, 50)

        revenue = round(
            quantity * random.uniform(20, 1000),
            2
        )

        shipping_cost = round(
            random.uniform(20, 500),
            2
        )

        orders.append({
            "product_id": product_id,
            "supplier_id": supplier_id,
            "warehouse_id": warehouse_id,
            "date_id": date_id,
            "quantity": quantity,
            "revenue": revenue,
            "shipping_cost": shipping_cost
        })

    return pd.DataFrame(orders)


if __name__ == "__main__":

    df = generate_fact_orders(5)

    print(df.head())