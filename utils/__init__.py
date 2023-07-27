import pandas as pd
import sqlalchemy as sa

from config import DB_URI
from utils.sql import SQLUtils


def get_requested_data_ch1() -> pd.DataFrame:
    with SQLUtils(DB_URI) as sql:
        query = """
        SELECT 
            td.department,
            tj.job,
            EXTRACT(QUARTER FROM the.datetime) AS quarter,
            count(*)
        FROM
            test_hired_employees the
        JOIN
            test_departments td
        ON
            the.department_id = td.id
        JOIN 
            test_jobs tj
        ON
            the.job_id = tj.id
        WHERE
            EXTRACT(YEAR FROM the.datetime) = 2021
        GROUP BY 
            1, 2, 3
        ORDER BY
            1, 2
        """
        df = pd.read_sql(query, con=sql.conn)

    return df


def get_requested_data_ch2() -> pd.DataFrame:
    with SQLUtils(DB_URI) as sql:
        query = """
        SELECT 
            the.department_id,
            td.department,
            count(*) as hired
        FROM
            test_hired_employees the
        JOIN
            test_departments td
        ON
            the.department_id = td.id
        WHERE
            EXTRACT(YEAR FROM the.datetime) = 2021
        GROUP BY
            1, 2
        ORDER BY 
            3 DESC
        """
        df = pd.read_sql(query, con=sql.conn)
    
    return df