import sqlite3

from wms2B.data.task import Task


class Database:

    def __init__(self, name):
        self._conn = sqlite3.connect(name, check_same_thread=False)
        self._cursor = self._conn.cursor()

        #Example tasks
        emp_1 = Task('1', 'Have a shower')
        emp_2 = Task('2', 'Henry')

        ##initialize tables
        self._cursor.execute("""CREATE TABLE Task (
                     created text,
                     content text
             )""")
        self._cursor.execute("INSERT INTO Task VALUES (?, ? )", (emp_1.created, emp_1.content))
        self._cursor.execute("INSERT INTO Task VALUES (:first, :last)",
                  {"first": emp_2.created, "last": emp_2.content})

        self._cursor.execute("""CREATE TABLE Activity (
                     created text,
                     activity_name text,
                     activity_subtype text,
                     start_time text,
                     stop_time text,
                     task_nature text,
                     hours_expended text
                     
             )""")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()