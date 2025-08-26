import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import logging
from scripts.database_connection import connect_to_database

logging.basicConfig(filename='training_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(db_path='database/DogImages.db'):
    try:
        df = connect_to_database(db_path)
        if df.empty:
            logging.error(f"No data loaded from {db_path}")
            raise ValueError(f"No data loaded from {db_path}")
        logging.info(f"Data loaded from {db_path} with {len(df)} records")
        print(f"Data loaded from {db_path} with {len(df)} records")
        df.to_csv('raw_data.csv', index=False)
        logging.info("Raw data saved to raw_data.csv")
        print("Raw data saved to raw_data.csv")
        return df
    except Exception as e:
        logging.error(f"Failed to load data from {db_path}: {e}")
        print(f"Failed to load data from {db_path}: {e}")
        raise e

if __name__ == "__main__":
    load_data()