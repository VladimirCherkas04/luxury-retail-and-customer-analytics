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


# ============================================================
# MERGE ORDERS + PRODUCTS
# ============================================================

product_sales = orders.merge(
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
# PRODUCT PERFORMANCE
# ============================================================

product_analysis = (
    product_sales
    .groupby(
        [
            "product_id",
            "product_category",
            "product_type"
        ]
    )
    .agg(
        orders=("order_id", "nunique"),
        units_sold=("units", "sum"),
        revenue=("order_value", "sum")
    )
    .reset_index()
)


# ============================================================
# AVERAGE ORDER VALUE
# ============================================================

product_analysis["average_order_value"] = (
    product_analysis["revenue"]
    / product_analysis["orders"]
).round(2)

product_analysis["revenue"] = (
    product_analysis["revenue"].round(2)
)


# ============================================================
# REVENUE RANK
# ============================================================

product_analysis["revenue_rank"] = (
    product_analysis["revenue"]
    .rank(
        method="min",
        ascending=False
    )
    .astype(int)
)


# ============================================================
# FINAL COLUMN ORDER
# ============================================================

product_analysis = product_analysis[
    [
        "product_id",
        "product_category",
        "product_type",
        "orders",
        "units_sold",
        "revenue",
        "average_order_value",
        "revenue_rank"
    ]
].sort_values(
    "revenue_rank"
)


# ============================================================
# SAVE TABLEAU-READY CSV
# ============================================================

output_file = OUTPUT_DIR / "product_analysis.csv"

product_analysis.to_csv(
    output_file,
    index=False,
    sep=";"
)


# ============================================================
# VALIDATION
# ============================================================

check = pd.read_csv(
    output_file,
    sep=";"
)

if len(check.columns) != 8:
    raise ValueError(
        "Unexpected number of columns in product_analysis.csv"
    )

if check["revenue"].isna().any():
    raise ValueError(
        "Revenue contains missing values."
    )

if check["average_order_value"].isna().any():
    raise ValueError(
        "Average order value contains missing values."
    )


# ============================================================
# RESULT
# ============================================================

print("Product analysis completed.")
print(f"Products analyzed: {len(product_analysis)}")
print(f"Columns: {len(product_analysis.columns)}")
print(f"Output: {output_file}")