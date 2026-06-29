def validate_data(orders, customers, products):
    print("🔍 Running Data Validation...")

    if len(orders) == 0:
        raise Exception("Orders dataset is empty!")

    if len(customers) == 0:
        raise Exception("Customers dataset is empty!")

    if len(products) == 0:
        raise Exception("Products dataset is empty!")

    print("✅ Validation Passed")
    print(f"Orders: {len(orders)}")
    print(f"Customers: {len(customers)}")
    print(f"Products: {len(products)}")