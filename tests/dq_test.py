assert spark.table("develop.bronze.sales").count() > 0
assert spark.table("develop.silver.sales_cleaned").count() > 0
assert spark.table("develop.gold.total_sales_product").count() > 0


expected_cols = ["product_id", "total_sales"]
assert all(col in df.columns for col in expected_cols)