import pandas as pd
import sqlite3
import os

excel_file = "database/dog_images_data_table.xls"
db_path = "database/DogImages.db"

df = pd.read_excel(excel_file)

df.columns = df.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)

df.to_sql('DogImages', conn, if_exists='replace', index=False)

conn.close()

print(f"Data imported successfully into {db_path}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT * FROM DogImages LIMIT 5")
print("\nFirst 5 rows of DogImages table:")
for row in cursor.fetchall():
    print(row)
conn.close()