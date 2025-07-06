# End-to-End Data Pipeline with Airflow, Python, and BigQuery

This project demonstrates a fully automated, end-to-end data pipeline designed to process and analyze e-commerce sales data. The pipeline extracts raw CSV data, performs data cleaning and transformations using Python, and loads the processed data into Google BigQuery for advanced SQL analysis. The entire workflow is orchestrated using Apache Airflow to ensure automation, scheduling, and reliability.

## 💡 Objectives

- Showcase hands-on data engineering skills using modern tools.
- Transform messy sales data into business-ready insights.
- Automate data workflows for reproducible, scalable analytics.

## ⚙️ Tech Stack

- **Python**: Data cleaning, transformation scripts.
- **Apache Airflow**: Workflow orchestration and scheduling.
- **Google BigQuery**: Cloud-based data warehouse for analytics.
- **SQL**: Advanced analysis and reporting.
- **Pandas**: Data manipulation in Python.

## 🚀 Project Structure

.
├── dags/
│ └── sales_etl_dag.py # Airflow DAG definition
├── etl_scripts/
│ └── sales_etl.py # ETL Python functions
├── data/
│ └── sales_data_sample.csv # Sample e-commerce data
├── sql/
│ └── example_queries.sql # BigQuery analysis queries & views
├── README.md






## 🛠️ Features

- **Automated ETL pipeline**: Clean, transform, and enrich raw sales data.
- **Airflow orchestration**: Schedule and manage ETL workflows as DAGs.
- **BigQuery integration**: Store and analyze data efficiently at scale.
- **Reusable SQL views**: Create summary views for business reporting.

## 📄 Example SQL Queries

- Total sales by city and product.
- Partitioned queries for faster filtering by date.
- Creation of reusable summary views for dashboards.

## ⚡ How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/anushreepatil031/data-pipeline-airflow-bigquery.git
    ```
2. Place your data file in the `data/` folder (or use provided sample).
3. Update `file_path` in `sales_etl_dag.py` to point to your local CSV.
4. Start Airflow webserver and scheduler to run the pipeline.
5. Use BigQuery to execute analysis queries from the `sql/` folder.

## ✅ Outcomes

- Cleaned and enriched sales data ready for analytics.
- Automated pipeline reduces manual effort and errors.
- Scalable architecture for future data growth and more complex workflows.



