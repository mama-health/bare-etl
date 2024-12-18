from pyspark.sql import SparkSession

def run_etl():
    spark = SparkSession.builder \
        .appName("SimpleETL") \
        .getOrCreate()

    df = spark.read.csv("data/input_data.csv", header=True, inferSchema=True)

    rows = df.collect()
    for row in rows:
        print(row)

    spark.stop()