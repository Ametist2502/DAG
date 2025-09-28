# Using base image from Airflow
FROM apache/airflow:3.0.1-python3.9

# Move to user airflow
USER airflow

# Copy requirements.txt to container
USER root
COPY requirements.txt /opt/airflow/requirements.txt
RUN chown airflow: /opt/airflow/requirements.txt
USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
