from file_watcher_service_pb2 import FileUpdate, SearchMatchesResponse
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
                log.info(f"Creating new directory with id {request.uuid}, {type(request.uuid)}")
                directory = Directory(id=request.uuid)
                session.add(directory)
                session.commit()
            
            try:
                existing_file = session.query(File).filter_by(file_path=request.file.file_path, directory_id=directory.id).one()
                existing_file.file_path = request.file.file_path
                existing_file.hash = request.file.hash
                existing_file.update_time = request.file.update_time.ToDatetime()
                log.debug(f"Updating file {existing_file}")
            except NoResultFound:
                log.debug(f"Creating new file {request.file.file_path} in directory {directory.id}")
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
    
    def Search(self, request, context):
        try:
            session = SessionLocal()
            query = session.query(File).filter_by(directory_id=request.uuid)
            if request.search_term:
                query = query.filter(File.file_path.contains(request.search_term))
            files = query.all()
            
            response = SearchMatchesResponse()
            response.search_term = request.search_term
            response.uuid = request.uuid
            for file in files:
                file_info = response.files.add()
                file_info.file_path = file.file_path
                file_info.hash = file.hash
                file_info.update_time.FromDatetime(file.update_time)
            
            session.close()
            return response
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            log.error(f"Error processing search request {request} {e}", exc_info=True)
        return SearchMatchesResponse(search_term=request.search_term, uuid=request.uuid)