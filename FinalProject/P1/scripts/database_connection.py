import sqlite3
import pandas as pd
import logging

logging.basicConfig(filename='training_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_database(db_path='database/DogImages.db'):
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT Breed, Image_File_Path FROM DogImages", conn)
        conn.close()
        if df.empty:
            logging.error(f"No data found in {db_path}")
            raise ValueError(f"No data found in {db_path}")
        logging.info(f"Successfully loaded metadata from {db_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to connect to database {db_path}: {e}")
        raise e