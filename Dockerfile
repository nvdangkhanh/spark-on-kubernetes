FROM erkansirin78/spark-py:3.1.1
USER root

WORKDIR /app
COPY ./jars/* /opt/spark/jars
COPY ./spark-jobs-1.0-jar-with-dependencies.jar /app/spark-jobs.jar