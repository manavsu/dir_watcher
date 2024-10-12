#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR"

if [ -d "../.venv" ]; then
    source ../.venv/bin/activate
else
    echo "Virtual environment not found. Exiting."
    exit 1
fi
# Check if proto files exist in the client/proto and server/proto directories and delete them
CLIENT_PROTO_DIR="../client"
SERVER_PROTO_DIR="../server"

python -m grpc_tools.protoc -I. --python_out="$CLIENT_PROTO_DIR" --grpc_python_out="$CLIENT_PROTO_DIR" "file_watcher_service.proto"
python -m grpc_tools.protoc -I. --python_out="$SERVER_PROTO_DIR" --grpc_python_out="$SERVER_PROTO_DIR" "file_watcher_service.proto"

echo "Proto definitions compiled successfully."
 