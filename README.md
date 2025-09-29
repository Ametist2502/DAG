# DAG
This folder will update DAG script of Airflow for Personal Project

## Cách sử dụng airflow bằng docker
Cách 1
----
1. Chúng ta sẽ sử dụng trực tiếp image có sẵn của airflow trên Docker Hub pull về và thêm file .env để chạy.
2. Thêm các plugins vào biến trong file requirement để khi chạy docker compose chúng sẽ cài trực tiếp cùng
3. Tiếp đến mình có dùng git-sync để chúng tự động syn code từ repo github về. Các bạn có thể tham khảo repo này để hiểu cách sử dụng hơn: [REPO](https://github.com/data-burst/airflow-git-sync)

Cách 2
---
1. Chúng ta sẽ build 1 Dockerfile để install các plugins trước rồi dùng chính image đã build đó và docker-compose để dựng Airflow
2. Sau đó sẽ tiếp dùng follow bước 3 bên trên để cài git-sync nếu mong muốn chúng tự động update folder dags


