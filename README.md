Upload input.txt to HDFS

```
hadoop fs -put /path/to/input.txt hdfs://localhost:8020/data/input.txt

```

Run spark job

```
docker exec -it spark-master bash
spark-submit --master spark://spark-master:7077 /opt/spark-apps/word_count.py
```
