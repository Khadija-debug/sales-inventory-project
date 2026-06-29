from config  import DATASET_PATH
import pandas as pd
import os

def extract_data():
    print("🚀 Extract started...")

    BASE_PATH = DATASET_PATH

    orders = pd.read_csv(os.path.join(BASE_PATH, "olist_orders_dataset.csv"))
    customers = pd.read_csv(os.path.join(BASE_PATH, "olist_customers_dataset.csv"))
    products = pd.read_csv(os.path.join(BASE_PATH, "olist_products_dataset.csv"))
    order_items = pd.read_csv(os.path.join(BASE_PATH, "olist_order_items_dataset.csv"))
    payments = pd.read_csv(os.path.join(BASE_PATH, "olist_order_payments_dataset.csv"))
    reviews = pd.read_csv(os.path.join(BASE_PATH, "olist_order_reviews_dataset.csv"))
    sellers = pd.read_csv(os.path.join(BASE_PATH, "olist_sellers_dataset.csv"))
   
    print("✅ Orders:", orders.shape)
    print("✅ Customers:", customers.shape)
    print("✅ Products:", products.shape)
    print ("order_items:", order_items.shape)
    print("✅ Payments:", payments.shape)
    print("✅ Reviews:", reviews.shape)
    print("✅ Sellers:", sellers.shape)
    return orders, customers, products, order_items, payments, reviews, sellers