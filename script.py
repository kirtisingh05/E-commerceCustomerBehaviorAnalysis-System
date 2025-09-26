# Let's create a sample e-commerce dataset for our project
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create sample data that mimics the UCI Online Retail dataset structure
# Product catalog
products = [
    'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'USB Drive',
    'Smartphone', 'Phone Case', 'Charger', 'Power Bank', 'Bluetooth Speaker',
    'Tablet', 'Tablet Cover', 'Stylus Pen', 'Screen Protector',
    'Coffee Mug', 'Water Bottle', 'Notebook', 'Pen Set', 'Desk Lamp',
    'Gaming Chair', 'Desk Organizer', 'Calendar', 'Stapler', 'Paper Clips'
]

# Generate transactions
num_transactions = 5000
transactions = []

# Define some associations (items frequently bought together)
associations = [
    ['Laptop', 'Mouse', 'Keyboard'],
    ['Smartphone', 'Phone Case', 'Screen Protector', 'Charger'],
    ['Tablet', 'Tablet Cover', 'Stylus Pen'],
    ['Coffee Mug', 'Water Bottle'],
    ['Notebook', 'Pen Set'],
    ['Monitor', 'Webcam', 'Headphones'],
    ['Gaming Chair', 'Desk Lamp', 'Desk Organizer']
]

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 3, 1)

for i in range(num_transactions):
    invoice_no = f"INV{str(i+10000).zfill(6)}"
    customer_id = np.random.randint(1000, 9999)
    invoice_date = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days))
    country = np.random.choice(['USA', 'UK', 'Germany', 'France', 'Canada'], p=[0.4, 0.25, 0.15, 0.1, 0.1])
    
    # Decide if this transaction follows an association pattern or is random
    if np.random.random() < 0.3:  # 30% chance of following association
        association = random.choice(associations)
        items_in_transaction = random.sample(association, min(len(association), np.random.randint(1, len(association)+1)))
    else:
        # Random items
        num_items = np.random.randint(1, 6)
        items_in_transaction = random.sample(products, num_items)
    
    for item in items_in_transaction:
        stock_code = f"PROD{hash(item) % 10000:04d}"
        quantity = np.random.randint(1, 5)
        unit_price = round(np.random.uniform(5, 200), 2)
        
        transactions.append({
            'InvoiceNo': invoice_no,
            'StockCode': stock_code,
            'Description': item,
            'Quantity': quantity,
            'InvoiceDate': invoice_date,
            'UnitPrice': unit_price,
            'CustomerID': customer_id,
            'Country': country
        })

# Create DataFrame
df = pd.DataFrame(transactions)

# Save to CSV
df.to_csv('ecommerce_transactions.csv', index=False)

print("Dataset Created Successfully!")
print(f"Total Transactions: {len(df)}")
print(f"Unique Customers: {df['CustomerID'].nunique()}")
print(f"Unique Products: {df['Description'].nunique()}")
print(f"Date Range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
print("\nFirst few rows:")
print(df.head())