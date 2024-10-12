import grpc
from proto.file_watcher_service_pb2 import FileUpdateRequest
from proto.file_watcher_service_pb2_grpc import FileWatcherServiceStub

def run():
    # Create a channel to connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub for the FileWatcherService
        stub = FileWatcherServiceStub(channel)
        
        # Create a request object
        request = FileUpdateRequest(
            directory_uuid='your-directory-uuid',
            file_uuid='your-file-uuid',
            file_path='/path/to/your/file',
            file_hash='your-file-hash',
            update_time='2023-10-01T12:00:00Z'
        )
        
        # Call the UpdateFile method
        response = stub.UpdateFile(request)
        
        # Print the response
        print("File update status:", response.status)

if __name__ == '__main__':
    run()