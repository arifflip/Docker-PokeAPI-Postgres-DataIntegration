from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
import os

from script.pokeAPI_fetch_function import *
from airflow.providers.postgres.hooks.postgres import PostgresHook

## --------------------------------
#  Functions
#$ --------------------------------

def get_pokemon_data() :
    
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    
    if response.status_code == 200:        
        
        dataset_pokemon_gen_1=get_dataset_information(151)
        dataset_pokemon_gen_1.to_csv("/opt/airflow/logs/temp_dataset_pokemon_gen1.csv")

    else :
        raise Exception("Gagal narik data dari PokeAPI!")

def get_postgres_engine():
    try:
        hook = PostgresHook(postgres_conn_id='my_postgres_conn')
        
        engine = hook.get_sqlalchemy_engine()
        
        logging.info("Koneksi ke Postgres via Hook Berhasil!")
        return engine
    except Exception as e:
        logging.error(f"Gagal narik koneksi: {e}")
        raise

def upload_data_to_db():

    #read data csv dari log folder
    path = ti.xcom_pull(task_ids='fetch_data_from_pokeAPI')
    df = pd.read_csv(path)
    
    #get engine
    engine = get_postgres_engine()

    #write to table
    table_name-"pokemon_gen_table"
    df.to_sql(f"{table_name}", engine, if_exists='overwrite', index=False)
    print("Berhasil diwrite ke {tbla_name}")

## --------------------------------
#  DAG
#$ --------------------------------

with DAG(
    dag_id='pokeapi_to_postgres_ingestion',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='fetch_data_from_pokeAPI',
        python_callable=get_pokemon_data
    )

    task2 = PythonOperator(
        task_id='load_to_postgres',
        python_callable=upload_data_to_db
    )

## --------------------------------
#  Dependecies
#$ --------------------------------

task1 >> task2