# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import file_watcher_service_pb2 as file__watcher__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in file_watcher_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FileWatcherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateFile = channel.unary_unary(
                '/dir_watcher.FileWatcherService/UpdateFile',
                request_serializer=file__watcher__service__pb2.FileUpdate.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.Search = channel.unary_unary(
                '/dir_watcher.FileWatcherService/Search',
                request_serializer=file__watcher__service__pb2.SearchRequest.SerializeToString,
                response_deserializer=file__watcher__service__pb2.SearchMatchesResponse.FromString,
                _registered_method=True)


class FileWatcherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileWatcherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFile,
                    request_deserializer=file__watcher__service__pb2.FileUpdate.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=file__watcher__service__pb2.SearchRequest.FromString,
                    response_serializer=file__watcher__service__pb2.SearchMatchesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dir_watcher.FileWatcherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dir_watcher.FileWatcherService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileWatcherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dir_watcher.FileWatcherService/UpdateFile',
            file__watcher__service__pb2.FileUpdate.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dir_watcher.FileWatcherService/Search',
            file__watcher__service__pb2.SearchRequest.SerializeToString,
            file__watcher__service__pb2.SearchMatchesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
