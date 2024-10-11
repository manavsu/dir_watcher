import logging
from watchdog.events import FileSystemEventHandler
from repo import Repo

log = logging.getLogger(__name__)

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