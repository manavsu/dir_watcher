from file_watcher_service_pb2 import File, FileUpdate
from file_watcher_service_pb2_grpc import FileWatcherServiceServicer
from db_config import SessionLocal
from db_models import Directory, File
from sqlalchemy.orm.exc import NoResultFound
from google.protobuf.empty_pb2 import Empty
import grpc
import logging

log = logging.getLogger(__name__)

class FileWatcherService(FileWatcherServiceServicer):
    def UpdateFile(self, request, context):
        try:
            session = SessionLocal()
            try:
                directory = session.query(Directory).filter_by(id=request.directory_uuid).one()
            except NoResultFound:
                directory = Directory(id=request.directory_uuid)
                session.add(directory)
                session.commit()
            
            try:
                existing_file = session.query(File).filter_by(file_path=request.file_path, directory_id=directory.id).one()
                existing_file.file_path = request.file_path
                existing_file.hash = request.file_hash
                existing_file.update_time = request.update_time
            except NoResultFound:
                new_file = File(
                    file_path=request.file_path,
                    hash=request.file_hash,
                    update_time=request.update_time,
                    directory_id=directory.id
                )
                session.add(new_file)
            
            session.commit()
            session.close()
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)