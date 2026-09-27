# Luxury Retail & Customer Analytics

## Project Overview

A synthetic luxury retail analytics project analyzing sales performance, customer behavior, product performance, regional markets, loyalty, satisfaction, and repeat purchasing using SQL, Python, and Tableau.

The project simulates a luxury retail business environment and demonstrates an end-to-end business analytics workflow:

**Synthetic Data → PostgreSQL → SQL → Python / pandas → Tableau → Business Insights**

The project is designed to demonstrate practical skills in:

- SQL data analysis
- PostgreSQL
- Python and pandas
- Customer analytics
- Retail analytics
- Business analytics
- Data preparation
- Data visualization
- Tableau dashboards
- Analytical storytelling

> **Important:** All data used in this project is synthetic and created for educational and portfolio purposes. It does not represent LVMH, any specific luxury brand, real customers, real transactions, or confidential business information.

---

## Business Context

Luxury retail businesses need to understand not only how much they sell, but also:

- which product categories generate the most revenue;
- which regions perform best;
- how online and boutique channels compare;
- which customer segments generate the most revenue;
- how loyalty levels relate to customer spending;
- how satisfaction is associated with repeat purchasing;
- which products generate the highest revenue;
- how average order value differs across markets.

This project approaches these questions from a business analytics perspective.

---

## Dataset

The synthetic dataset covers the period from **January 2023 to December 2025**.

### Customers

**2,200 customers**

Fields:

- `customer_id`
- `region_id`
- `age_group`
- `gender`
- `customer_segment`
- `loyalty_level`

### Orders

**9,000 orders**

Fields:

- `order_id`
- `customer_id`
- `order_date`
- `region_id`
- `channel`
- `product_id`
- `units`
- `unit_price`
- `order_value`
- `satisfaction_score`
- `repeat_customer`

### Products

**28 products**

Fields:

- `product_id`
- `product_category`
- `product_type`
- `unit_price`

### Regions

**10 regions**

Fields:

- `region_id`
- `country`
- `subregion`
- `market`

---

## Data Structure

```text
luxury-retail-and-customer-analytics/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   ├── products.csv
│   │   ├── regions.csv
│   │   └── DATA_NOTE.txt
│   │
│   └── processed/
│       ├── monthly_sales.csv
│       ├── category_sales.csv
│       ├── channel_sales.csv
│       ├── customer_analysis.csv
│       ├── product_analysis.csv
│       └── regional_analysis.csv
│
├── sql/
│   ├── 01_retail_overview.sql
│   ├── 02_monthly_revenue.sql
│   ├── 03_revenue_by_category.sql
│   ├── 04_revenue_by_channel_region.sql
│   ├── 05_customer_segmentation.sql
│   ├── 06_loyalty_repeat_purchase.sql
│   ├── 07_satisfaction_customer_behavior.sql
│   ├── 08_product_performance.sql
│   ├── 09_top_customers.sql
│   └── 10_regional_performance.sql
│
├── python/
│   ├── 01_sales_analysis.py
│   ├── 02_customer_analysis.py
│   ├── 03_product_analysis.py
│   ├── 04_regional_analysis.py
│   └── 05_export_tableau_data.py
│
├── tableau/
│   └── luxury_retail_analytics.twb
│

Analytical Questions
The project addresses the following business questions:
1. Which product categories generate the most revenue?
2. Which categories have the highest average order value?
3. How do sales change over time?
4. Which regions generate the most revenue?
5. How do boutique and online channels compare?
6. Which customer segments generate the most revenue?
7. How does loyalty level relate to customer spending?
8. How is customer satisfaction associated with repeat purchasing?
9. Which products generate the highest revenue?
10. How does average order value differ across regions?
11. How does customer behavior vary across markets?
12. Which customers generate the highest total revenue?

SQL Analysis
PostgreSQL was used as the main analytical database.
Database structure:
regions
   │
   ├── customers
   │      │
   │      └── orders
   │
   └── orders
          │
          └── products

Foreign-key relationships:
customers.region_id → regions.region_id
orders.customer_id → customers.customer_id
orders.region_id   → regions.region_id
orders.product_id  → products.product_id

SQL queries
The project contains 10 substantive SQL analyses:
Query	Analysis
01	Retail Overview
02	Monthly Revenue Trends
03	Revenue by Product Category
04	Revenue by Channel & Region
05	Customer Segmentation & Spending
06	Loyalty & Repeat Purchase Analysis
07	Satisfaction & Customer Behavior
08	Product Performance Ranking
09	Top Customers by Revenue
10	Regional Retail Performance

The SQL analysis demonstrates:
- SELECT
- filtering
- aggregation
- GROUP BY
- HAVING
- CASE
- date functions
- string and numeric functions
- JOIN
- COUNT DISTINCT
- conditional aggregation
- CTEs
- window functions
- ranking
- business KPI calculation

Python Analysis

Python and pandas were used to transform the raw data into Tableau-ready analytical datasets.

01_sales_analysis.py
Creates:
- monthly_sales.csv
- category_sales.csv
- channel_sales.csv
Main metrics:
- revenue
- number of orders
- average order value
- sales by category
- sales by channel
- monthly sales trends

02_customer_analysis.py
Creates:
- customer_analysis.csv
Calculates customer-level metrics:
- number of orders
- total revenue
- average order value
- average satisfaction
- repeat orders
- repeat customer flag
- customer segment
- loyalty level
- age group
- gender
- region

03_product_analysis.py
Creates:
- product_analysis.csv
Calculates:
- orders
- units sold
- revenue
- average order value
- revenue ranking
- product category
- product type

04_regional_analysis.py
Creates:
- regional_analysis.csv
Calculates:
- orders
- customers
- revenue
- average order value
- regional revenue ranking

05_export_tableau_data.py
Validates the processed datasets before they are used in Tableau.

Validation includes:
- file existence
- row count
- column count
- expected column names
- missing values
- Tableau-ready structure
All processed CSV files use a semicolon delimiter for reliable Tableau import.

Tableau Dashboards

The final Tableau workbook contains three dashboards.

1. Sales Overview
The dashboard provides a high-level view of retail performance.
KPIs
- Total Revenue
- Total Orders
- Average Order Value
Visualizations
- Monthly Revenue
- Revenue by Product Category
- Revenue by Channel

2. Customer Analytics
The dashboard focuses on customer behavior and retention.
Visualizations
- Revenue by Customer Segment
- Spending by Loyalty Level
- Repeat Customer Rate by Loyalty
- Repeat Rate by Satisfaction
- Regional Customer Profile
The dashboard is designed to explore customer segmentation, loyalty, satisfaction, and repeat purchasing without interpreting correlation as causation.

3. Retail Performance
The dashboard focuses on regional and product performance.
Visualizations
- Revenue by Region
- Average Order Value by Region
- Top Products
- Category Performance
This dashboard provides a more detailed view of market, product, and category performance.

Key Findings
Because the dataset is synthetic, the findings below should be interpreted as illustrative business patterns rather than real-world luxury retail statistics.

Revenue by Category
The largest revenue categories in the synthetic dataset were:
1. Watches
2. Jewelry
3. Leather Goods
4. Fashion
5. Beauty
Watches and Jewelry generated substantially more revenue than the other categories in the simulated dataset.

Channel Performance
The synthetic dataset shows higher overall revenue contribution from boutique sales compared with online sales.
This allows the project to demonstrate channel-performance analysis and comparison.
Customer Loyalty
Repeat-customer rates are high across all loyalty levels in the synthetic dataset.
This means loyalty level should not be interpreted as the sole explanation for repeat purchasing.

Customer Satisfaction
Repeat purchasing and satisfaction are analyzed at the customer level.
The analysis identifies differences between satisfaction groups but does not claim that satisfaction directly causes repeat purchasing.

Product Performance
The product-level analysis identifies the highest-revenue products and ranks them using SQL window functions and Python-generated metrics.

Regional Performance
The regional analysis compares markets using:
- revenue
- orders
- customer count
- average order value
This makes it possible to distinguish between markets with high total revenue and markets with higher spending per order.

Technology Stack
Database
- PostgreSQL
- DBeaver
Programming
- Python
- pandas
- pathlib
Visualization
- Tableau
Version Control
- GitHub

Data Privacy & Disclaimer
All datasets in this repository are synthetic.
They were generated specifically for educational and portfolio purposes and do not represent:
- LVMH
- any LVMH Maison
- any real luxury brand
- real customers
- real transactions
- real company performance
- official statistics
- confidential business information
The project should therefore be interpreted as a demonstration of analytical methodology rather than as an analysis of a real company's operations.
