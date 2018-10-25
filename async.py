# -*- coding: utf-8 -*-

"""
    This module handles asynchronous executions.
"""

from gevent import spawn, socket
from flask import copy_current_request_context
import pymssql


def wait_callback(read_fileno):
    socket.wait_read(read_fileno)


pymssql.set_wait_callback(wait_callback)


def exec_async(func, *args, **kwargs):
    """
        Executes a function asynchronously by spawning a new greenlet, and ensures this function has access to
        the current request context.

        :param func: Function to execute asynchronously
        :type func: function
    """

    @copy_current_request_context
    def func_with_context(*f_args, **f_kwargs):
        func(*f_args, **f_kwargs)

    # spawn a greenlet
    g = spawn(func_with_context, *args, **kwargs)

    return g
