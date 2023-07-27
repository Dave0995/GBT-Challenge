from fastapi import FastAPI

import utils
from utils.gcp import GCPUtils
from config import gcp_config
from models import file_model, records_validation


app = FastAPI()


@app.post('/process_file')
def ingestion_process(file_name: str, date: str):
    gcp = GCPUtils(
        bucket_name=gcp_config['bucket_name'],
        prefix=gcp_config['prefix'],
    )
    df = gcp.create_df(file_name, date)
    records_validation(df, file_model.get(file_name, None))


@app.get('/hired_employees_by_department')
def hired_employees_by_department():
    df = utils.get_requested_data_ch1()


@app.get('/rank_hired_employees')
def rank_hired_employees():
    df = utils.get_requested_data_ch2()
