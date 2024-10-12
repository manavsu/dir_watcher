from file_watcher_service_pb2 import FileUpdate
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
                directory = session.query(Directory).filter_by(id=request.uuid).one()
            except NoResultFound:
                print(f"Creating new directory with id {request.uuid}, {type(request.uuid)}")
                directory = Directory(id=request.uuid)
                session.add(directory)
                session.commit()
            
            try:
                existing_file = session.query(File).filter_by(file_path=request.file.file_path, directory_id=directory.id).one()
                existing_file.file_path = request.file.file_path
                existing_file.hash = request.file.hash
                existing_file.update_time = request.file.update_time.ToDatetime()
            except NoResultFound:
                new_file = File(
                    file_path=request.file.file_path,
                    hash=request.file.hash,
                    update_time=request.file.update_time.ToDatetime(),
                    directory_id=directory.id
                )
                session.add(new_file)
            
            session.commit()
            session.close()
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            log.error(f"Error processing update file {request} {e}", exc_info=True)
        return Empty()