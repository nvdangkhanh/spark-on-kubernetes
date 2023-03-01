FROM erkansirin78/spark-py:3.1.1
USER root
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY spark_on_k8s_app.py .
