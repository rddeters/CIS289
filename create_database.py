"""
Program: create_database.py
Author: River Deters
Last date modified: 07/28/2023

The purpose of this program is to create the database for my Python II final project.
"""

import csv
import sqlite3
from sqlite3 import Error

# This function creates a database connection and database if it doesn't already exist
database = "2020_mens_vnl.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


sql_create_attackers_table = """ CREATE TABLE IF NOT EXISTS Attackers (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        spikes text,
                                        faults text,
                                        shots text,
                                        total_attempts text,
                                        success_percentage text
                                    ); """

sql_create_blockers_table = """ CREATE TABLE IF NOT EXISTS Blockers (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        stuff_blocks text,
                                        faults text,
                                        rebounds text,
                                        total_attempts text,
                                        average_per_set text
                                    ); """

sql_create_diggers_table = """ CREATE TABLE IF NOT EXISTS Diggers (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        digs text,
                                        faults text,
                                        reception text,
                                        total_attempts text,
                                        average_per_set text
                                    ); """

sql_create_receivers_table = """ CREATE TABLE IF NOT EXISTS Receivers (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        excellents text,
                                        faults text,
                                        serve_reception text,
                                        total_attempts text,
                                        efficiency_percentage text
                                    ); """

sql_create_servers_table = """ CREATE TABLE IF NOT EXISTS Servers (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        aces text,
                                        faults text,
                                        hits text,
                                        total_attempts text,
                                        average_per_set text
                                    ); """

sql_create_setters_table = """ CREATE TABLE IF NOT EXISTS Setters (
                                        rank text NOT NULL,
                                        shirt_number text,
                                        name text,
                                        team text,
                                        running_sets text,
                                        faults text,
                                        still_sets text,
                                        total_attempts text,
                                        average_per_set text
                                    ); """

# create a database connection and database if it doesn't already exist
conn = create_connection(database)


def process_csv_data(filename):
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = csv.DictReader(input_file)
        return [tuple(i.values()) for i in data]


# create a database connection and database if it doesn't already exist
database = "2020_mens_vnl.db"
# conn = create_connection(database)

# create tables
if conn is not None:
    table_definitions = {
        "Attackers": sql_create_attackers_table,
        "Blockers": sql_create_blockers_table,
        "Diggers": sql_create_diggers_table,
        "Receivers": sql_create_receivers_table,
        "Servers": sql_create_servers_table,
        "Setters": sql_create_setters_table
    }

    for table_name, create_table_sql in table_definitions.items():
        create_table(conn, create_table_sql)

        # Process CSV data and insert into the corresponding table
        csv_filename = f"men_best_{table_name.lower()}.csv"
        csv_data = process_csv_data(csv_filename)
        insert_query = f"REPLACE INTO {table_name} VALUES ({', '.join(['?'] * len(csv_data[0]))});"
        cur = conn.cursor()
        cur.executemany(insert_query, csv_data)
        conn.commit()

    conn.close()
else:
    print("Error! cannot create the database connection.")
