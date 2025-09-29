from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from common.telegram_notifications import send_fail_telegram_notification, send_success_telegram_notification

default_args = {
    'owner': 'ametist',
    'email_on_retry': False,
    'on_failure_callback': send_fail_telegram_notification,  # Alert on failure
    'on_success_callback': send_success_telegram_notification   # Alert on success
}

with DAG(
    "example_dag",
    start_date=datetime(2025, 9, 29),
    schedule=None,
    catchup=False,
) as dag:

    hello = PythonOperator(
        task_id="hello_task",
        python_callable=lambda: print("Hello Airflow"),
        on_success_callback=send_success_telegram_notification,
        on_failure_callback=send_fail_telegram_notification,
    )
