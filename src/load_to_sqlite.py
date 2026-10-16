import sqlite3
import pandas as pd

CSV_PATH = "data/loans_2013_2015.csv"
DB_PATH = "data/lending_club.db"

conn = sqlite3.connect(DB_PATH)
first = True

for chunk in pd.read_csv(CSV_PATH, chunksize=100_000, low_memory=False):
    # "default" is a reserved word in SQL, so rename it to avoid headaches
    chunk = chunk.rename(columns={"default": "is_default"})
    chunk.to_sql("loans", conn, if_exists="replace" if first else "append", index=False)
    first = False

conn.execute("CREATE INDEX idx_loans_grade ON loans(grade)")
conn.execute("CREATE INDEX idx_loans_purpose ON loans(purpose)")
conn.commit()

print(pd.read_sql_query("SELECT COUNT(*) AS n FROM loans", conn))
conn.close()