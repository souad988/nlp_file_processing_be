import psycopg2
from psycopg2 import sql
from db_config import Base, engine,DB_PASSWORD,DB_USER,DB_NAME,DB_HOST

# Connect to the default database
def create_database_if_not_exists():
    conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [DB_NAME])
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database_if_not_exists()
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
