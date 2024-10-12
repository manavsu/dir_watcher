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

if [ -d "$CLIENT_PROTO_DIR" ]; then
    rm -f "$CLIENT_PROTO_DIR"/*.py
    echo "Deleted existing proto files in $CLIENT_PROTO_DIR"
fi

if [ -d "$SERVER_PROTO_DIR" ]; then
    rm -f "$SERVER_PROTO_DIR"/*.py
    echo "Deleted existing proto files in $SERVER_PROTO_DIR"
fi

if [ ! -d "$CLIENT_PROTO_DIR" ]; then
    mkdir "$CLIENT_PROTO_DIR"
    echo "Created directory $CLIENT_PROTO_DIR"
fi

if [ ! -d "$SERVER_PROTO_DIR" ]; then
    mkdir "$SERVER_PROTO_DIR"
    echo "Created directory $SERVER_PROTO_DIR"
fi

python -m grpc_tools.protoc -I. --python_out="$CLIENT_PROTO_DIR" --grpc_python_out="$CLIENT_PROTO_DIR" "file_watcher_service.proto"
python -m grpc_tools.protoc -I. --python_out="$SERVER_PROTO_DIR" --grpc_python_out="$SERVER_PROTO_DIR" "file_watcher_service.proto"

echo "Proto definitions compiled successfully."
 