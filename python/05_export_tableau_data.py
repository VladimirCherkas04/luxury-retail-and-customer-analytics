import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(
    "/Users/vovcik/Documents/luxury-retail-and-customer-analytics"
)

PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================================
# EXPECTED FILES
# ============================================================

files = {
    "monthly_sales.csv": 4,
    "category_sales.csv": 5,
    "channel_sales.csv": 4,
    "customer_analysis.csv": 12,
    "product_analysis.csv": 8,
    "regional_analysis.csv": 9
}


# ============================================================
# VALIDATION
# ============================================================

print("Checking Tableau-ready processed files...\n")

for file_name, expected_columns in files.items():

    file_path = PROCESSED_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(
            f"Missing file: {file_path}"
        )

    df = pd.read_csv(
        file_path,
        sep=";"
    )

    print(
        f"{file_name}: "
        f"{len(df)} rows, "
        f"{len(df.columns)} columns"
    )

    print(
        "Columns:",
        ", ".join(df.columns)
    )

    # Check column count
    if len(df.columns) != expected_columns:
        raise ValueError(
            f"{file_name}: expected "
            f"{expected_columns} columns, "
            f"got {len(df.columns)}"
        )

    # Check for completely empty columns
    empty_columns = [
        column
        for column in df.columns
        if df[column].isna().all()
    ]

    if empty_columns:
        raise ValueError(
            f"{file_name} contains completely empty "
            f"columns: {empty_columns}"
        )


# ============================================================
# FINAL RESULT
# ============================================================

print("\nAll processed files are Tableau-ready.")
print(f"Location: {PROCESSED_DIR}")