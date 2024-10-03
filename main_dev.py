import ast
import os
import signal
import subprocess
import sys
import threading

import uvicorn
from fastapi import FastAPI
from testcontainers.postgres import PostgresContainer


def run_informed_server(app: FastAPI, host: str, port: int):
    uvicorn.run(app, host=host, port=port, log_config=None, log_level="debug")


def start_server(db_connection_string: str) -> None:
    print(f"db_connection_string: {db_connection_string}")


def signal_handler(signum, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:

        with PostgresContainer(
            "postgres:latest", driver=None
        ).with_bind_ports(
            5432, 5432
        ) as postgres:

            db_connection_string = postgres.get_connection_url()
            os.environ["DATABASE_CONFIG__DB_URL"] = db_connection_string
            start_server(db_connection_string)
    except Exception as e:
        print(f"Failed to start server: {str(e)}")
