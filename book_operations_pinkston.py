# Import from Python Standard Library first
import sqlite3
import pathlib
import logging

# Import from external packages
import pandas as pd

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql")

def execute_sql_from_file(db_filepath, sql_file):
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
            print(f"Executed SQL from {sql_file}")
    except (sqlite3.Error, FileNotFoundError) as e:
        error_message = f"Error executing SQL from {sql_file}: {e}"
        logging.error(error_message)
        print(error_message)

def main():

    sql_file = [
        sql_file_path.joinpath("insert_records.sql"),
        sql_file_path.joinpath("insert_books.sql"),
        sql_file_path.joinpath("update_records.sql"),
        sql_file_path.joinpath("delete_records.sql"),
        sql_file_path.joinpath("query_aggregation.sql"),
        sql_file_path.joinpath("query_filter.sql"),
        sql_file_path.joinpath("query_sorting.sql"),
        sql_file_path.joinpath("query_group.sql"),
        sql_file_path.joinpath("query_join.sql"),
    ]

    # Perform SQL operations on database
    execute_sql_from_file(db_file_path, sql_file)  

# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()
