import logging
from typing import Union, Dict, List

from pandas import DataFrame

from models.basic_models import HiredEmployees, Deparments, Jobs
from utils.sql import SQLUtils
from utils.logger import get_logger
from config import DB_URI

file_model: Dict[str, str] = {
    "hired_employees": HiredEmployees,
    "departments": Deparments,
    "jobs": Jobs,
}

logger = get_logger("models")

def save_records(records: List[Dict[str, str]]) -> None:
    with SQLUtils(DB_URI) as sql:
        sql.conn("query")


def records_validation(df: DataFrame, model: Union[HiredEmployees, Deparments, Jobs]) -> None:
    if not model:
        logger.error("Not recognized model")
        return None
    
    to_save: List[Dict[str, str]] = []

    for _, row in df.iterrows():
        try:
            record = model(**row.to_dict())
            to_save.append(record)
        except Exception as e:
            logger.error(e)
            logger.error(row.to_dict())
    
    save_records(to_save)
