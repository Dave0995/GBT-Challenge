import tempfile

import pandas as pd
from google.cloud import storage


class GCPUtils:
    
    def __init__(self, bucket_name: str, prefix: str) -> None:
        self._bucket_name = bucket_name
        self._prefix = prefix
        self._client = storage.Client()
        self.bucket = self._client.bucket(self._bucket_name)
    
    def get_blob(self, file_name: str, date: str) -> storage.Blob:
        blob_name = f"{self._prefix}/{file_name}/{file_name}_{date}.csv"
        return self.bucket.blob(blob_name)
    
    def create_df(self, file_name: str, date: str):
        blob = self.get_blob(file_name, date)
        with tempfile.NamedTemporaryFile() as tmp_file:
            file = tmp_file.name
            blob.download_to_filename(file)
            return pd.read_csv(file)
