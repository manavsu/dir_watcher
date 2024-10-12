import os
import hashlib
import json
import config
import logging
import uuid
from file_watcher_stub import FileWatcherStub
from file_watcher_service_pb2 import FileUpdateType
from datetime import datetime

log = logging.getLogger(__name__)

class Repo:
    def __init__(self, path, push=True):
        self.dir_state = {}
        self.UUID = None
        self.path = path
        self.push = push
        self.repo_dir = os.path.join(path, config.REPO_DIR)
        self.index_file = os.path.join(self.repo_dir, config.INDEX_FILE)
        self.uuid_file = os.path.join(self.repo_dir, config.UUID_FILE)
        self.load_state()
        self.scan_dir()
        self.upstream_stub = FileWatcherStub() 

    def load_state(self):
        if not os.path.exists(self.repo_dir):
            os.makedirs(self.repo_dir)

        if not os.path.exists(self.index_file):
            with open(self.index_file, 'w') as f:
                json.dump({}, f)
        
        if not os.path.exists(self.uuid_file):
            with open(self.uuid_file, 'w') as f:
                f.write(uuid.uuid4().hex)
        
        with open(self.uuid_file, 'r') as f:
            self.UUID = f.read()

        with open(self.index_file, 'r') as f:
            self.dir_state = json.load(f)
    
    def scan_dir(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                filepath = os.path.join(root, file)
                if filepath == self.index_file or filepath == self.uuid_file:
                    continue
                if filepath not in self.dir_state:
                    self.dir_state[filepath] = self.hash_file(filepath)
                    log.info(f"Added {filepath} to state.")
                    if self.push:
                        self.upstream_stub.update_file(self.UUID, filepath, self.dir_state[filepath], datetime.now(), FileUpdateType.CREATED)
                else:
                    hash = self.hash_file(filepath)
                    if hash != self.dir_state[filepath]:
                        self.dir_state[filepath] = hash
                        if self.push:
                            self.upstream_stub.update_file(self.UUID, filepath, self.dir_state[filepath], datetime.now(), FileUpdateType.UPDATED)
                        log.info(f"Updated {filepath} in state.")
        self.commit()

    def hash_file(self, filepath):
        hasher = hashlib.sha1()
        try:
            with open(filepath, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            return hasher.hexdigest()
        except FileNotFoundError:
            log.error(f"File not found: {filepath}", extra={'filepath': filepath, 'func': 'hash_file'})
            return None

    def update_file_state(self, filepath, created=False):
        self.dir_state[filepath] = self.hash_file(filepath)
        log.info(f"Updated state for {filepath}")
        self.commit()
        if self.push:
            self.upstream_stub.update_file(self.UUID, filepath, self.dir_state[filepath], datetime.now(), FileUpdateType.CREATED if created else FileUpdateType.UPDATED)

    def delete_file_state(self, filepath):
        if filepath in self.dir_state:
            del self.dir_state[filepath]
            log.info(f"Deleted state for {filepath}")
            self.commit()
            if self.push:
                self.upstream_stub.update_file(self.UUID, filepath, self.dir_state[filepath], datetime.now(), FileUpdateType.DELETED)

        else:
            log.error(f"File not found: {filepath}", extra={'filepath': filepath, 'func': 'delete_file_state'})
        

    def commit(self):
        with open(self.index_file, 'w') as f:
            json.dump(self.dir_state, f, indent=4)
        log.info("Changes committed.")
