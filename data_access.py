#! /usr/bin/env python

from model import Message, User
from sqlalchemy import create_engine, pool
from svc_utils import SvcUtils
import pyodbc


class DataAccess(object):
    def __init__(self, db_connection_str):
        if db_connection_str is None:
            raise ReferenceError('database connection string is NULL')

        self.connection_str = db_connection_str
        self.connection_pool = pool.QueuePool(self.create_connection, pool_size=1)
        self.engine = create_engine('mssql+pyodbc://', pool=self.connection_pool)

    def create_connection(self):
        try:
            connection = pyodbc.connect(self.connection_str)
            return connection
        except Exception as ex:
            raise Exception(SvcUtils.error_message('database connection failed', {'error': ex.message}))

    def get_user_id_by_username(self, username):
        user_id = 0
        statement = 'SELECT id FROM [user] WITH (NOLOCK) WHERE username = ?'

        try:
            result = self.engine.execute(statement, [username]).fetchone()

            if result is not None:
                user_id = result.id

        except Exception as ex:
            raise Exception(SvcUtils.error_message('user lookup failed', {'username': username, 'error': ex.message}))

        return user_id

    def get_user_by_id(self, user_id):
        user = None
        statement = 'SELECT id, username, created_date_utc FROM [user] WITH (NOLOCK) WHERE id = ?'

        try:
            result = self.engine.execute(statement, [user_id]).fetchone()

            if result is not None:
                user = User(id=result.id, username=result.username, created_date_utc=result.created_date_utc)

        except Exception as ex:
            raise Exception(SvcUtils.error_message('user lookup failed', {'user ID': user_id, 'error': ex.message}))

        return user

    def get_user_by_username(self, username):
        user = None
        statement = 'SELECT id, username, created_date_utc FROM [user] WITH (NOLOCK) WHERE username = ?'

        try:
            result = self.engine.execute(statement, [username]).fetchone()

            if result is not None:
                user = User(id=result.id, username=result.username, created_date_utc=result.created_date_utc)

        except Exception as ex:
            raise Exception(SvcUtils.error_message('user lookup failed', {'username': username, 'error': ex.message}))

        return user
    
    def get_message_by_id(self, message_id):
        message = None
        statement = 'SELECT id, [user_id], [text], expiration_date_utc, created_date_utc FROM [message] WITH (NOLOCK) WHERE [message].id = ?'

        try:
            result = self.engine.execute(statement, message_id).fetchone()

            if result is not None:
                message = Message(id=result.id, user_id=result.user_id, text=result.text, expiration_date_utc=result.expiration_date_utc, created_date_utc=result.created_date_utc)

        except Exception as ex:
            raise Exception(SvcUtils.error_message('message lookup failed', {'id': message_id, 'error': ex.message}))

        return message

    def get_messages_by_username(self, username):
        messages = []
        statement = '''
            SELECT	msg.id, msg.[user_id], [text], expiration_date_utc, msg.created_date_utc
            FROM	[message] msg WITH (NOLOCK)
                    JOIN [user] usr WITH (NOLOCK) ON usr.[id] = msg.[user_id]
            WHERE	usr.username = ?'''

        try:
            result = self.engine.execute(statement, username).fetchall()

            if result is not None:
                for row in result:
                    messages.append(Message(id=row.id, user_id=row.user_id, text=row.text, expiration_date_utc=row.expiration_date_utc, created_date_utc=row.created_date_utc))

        except Exception as ex:
            raise Exception(SvcUtils.error_message('message lookup failed', {'id': username, 'error': ex.message}))

        return messages

    def save_user(self, username):
        user_id = 0
        statement = 'INSERT INTO [user](username) VALUES (?)'

        try:
            self.engine.execute(statement, [username])
            result = self.engine.execute('SELECT CAST(@@IDENTITY AS BIGINT) AS [user_id]').fetchone()

            if result is not None:
                user_id = result.user_id

        except Exception as ex:
            raise Exception(SvcUtils.error_message('user insert failed', {'username': username, 'error': ex.message}))

        return user_id

    def save_message(self, user_id, message, expiration_date_utc):
        message_id = 0
        statement = 'INSERT INTO [message]([user_id], [text], expiration_date_utc) VALUES (?, ?, ?)'

        try:
            self.engine.execute(statement, [user_id, message, expiration_date_utc])
            result = self.engine.execute('SELECT CAST(@@IDENTITY AS BIGINT) AS message_id').fetchone()

            if result is not None:
                message_id = result.message_id

        except Exception as ex:
            raise Exception(SvcUtils.error_message('message insert failed', {'user_id': user_id, 'message': message, 'expiration_date_utc': expiration_date_utc, 'error': ex.message}))

        return message_id
