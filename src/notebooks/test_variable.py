# Databricks notebook source
# MAGIC %md
# MAGIC # Test Notebook - Environment Variables
# MAGIC
# MAGIC This notebook demonstrates how to use bundle variables in Databricks notebooks.
# MAGIC Variables are automatically injected based on the deployment target (dev/uat/prod).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Import Required Libraries

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
import os

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Access Bundle Variables via Widgets
# MAGIC
# MAGIC Databricks bundles inject variables as notebook widgets

# COMMAND ----------

# Get variables from widgets (injected by Databricks bundle)
dbutils.widgets.text("catalog_name", "dev_catalog", "Catalog Name")
dbutils.widgets.text("schema_name", "default", "Schema Name")
dbutils.widgets.text("storage_account", "devstorageaccount", "Storage Account")
dbutils.widgets.text("container_name", "raw-data", "Container Name")
dbutils.widgets.text("env_name", "development", "Environment")

catalog_name = dbutils.widgets.get("catalog_name")
schema_name = dbutils.widgets.get("schema_name")
storage_account = dbutils.widgets.get("storage_account")
container_name = dbutils.widgets.get("container_name")
env_name = dbutils.widgets.get("env_name")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Display Current Configuration

# COMMAND ----------

print("=" * 60)
print(f"Current Environment: {env_name.upper()}")
print("=" * 60)
print(f"Catalog Name:      {catalog_name}")
print(f"Schema Name:       {schema_name}")
print(f"Storage Account:   {storage_account}")
print(f"Container Name:    {container_name}")
print("=" * 60)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Create/Use Schema with Variables

# COMMAND ----------

# Create catalog and schema if they don't exist
spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")
spark.sql(f"USE CATALOG {catalog_name}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
spark.sql(f"USE SCHEMA {schema_name}")

print(f"✅ Using: {catalog_name}.{schema_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Read Data from ADLS using Variables

# COMMAND ----------

# Construct ABFSS path using variables
abfss_path = f"abfss://{container_name}@{storage_account}.dfs.core.windows.net/sample_data/"

print(f"Reading from: {abfss_path}")

# Example: Read a sample CSV file
try:
    df = spark.read.format("csv").option("header", "true").load(abfss_path)
    print(f"✅ Successfully read data from {env_name} environment")
    print(f"Record count: {df.count()}")
except Exception as e:
    print(f"⚠️ Could not read data: {str(e)}")
    # Create sample data for testing
    df = spark.createDataFrame(
        [(1, "Sample", env_name), (2, "Data", env_name)],
        ["id", "name", "environment"]
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Write Data to Delta Table

# COMMAND ----------

# Add metadata columns
df_with_metadata = df.withColumn("ingestion_timestamp", current_timestamp()).withColumn(
    "environment", col("environment") if "environment" in df.columns else spark.lit(env_name)
)

# Write to Delta table
table_name = f"{catalog_name}.{schema_name}.test_table"

df_with_metadata.write.format("delta").mode("overwrite").saveAsTable(table_name)

print(f"✅ Data written to: {table_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Verify Data

# COMMAND ----------

result_df = spark.table(table_name)
display(result_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Summary

# COMMAND ----------

summary = f"""
Environment Configuration Summary:
-----------------------------------
Environment:     {env_name}
Catalog:         {catalog_name}
Schema:          {schema_name}
Storage:         {storage_account}/{container_name}
Target Table:    {table_name}
Records Written: {result_df.count()}

✅ All variables injected successfully from databricks.yml
"""

print(summary)
