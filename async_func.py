from time import sleep
import pyodbc
import pymssql


def gevent_pyodbc():
    try:
        connect_str = 'DRIVER={{ODBC Driver 17 for SQL Server}};' \
            'DATABASE={db};SERVER={dsn};' \
            'UID=sa;PWD=MyP@ssw0rd'.format(dsn='mssql', db='TEST')
        with pyodbc.connect(connect_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SET NOCOUNT ON;
                    DECLARE @return_value int;
                    EXEC @return_value = [{}];
                    SELECT 'Return Value' = @return_value
                """.format('WAIT_PROC'))

        print('...finish ASYNC FUNCTION :)')
    except Exception as e:
        print('---------ERROR-------\n{}'.format(e))
        return -2


def gevent_pyodbc_with_sleep():
    """
    """
    sleep(0.1)
    try:
        connect_str = 'DRIVER={{ODBC Driver 17 for SQL Server}};' \
            'DATABASE={db};SERVER={dsn};' \
            'UID=sa;PWD=MyP@ssw0rd'.format(dsn='mssql', db='TEST')
        with pyodbc.connect(connect_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SET NOCOUNT ON;
                    DECLARE @return_value int;
                    EXEC @return_value = [{}];
                    SELECT 'Return Value' = @return_value
                """.format('WAIT_PROC'))

        print('...finish ASYNC FUNCTION :)')
    except Exception as e:
        print('---------ERROR-------\n{}'.format(e))
        return -2


def gevent_pymssql():
    try:
        with pymssql.connect(server='mssql', user='sa', password='MyP@ssw0rd', database='TEST') as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SET NOCOUNT ON;
                    DECLARE @return_value int;
                    EXEC @return_value = [{}];
                    SELECT 'Return Value' = @return_value
                """.format('WAIT_PROC'))

        print('...finish ASYNC FUNCTION :)')
    except Exception as e:
        print('---------ERROR-------\n{}'.format(e))
        return -2
