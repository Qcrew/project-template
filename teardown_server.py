""" """

import time

import Pyro5.api as pyro
from qcore import Server

if __name__ == "__main__":
    with pyro.Proxy(Server.URI) as server:
        server.teardown()
    time.sleep(2)
