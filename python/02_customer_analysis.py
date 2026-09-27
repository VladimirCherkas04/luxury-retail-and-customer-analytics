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

customers = pd.read_csv(
    RAW_DIR / "customers.csv"
)

orders = pd.read_csv(
    RAW_DIR / "orders.csv"
)


# ============================================================
# CUSTOMER-LEVEL ANALYSIS
# ============================================================

customer_analysis = (
    orders
    .groupby("customer_id")
    .agg(
        orders=("order_id", "nunique"),
        total_revenue=("order_value", "sum"),
        repeat_orders=(
            "repeat_customer",
            lambda x: (x == "Yes").sum()
        ),
        average_satisfaction=(
            "satisfaction_score",
            "mean"
        )
    )
    .reset_index()
)


# ============================================================
# CALCULATE AVERAGE ORDER VALUE
# ============================================================

customer_analysis["average_order_value"] = (
    customer_analysis["total_revenue"]
    / customer_analysis["orders"]
).round(2)

customer_analysis["total_revenue"] = (
    customer_analysis["total_revenue"]
    .round(2)
)

customer_analysis["average_satisfaction"] = (
    customer_analysis["average_satisfaction"]
    .round(2)
)


# ============================================================
# REPEAT CUSTOMER FLAG
# ============================================================

customer_analysis["is_repeat_customer"] = (
    customer_analysis["repeat_orders"] > 0
).astype(int)


# ============================================================
# ADD CUSTOMER CHARACTERISTICS
# ============================================================

customer_analysis = customer_analysis.merge(
    customers[
        [
            "customer_id",
            "customer_segment",
            "loyalty_level",
            "age_group",
            "gender",
            "region_id"
        ]
    ],
    on="customer_id",
    how="left"
)


# ============================================================
# FINAL COLUMN ORDER
# ============================================================

customer_analysis = customer_analysis[
    [
        "customer_id",
        "orders",
        "total_revenue",
        "average_order_value",
        "average_satisfaction",
        "repeat_orders",
        "is_repeat_customer",
        "customer_segment",
        "loyalty_level",
        "age_group",
        "gender",
        "region_id"
    ]
]


# ============================================================
# SAVE
# ============================================================

customer_analysis.to_csv(
    OUTPUT_DIR / "customer_analysis.csv",
    index=False,
    sep=";"
)


# ============================================================
# RESULT
# ============================================================

print("Customer analysis completed.")
print(f"Customers analyzed: {len(customer_analysis)}")
print(
    f"Output: {OUTPUT_DIR / 'customer_analysis.csv'}"
)