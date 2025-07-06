from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_scripts.sales_etl import final_transform

def run_etl():
    file_path = '/opt/airflow/data/sales_data_sample.csv'
    df = final_transform(file_path)
    print(df.head())

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'sales_etl_dag',
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args,
    description='Automated ETL pipeline example',
) as dag:

    etl_task = PythonOperator(
        task_id='run_sales_etl',
        python_callable=run_etl,
    )
