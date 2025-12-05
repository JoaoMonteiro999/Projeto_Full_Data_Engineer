from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.getOrCreate()


# GCS Paths
bronze_path = "gs://your_bucket/bronze/"
silver_path = "gs://your_bucket/silver/"
gold_path = "gs://your_bucket/gold/"

# 1 — Read Bronze using pandas
