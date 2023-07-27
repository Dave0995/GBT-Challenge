from typing import Dict

from utils.secrets import SecretsManager


PROJECT_ID = "build-project-394105"

secrets_manager = SecretsManager(PROJECT_ID)

gcp_config: Dict[str, str] = {
    "bucket_name": "data-lake-dave-1",
    "prefix": "datasets",
}

MYSQL_HOST = secrets_manager.get_secret("MYSQL_HOST")
MYSQL_PORT = secrets_manager.get_secret("MYSQL_PORT")
MYSQL_USER = secrets_manager.get_secret("MYSQL_USER")
MYSQL_PASSWORD = secrets_manager.get_secret("MYSQL_PASSWORD")
MYSQL_SCHEMA = secrets_manager.get_secret("MYSQL_SCHEMA")

DB_URI = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_SCHEMA}"