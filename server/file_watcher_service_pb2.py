# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: file_watcher_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'file_watcher_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x66ile_watcher_service.proto\x12\x0b\x64ir_watcher\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"m\n\nFileUpdate\x12\x1f\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x11.dir_watcher.File\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x30\n\x0bupdate_type\x18\x03 \x01(\x0e\x32\x1b.dir_watcher.FileUpdateType\"2\n\rSearchRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x13\n\x0bsearch_term\x18\x02 \x01(\t\"\\\n\x15SearchMatchesResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x13\n\x0bsearch_term\x18\x02 \x01(\t\x12 \n\x05\x66iles\x18\x03 \x03(\x0b\x32\x11.dir_watcher.File\"X\n\x04\x46ile\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*7\n\x0e\x46ileUpdateType\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0b\n\x07UPDATED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x32\x9d\x01\n\x12\x46ileWatcherService\x12=\n\nUpdateFile\x12\x17.dir_watcher.FileUpdate\x1a\x16.google.protobuf.Empty\x12H\n\x06Search\x12\x1a.dir_watcher.SearchRequest\x1a\".dir_watcher.SearchMatchesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_watcher_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEUPDATETYPE']._serialized_start=452
  _globals['_FILEUPDATETYPE']._serialized_end=507
  _globals['_FILEUPDATE']._serialized_start=105
  _globals['_FILEUPDATE']._serialized_end=214
  _globals['_SEARCHREQUEST']._serialized_start=216
  _globals['_SEARCHREQUEST']._serialized_end=266
  _globals['_SEARCHMATCHESRESPONSE']._serialized_start=268
  _globals['_SEARCHMATCHESRESPONSE']._serialized_end=360
  _globals['_FILE']._serialized_start=362
  _globals['_FILE']._serialized_end=450
  _globals['_FILEWATCHERSERVICE']._serialized_start=510
  _globals['_FILEWATCHERSERVICE']._serialized_end=667
# @@protoc_insertion_point(module_scope)
