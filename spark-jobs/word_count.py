from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read the input file from HDFS
input_data = spark.read.text("hdfs://hadoop-namenode:8020/data/input.txt").rdd

# Split each line into words and count them
word_counts = input_data.flatMap(lambda line: line.value.split(" ")) \
                        .map(lambda word: (word, 1)) \
                        .reduceByKey(lambda a, b: a + b)

# Show the result
output = word_counts.collect()
for word, count in output:
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()
