# Docker-PokeAPI-Postgres-DataIntegration

## Pokemon Clustering End-to-End Pipeline

Proyek ini mendemonstrasikan pipeline data otomatis yang melakukan ekstraksi data Pokemon, pemrosesan clustering menggunakan Machine Learning (K-Means), dan visualisasi data menggunakan Looker Studio.

--------------------------------------------------------------------------------------------------------------------
## Project Result Showcase

<img width="3278" height="819" alt="image (3)" src="https://github.com/user-attachments/assets/15af1a05-95c3-408b-bf53-1da4a2e74e97" />

<img width="2872" height="1075" alt="dashboard_pokemon_merged" src="https://github.com/user-attachments/assets/96411ccb-11ff-429c-8a9a-7b04401d6db8" />

pokemon clutering result dashboard url : https://lookerstudio.google.com/reporting/9573a5c4-3510-4a1d-9a05-97f1aa8b5359/page/zY7iF

--------------------------------------------------------------------------------------------------------------------
## Tech Stack


Orchestration: Apache Airflow

Containerization: Docker & Docker Compose

Database: PostgreSQL (Metadata & Results Storage)

Language: Python 3.x

Data Processing: Pandas, Scikit-Learn (K-Means Clustering)

Visualization: Looker Studio

--------------------------------------------------------------------------------------------------------------------

## Architecture
Pipeline ini berjalan di atas Docker dengan arsitektur sebagai berikut:

Airflow: Mengatur jadwal (scheduling) fetch data dan ingestion ke postgre

PostgreSQL: Terdiri dari dua database utama:

airflow_metadata: Menyimpan konfigurasi internal Airflow.

pokemon_db: Menyimpan data mentah dan hasil clustering.

K-Means Engine: Script Python yang melakukan scaling fitur dan segmentasi Pokemon berdasarkan statistik mereka (HP, Attack, Defense, dll).

--------------------------------------------------------------------------------------------------------------------

## Project Structure

<img width="1048" height="372" alt="image" src="https://github.com/user-attachments/assets/5a928282-3690-406b-a14a-2556d55ea740" />
