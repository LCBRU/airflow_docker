# Airflow Docker

Docker compose configuration for Airflow.

## Documentation

### Docker Configuration

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

### Initialisation

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#initializing-environment

### MySQL Configuration

https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#setting-up-a-mysql-database

```sql
CREATE DATABASE {airflow_db} CHARACTER SET UTF8mb3 COLLATE utf8_general_ci
CREATE USER '{airflow_user}' IDENTIFIED BY '{airflow_pass}';
GRANT ALL PRIVILEGES ON {airflow_db}.* TO '{airflow_user}';
```
