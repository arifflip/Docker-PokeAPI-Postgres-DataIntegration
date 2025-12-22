FROM apache/airflow:2.7.1

#copy requiremtnt to containert volue
COPY ./airflow/requirements.txt /requirements.txt

#run pip install to install libraries
RUN pip install --no-cache-dir -r /requirements.txt