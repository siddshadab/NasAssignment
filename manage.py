#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3
from sqlite3 import Error
import environ

from NasAssesment.settings import BASE_DIR

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_task(conn,id):
    #insert if record not exist
   sql = 'INSERT INTO restApi_slotMaster (id) SELECT ' +str(id) + ' WHERE NOT EXISTS (SELECT * FROM restApi_slotMaster WHERE id ='+str(id)+');'
   print(id)
   print(sql)
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()


def main():
    """Run administrative tasks."""

    database = BASE_DIR / 'db.sqlite3'
    print(database)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NasAssesment.settings')
    conn = create_connection(database)
    # Handle for first run
    env = environ.Env()
    env.read_env(env.str('BASE_DIR', '.env'))
    SLOT_NUMBER = env('SLOT_NUMBER')

    try:
        with conn:
            for x in range(int(SLOT_NUMBER)):
                #Take range from property file later
                update_task(conn,x + 1)
    except:
        print("An exception occurred On first Time Server Run")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
