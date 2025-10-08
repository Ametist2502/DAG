from airflow.utils.state import State

def check_tasks_status(dag_run, task_ids=None, task_group_ids=None):
    """
    Kiểm tra trạng thái của các task cụ thể hoặc tất cả sub-task trong các task group truyền vào.
    Args:
        dag_run (DagRun): phiên làm việc của DAG
        task_ids (list[str], optional): danh sách các task id cần check riêng lẻ
        task_group_ids (list[str], optional): danh sách các group_id prefix task để check tất cả subtasks bên trong
    Returns:
        dict: {task_id: state}, trạng thái các task được check
    """
    checked_tasks = {}

    for ti in dag_run.get_task_instances():
        # Kiểm tra task id riêng lẻ
        if task_ids and ti.task_id in task_ids:
            checked_tasks[ti.task_id] = ti.current_state()
            continue
        
        # Kiểm tra tất cả task trong các group được truyền
        if task_group_ids and any(ti.task_id.startswith(f"{group_id}.") for group_id in task_group_ids):
            checked_tasks[ti.task_id] = ti.current_state()

    # Nếu không truyền gì thì trả tất cả task trạng thái
    if not task_ids and not task_group_ids:
        for ti in dag_run.get_task_instances():
            checked_tasks[ti.task_id] = ti.current_state()

    return checked_tasks
