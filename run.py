"""
run
~~~

This module runs the application.
"""
from gevent import monkey
monkey.patch_all()

from werkzeug.serving import run_with_reloader
from gevent.pywsgi import WSGIServer


from app import app

# if __name__ == '__main__':
#     run_with_reloader(lambda: WSGIServer(('127.0.0.1', 8080), app.wsgi_app).serve_forever())

if __name__ == '__main__':
    run_with_reloader(lambda: WSGIServer(('0.0.0.0', 8082), app.wsgi_app).serve_forever())
