# -*- coding: utf-8 -*-
"""Custom file server."""
import configparser
import os
from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer

from logger import get_logger

LOGGER = get_logger()


def get_base_dir():
    """
    Function to get the base directory.

    :param: None
    :return: str
        Path of base directory.
    """
    return os.path.abspath(os.path.dirname(__file__))


# pylint: disable=broad-except,invalid-name
class RequestsHandler(BaseHTTPRequestHandler):
    """Request handler class."""

    BASE_PATH = None
    PORT = None

    def do_GET(self):
        """
        Method to handle 'GET'.

        :return: None
        """
        LOGGER.info(self.path)
        path = RequestsHandler.BASE_PATH + self.path
        if not os.path.abspath(path).startswith(RequestsHandler.BASE_PATH):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Not authorized')
        elif os.path.isdir(path):
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(os.listdir(path)).encode())
            except Exception:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'error')
        else:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
            # error handling skipped
            except Exception:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Error')


def start_server():
    """
    Helper function to start the server.

    :return: None
    """
    os.environ['basedir'] = get_base_dir()
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['basedir'], 'cfgs', 'default.cfg'))
        RequestsHandler.PORT = int(config['DEFAULT']['http_server_port'])
        RequestsHandler.BASE_PATH = config['DEFAULT']['base_path']
    except Exception:  # pylint: disable=broad-except
        RequestsHandler.PORT = 8888
        RequestsHandler.BASE_PATH = '/tmp'
    httpd = TCPServer(('', RequestsHandler.PORT), RequestsHandler)
    LOGGER.info('Server started on %s', RequestsHandler.PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    start_server()
