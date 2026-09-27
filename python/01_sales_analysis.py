import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(
    "/Users/vovcik/Documents/luxury-retail-and-customer-analytics"
)

RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

orders = pd.read_csv(
    RAW_DIR / "orders.csv"
)

products = pd.read_csv(
    RAW_DIR / "products.csv"
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)


# ============================================================
# MERGE ORDERS + PRODUCTS
# ============================================================

sales = orders.merge(
    products[
        [
            "product_id",
            "product_category",
            "product_type"
        ]
    ],
    on="product_id",
    how="left"
)


# ============================================================
# 1. MONTHLY SALES
# ============================================================

monthly_sales = (
    sales
    .groupby(
        sales["order_date"].dt.to_period("M")
    )
    .agg(
        orders=("order_id", "nunique"),
        revenue=("order_value", "sum")
    )
    .reset_index()
)

monthly_sales["order_date"] = (
    monthly_sales["order_date"].astype(str)
)

monthly_sales["average_order_value"] = (
    monthly_sales["revenue"]
    / monthly_sales["orders"]
).round(2)

monthly_sales["revenue"] = (
    monthly_sales["revenue"].round(2)
)

monthly_sales = monthly_sales[
    [
        "order_date",
        "orders",
        "revenue",
        "average_order_value"
    ]
]


# ============================================================
# 2. PRODUCT CATEGORY PERFORMANCE
# ============================================================

category_sales = (
    sales
    .groupby("product_category")
    .agg(
        orders=("order_id", "nunique"),
        units_sold=("units", "sum"),
        revenue=("order_value", "sum")
    )
    .reset_index()
)

category_sales["average_order_value"] = (
    category_sales["revenue"]
    / category_sales["orders"]
).round(2)

category_sales["revenue"] = (
    category_sales["revenue"].round(2)
)

category_sales = category_sales[
    [
        "product_category",
        "orders",
        "units_sold",
        "revenue",
        "average_order_value"
    ]
].sort_values(
    "revenue",
    ascending=False
)


# ============================================================
# 3. CHANNEL PERFORMANCE
# ============================================================

channel_sales = (
    sales
    .groupby("channel")
    .agg(
        orders=("order_id", "nunique"),
        revenue=("order_value", "sum")
    )
    .reset_index()
)

channel_sales["average_order_value"] = (
    channel_sales["revenue"]
    / channel_sales["orders"]
).round(2)

channel_sales["revenue"] = (
    channel_sales["revenue"].round(2)
)

channel_sales = channel_sales[
    [
        "channel",
        "orders",
        "revenue",
        "average_order_value"
    ]
].sort_values(
    "revenue",
    ascending=False
)


# ============================================================
# SAVE TABLEAU-READY FILES
# ============================================================

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales.csv",
    index=False,
    sep=";"
)

category_sales.to_csv(
    OUTPUT_DIR / "category_sales.csv",
    index=False,
    sep=";"
)

channel_sales.to_csv(
    OUTPUT_DIR / "channel_sales.csv",
    index=False,
    sep=";"
)


# ============================================================
# RESULT
# ============================================================

print("Sales analysis completed.")
print(f"Monthly rows: {len(monthly_sales)}")
print(f"Category rows: {len(category_sales)}")
print(f"Channel rows: {len(channel_sales)}")

print("\nProcessed files saved to:")
print(OUTPUT_DIR)