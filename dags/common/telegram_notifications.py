from airflow.providers.telegram.operators.telegram import TelegramOperator
from datetime import datetime

CHAT_ID='-4826430719'

def create_telegram_message(context, status: str):
    if status == "success":
        message = (
            f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Task {context['task_instance'].task_id} success\n"
            f"DAG_ID {context['dag'].dag_id}\n"
            # f"Duration: {context['task_instance'].duration}"
        )
        return message

    if status == "fail":
        message = (
            f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Task {context['task_instance'].task_id} fail\n"
            f"DAG_ID {context['dag'].dag_id}\n"
            # f"Duration: {context['task_instance'].duration}\n"
            f"Log URL: {context['task_instance'].log_url}"
        )
        return message
    
def send_success_telegram_notification(context):
    message = create_telegram_message(context, "success")
    return TelegramOperator(
        task_id="notify_success",
        telegram_conn_id="telegram_conn",
        chat_id=CHAT_ID,
        text=message
    ).execute(context=context)

def send_fail_telegram_notification(context):
    message = create_telegram_message(context, "fail")
    return TelegramOperator(
        task_id="notify_failure",
        telegram_conn_id="telegram_conn",
        chat_id=CHAT_ID,
        text=message
    ).execute(context=context)

def task_fail_alert(context):
    return TelegramOperator(
        task_id="notify_failure",
        telegram_conn_id="telegram_conn",
        chat_id=CHAT_ID,
        text=f"❌ Task {context['task_instance'].task_id} failed in DAG {context['dag'].dag_id}"
    ).execute(context=context)


