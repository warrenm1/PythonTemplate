#! /usr/bin/python3

import sqlite3

from src.Enums import SQLiteTableValues

class SQLite(object):
    # Variables #
    connection = None
    database = None

    # ClassMethods #
    @classmethod
    def connect(cls, path: str):
        '''
            Ensures the database is created if it doesn't exist
            Sotres the database path

            :type path: str
            :param path: path to the database
        '''
        cls.database = path
        cls.connection = sqlite3.connect(database=cls.database)
        cls.connection.close()

    @classmethod
    def createTable(cls, tableName: str):
        '''
            Creates a table in the database

            :type tableName: str
            :param tableName: name of the table to be created in the database
        '''
        cls.connection = sqlite3.connect(database=cls.database)

        command = f'CREATE TABLE {tableName} ('
        command += ', '.join(list(map(lambda c: f'{c.name} {c.value}', SQLiteTableValues)))
        command += ')'

        cls.connection.execute(command)

        cls.connection.commit()
        cls.connection.close()

    @classmethod
    def doesTableExist(cls, table: str) -> bool:
        '''
            Determine whether or not a given table exists within the database

            :type table: str
            :param table: name of the table being checked of its existence

            :rtype: bool
            :returns: whether or not the table exists in the database
        '''
        cls.connection = sqlite3.connect(database=cls.database)
        tables = cls.connection.execute(sql=f"SELECT tbl_name WHERE type='table' and tbl_nam'{table}'").fetchall()

        cls.connection.close()
        return tables == []
