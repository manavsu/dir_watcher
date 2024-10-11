import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import hashlib
import logging
from repo import Repo
import signal
import threading

log = logging.getLogger(__name__)

cancel_event = threading.Event()

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, path):
        super().__init__()
        self.repo = Repo(path)

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path == self.repo.index_file or event.src_path == self.repo.uuid_file:
            return
        self.repo.update_file_state(event.src_path)
        log.debug(f"File modified: {event.src_path}")
    
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path == self.repo.index_file or event.src_path == self.repo.uuid_file:
            return
        self.repo.update_file_state(event.src_path)
        log.debug(f"File created: {event.src_path}")
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        if event.src_path == self.repo.index_file or event.src_path == self.repo.uuid_file:
            return
        self.repo.delete_file_state(event.src_path)
        log.debug(f"File deleted: {event.src_path}")

def signal_handler(signal, frame):
    print(f"Signal {signal} received, stopping observer...")
    cancel_event.set()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch a directory for changes.")
    parser.add_argument("path", nargs="?", default=".", help="The path to watch. Defaults to the current directory.")
    args = parser.parse_args()

    path_to_watch = args.path
    log.info(f"Watching {path_to_watch} for changes.")
    event_handler = ChangeHandler(path_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    observer.start()

    while not cancel_event.wait(1):
        pass
    observer.stop()
    observer.join()