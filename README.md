uwsgi_gevent_pyodbc
=========================
Repository to prove uWSGI + gevent + pyodbc delay issue.

Running flask application with uWSGI using gevent + pyodbc caused a delayed response. However running without uwsgi doesn't caused any delay.

The process waits for the end of the greenlet task to return response. Use a time.sleep in the asynchronous function can be a workaround to this issue.

python 3.6/uwsgi 2.0.17.1/gevent 1.2.1

-------------


## Requirements

- [docker-compose](https://docs.docker.com/compose/install/) (Running with 1.21.2)


## How to test

```
cd /path/to/uwsgi_event_pyodbc
docker-compose up
docker exec -it container_name bash
cd /app

python run.py #running without uwsgi
uwsgi uwsgi.ini #running with uwsgi
```

Then, using CURL/POSTMAN

```
# execute using pyodbc
curl http://0.0.0.0:8082/gevent/pyodbc

# execute using pyodbc with a sleep
curl http://0.0.0.0:8082/gevent/pyodbc/sleep

# execute using pymssql
curl http://0.0.0.0:8082/gevent/pymssql
```


RESPONSE USING uwsgi:
```
curl http://0.0.0.0:8082/gevent/pyodbc

Api's log:

---- START EXEC ASYNC
-----RETURNING
...finish ASYNC FUNCTION :)
[pid: 339|app: 0|req: 4/4] 172.24.0.1 () {28 vars in 319 bytes} [Thu Oct 25 13:16:18 2018] GET /gevent/pyodbc => generated 3 bytes in 5064 msecs (HTTP/1.1 200) 2 headers in 70 bytes (4 switches on core 99)


curl http://0.0.0.0:8082/gevent/pyodbc/sleep

Api's log:

---- START EXEC ASYNC
-----RETURNING
[pid: 339|app: 0|req: 5/5] 172.24.0.1 () {28 vars in 331 bytes} [Thu Oct 25 13:17:05 2018] GET /gevent/pyodbc/sleep => generated 3 bytes in 1 msecs (HTTP/1.1 200) 2 headers in 70 bytes (4 switches on core 99)
...finish ASYNC FUNCTION :)



curl http://0.0.0.0:8082/gevent/pymssql

Api's log:

---- START EXEC ASYNC
-----RETURNING
[pid: 339|app: 0|req: 6/6] 172.24.0.1 () {28 vars in 320 bytes} [Thu Oct 25 13:17:39 2018] GET /gevent/pymssql => generated 3 bytes in 7 msecs (HTTP/1.1 200) 2 headers in 70 bytes (4 switches on core 99)
...finish ASYNC FUNCTION :)

```
