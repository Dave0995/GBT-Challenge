import sqlalchemy as sa

class SQLUtils:
    def __init__(self, db_uri: str):
        self.engine = sa.create_engine(db_uri)
    
    def __enter__(self):
        self.conn = self.engine.connect()
        return self

    def __exit__(self) -> None:
        self.conn.close()
