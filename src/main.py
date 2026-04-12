import sqlite3
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schema.create_tables import create_tables
from seed.insert_data import insert_data
from queries.queries import run_queries

conn = sqlite3.connect("reliable_rentals.db")
conn.execute("PRAGMA foreign_keys = ON")

create_tables(conn)
insert_data(conn)
run_queries(conn)

conn.close()
print("\n✓ Done. Connection closed.")