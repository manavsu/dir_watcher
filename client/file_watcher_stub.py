import grpc
from file_watcher_service_pb2 import FileUpdate, File
from file_watcher_service_pb2_grpc import FileWatcherServiceStub
import config

class FileWatcherStub:
    def __init__(self):
        self.channel = grpc.insecure_channel(config.URL)
        self.stub = FileWatcherServiceStub(self.channel)
    
    def update_file(self, directory_uuid, file_path, file_hash, update_time, update_type):
        request = FileUpdate(
            file = File(file_path=file_path, hash=file_hash, update_time=update_time),
            uuid=directory_uuid,
            update_type=update_type
        )
        response = self.stub.UpdateFile(request)
        return response.status