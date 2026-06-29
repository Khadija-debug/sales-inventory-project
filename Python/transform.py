import pandas as pd

def transform_data(orders):
    print("🚀 Transform started...")

    orders.columns = [col.lower() for col in orders.columns]

    orders = orders.where(pd.notnull(orders), None)

    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
        orders[col] = orders[col].where(orders[col].notnull(), None)

    print("✅ Transform completed")
    return orders