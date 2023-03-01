from pyspark.sql import SparkSession, functions as F
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
import os

spark = SparkSession.builder.appName("Spark ON K8S").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("WARN")

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
rdd = spark.sparkContext.parallelize(data)

dfFromRDD1 = rdd.toDF()
dfFromRDD1.printSchema()
dfFromRDD1.show()

spark.stop()
