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

regions = pd.read_csv(
    RAW_DIR / "regions.csv"
)


# ============================================================
# MERGE ORDERS + REGIONS
# ============================================================

regional_sales = orders.merge(
    regions[
        [
            "region_id",
            "country",
            "subregion",
            "market"
        ]
    ],
    on="region_id",
    how="left"
)


# ============================================================
# REGIONAL PERFORMANCE
# ============================================================

regional_analysis = (
    regional_sales
    .groupby(
        [
            "region_id",
            "country",
            "subregion",
            "market"
        ]
    )
    .agg(
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
        revenue=("order_value", "sum")
    )
    .reset_index()
)


# ============================================================
# AVERAGE ORDER VALUE
# ============================================================

regional_analysis["average_order_value"] = (
    regional_analysis["revenue"]
    / regional_analysis["orders"]
).round(2)

regional_analysis["revenue"] = (
    regional_analysis["revenue"].round(2)
)


# ============================================================
# REVENUE RANK
# ============================================================

regional_analysis["revenue_rank"] = (
    regional_analysis["revenue"]
    .rank(
        method="min",
        ascending=False
    )
    .astype(int)
)


# ============================================================
# FINAL COLUMN ORDER
# ============================================================

regional_analysis = regional_analysis[
    [
        "region_id",
        "country",
        "subregion",
        "market",
        "orders",
        "customers",
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

output_file = OUTPUT_DIR / "regional_analysis.csv"

regional_analysis.to_csv(
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

if len(check.columns) != 9:
    raise ValueError(
        "Unexpected number of columns in regional_analysis.csv"
    )

if check["revenue"].isna().any():
    raise ValueError(
        "Revenue contains missing values."
    )

if check["average_order_value"].isna().any():
    raise ValueError(
        "Average order value contains missing values."
    )

if check["country"].isna().any():
    raise ValueError(
        "Country contains missing values."
    )


# ============================================================
# RESULT
# ============================================================

print("Regional analysis completed.")
print(f"Regions analyzed: {len(regional_analysis)}")
print(f"Columns: {len(regional_analysis.columns)}")
print(f"Output: {output_file}")