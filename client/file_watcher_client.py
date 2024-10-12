import grpc
from file_watcher_service_pb2 import FileUpdate, File
from file_watcher_service_pb2_grpc import FileWatcherServiceStub
import config

class FileWatcherClient:
    def __init__(self):
        self.channel = grpc.insecure_channel(config.URL':50051')
        self.stub = FileWatcherServiceStub(self.channel)
    
    def update_file(self, directory_uuid, file_uuid, file_path, file_hash, update_time):
        request = FileUpdate(
            directory_uuid=directory_uuid,
            file_uuid=file_uuid,
            file_path=file_path,
            file_hash=file_hash,
            update_time=update_time
        )
        response = self.stub.UpdateFile(request)
        return response.status