from flask import Flask, jsonify

from async_func import (
    gevent_pyodbc,
    gevent_pyodbc_with_sleep,
    gevent_pymssql
)
from async import exec_async

__app_name__ = 'test'

app = Flask(__name__)


@app.route('/gevent/pyodbc', methods=['GET'])
def get_gevent_pyodbc():

    print('---- START EXEC ASYNC')
    exec_async(gevent_pyodbc)
    print('-----RETURNING')
    return jsonify({})


@app.route('/gevent/pyodbc/sleep', methods=['GET'])
def get_gevent_pyodbc_with_sleep():

    print('---- START EXEC ASYNC')
    exec_async(gevent_pyodbc_with_sleep)
    print('-----RETURNING')
    return jsonify({})


@app.route('/gevent/pymssql', methods=['GET'])
def get_gevent_with_pymssql():

    print('---- START EXEC ASYNC')
    exec_async(gevent_pymssql)
    print('-----RETURNING')
    return jsonify({})
