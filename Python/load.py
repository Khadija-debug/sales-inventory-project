from config import CONNECTION_STRING
import pyodbc
import pandas as pd

def load_data(orders, customers, products, order_items, payments, reviews, sellers):
    print("🚀 LOAD process started...")

    

    # -----------------------
    # CONNECT TO SQL SERVER
    # -----------------------
    conn = pyodbc.connect(CONNECTION_STRING)
    cursor = conn.cursor()

    # Speed optimization
    cursor.fast_executemany = True

    print("✅ Connected to SQL Server")

    # -----------------------
    # CLEAN DATA
    # -----------------------
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

    # -----------------------
    # BULK INSERT
    # -----------------------
    print("📤 Bulk inserting data into SQL Server...")

    insert_query = """
    INSERT INTO orders (
        order_id,
        customer_id,
        order_status,
        order_purchase_timestamp,
        order_approved_at,
        order_delivered_carrier_date,
        order_delivered_customer_date,
        order_estimated_delivery_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

    data = list(orders.itertuples(index=False, name=None))

    cursor.executemany(insert_query, data)

    conn.commit()

    print("✅ Bulk insert completed successfully")
    print(f"Customers ready:{len(customers)} rows") 
    print(f"Products ready:{len(products)} rows")
    print(f"Order Items ready:{len(order_items)} rows")
    print(f"Payments ready:{len(payments)} rows")
    print(f"Reviews ready:{len(reviews)} rows")
    print(f"Sellers ready:{len(sellers)} rows")
    cursor.close()
    conn.close()

    print("🔌 Connection closed")
    print("🎉 LOAD process completed")