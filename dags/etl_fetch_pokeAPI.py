from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

from script.pokeAPI_fetch_function import *
from airflow.providers.postgres.hooks.postgres import PostgresHook

## --------------------------------
#  Functions
#$ --------------------------------

def get_pokemon_data() :
    
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    
    if response.status_code == 200:        
        
        dataset_pokemon_gen_1=get_dataset_information(2)
        dataset_pokemon_gen_1.to_csv("/opt/airflow/logs/temp_dataset_pokemon_gen1.csv")

    else :
        raise Exception("Gagal narik data dari PokeAPI!")

def get_postgres_engine():
    
    hook = PostgresHook(postgres_conn_id='postgre_database_airflow')
    conn = hook.get_connection('postgre_database_airflow')
    
    # 2. Ambil data mentah tanpa embel-embel 'extra'
    user = conn.login
    password = conn.password
    host = conn.host
    port = conn.port or 5432
    db = conn.schema

    # 3. Rakit URI (Clean & Proper)
    uri = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    
    # 4. Create Engine
    return create_engine(uri)

    #user = os.getenv('DB_USER')
    #password = os.getenv('DB_PASSWORD')
    #host = "postgres-db"
    #db = os.getenv('DB_NAME')
    #port = "5432"
    
    conn_uri = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(conn_uri)

"""    try:
        hook = PostgresHook(postgres_conn_id='postgre_database_airflow')
        
        engine = hook.get_sqlalchemy_engine()
        
        print("Koneksi ke Postgres via Hook Berhasil!")
        conn_uri = hook.get_uri()
        if conn_uri.startswith("postgres://"):
            conn_uri = conn_uri.replace("postgres://", "postgresql://", 1)

        engine = create_engine(conn_uri)        
        return engine
    except Exception as e:
        print(f"Gagal narik koneksi: {e}")
        raise
"""
def upload_data_to_db():

    #read data csv dari log folder
    path = "/opt/airflow/logs/temp_dataset_pokemon_gen1.csv"
    df = pd.read_csv(path)
    
    #get engine
    engine = get_postgres_engine()

    #write to table
    table_name="pokemon_gen_1"
    df.to_sql(f"{table_name}", engine, if_exists='replace', index=False)
    print("Berhasil diwrite ke {table_name}")

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