# Docker-PokeAPI-Postgres-DataIntegration

## Pokemon Clustering End-to-End Pipeline

Proyek ini mendemonstrasikan pipeline data otomatis yang melakukan ekstraksi data Pokemon, pemrosesan clustering menggunakan Machine Learning (K-Means), dan visualisasi data secara real-time.

--------------------------------------------------------------------------------------------------------------------
## Project Result Showcase

<img width="2548" height="1560" alt="merged_all_project" src="https://github.com/user-attachments/assets/87b795b9-0dce-44ac-98a7-51b0dc1cc29e" />

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

Airflow: Mengatur jadwal (scheduling) task dari ingestion hingga clustering.

PostgreSQL: Terdiri dari dua database utama:

airflow_metadata: Menyimpan konfigurasi internal Airflow.

pokemon_db: Menyimpan data mentah dan hasil clustering.

K-Means Engine: Script Python yang melakukan scaling fitur dan segmentasi Pokemon berdasarkan statistik mereka (HP, Attack, Defense, dll).

--------------------------------------------------------------------------------------------------------------------

## Project Structure

<img width="1048" height="372" alt="image" src="https://github.com/user-attachments/assets/5a928282-3690-406b-a14a-2556d55ea740" />
