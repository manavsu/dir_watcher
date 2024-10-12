import grpc
import logging
import threading
import argparse
from file_watcher_service import FileWatcherService
import file_watcher_service_pb2_grpc
from concurrent.futures import ThreadPoolExecutor
import config

log = logging.getLogger(__name__)

cancel_event = threading.Event()

def signal_handler(signal, frame):
    log.info(f"Signal {signal} received, stopping observer...")
    cancel_event.set()

def serve():
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=10))
    file_watcher_service_pb2_grpc.add_FileWatcherServiceServicer_to_server(FileWatcherService(), server)
    server.add_insecure_port(config.URL)
    server.start()

    while not cancel_event.wait(1):
        pass
    server.stop(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the File Watcher Service.')

    serve()