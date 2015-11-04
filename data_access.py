#! /usr/bin/env python

import pyodbc
from sqlalchemy import create_engine, pool
from svc_utils import SvcUtils


class DataAccess(object):
    def __init__(self, db_connection_str):
        if db_connection_str is None:
            raise ReferenceError('Database connection string is NULL')

        self.connection_str = db_connection_str
        self.connection_pool = pool.QueuePool(self.create_connection, pool_size=10)
        self.engine = create_engine('mssql+pyodbc://', pool=self.connection_pool)

    def create_connection(self):
        try:
            connection = pyodbc.connect(self.connection_str)
            return connection
        except Exception as ex:
            raise Exception(SvcUtils.error_message('Database connection failed', {'error': ex}))
