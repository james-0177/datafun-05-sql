# Import from Python Standard Library first
import sqlite3
import pathlib
import logging

# Import from external packages
import pandas as pd

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths using joinpath
db_filepath = pathlib.Path("project.db")
sql_file_insert = pathlib.Path("sql").joinpath("insert_records.sql")
sql_file_update = pathlib.Path("sql").joinpath("update_records.sql")
sql_file_delete = pathlib.Path("sql").joinpath("delete_records.sql")
sql_file_qagg = pathlib.Path("sql").joinpath("query_aggregation.sql")
sql_file_qfilter = pathlib.Path("sql").joinpath("query_filter.sql")
sql_file_qsort = pathlib.Path("sql").joinpath("query_sorting.sql")
sql_file_qgroup = pathlib.Path("sql").joinpath("query_group.sql")
sql_file_qjoin = pathlib.Path("sql").joinpath("query_join.sql")


# Insert records
def execute_sql_insert(db_filepath, sql_file_insert):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_insert, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_insert}")

# Update records
def execute_sql_update(db_filepath, sql_file_update):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_update, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_update}")

# Delete records
def execute_sql_delete(db_filepath, sql_file_delete):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_delete, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_delete}")

# Query aggregate
def execute_sql_qagg(db_filepath, sql_file_qagg):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_qagg, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_qagg}")

# Query filter
def execute_sql_qfilter(db_filepath, sql_file_qfilter):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_qfilter, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_qfilter}")

# Query sort
def execute_sql_qsort(db_filepath, sql_file_qsort):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_qsort, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_qsort}")

# Query group
def execute_sql_qgroup(db_filepath, sql_file_qgroup):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_qgroup, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_qgroup}")

# Query join
def execute_sql_qjoin(db_filepath, sql_file_qjoin):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file_qjoin, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file_qjoin}")


def main():
    logging.info("Program started")
    ...

    # Perform SQL operations on database
    execute_sql_insert(db_filepath, sql_file_insert)
    execute_sql_update(db_filepath, sql_file_update)
    execute_sql_delete(db_filepath, sql_file_delete)
    execute_sql_qagg(db_filepath, sql_file_qagg)
    execute_sql_qfilter(db_filepath, sql_file_qfilter)
    execute_sql_qsort(db_filepath, sql_file_qsort)
    execute_sql_qgroup(db_filepath, sql_file_qgroup)
    execute_sql_qjoin(db_filepath, sql_file_qjoin)  

    logging.info("All SQL operations completed successfully")
    logging.info("Program ended")

# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()
