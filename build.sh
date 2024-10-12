#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR"

if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment not found. Creating virtual environment."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi
# Check if proto files exist in the client/proto and server/proto directories and delete them
CLIENT_PROTO_DIR="/client"
SERVER_PROTO_DIR="/server"

python -m grpc_tools.protoc -I. --python_out="$CLIENT_PROTO_DIR" --grpc_python_out="$CLIENT_PROTO_DIR" "file_watcher_service.proto"
python -m grpc_tools.protoc -I. --python_out="$SERVER_PROTO_DIR" --grpc_python_out="$SERVER_PROTO_DIR" "file_watcher_service.proto"

echo "Proto definitions compiled successfully."

echo "Building executables..."

pyinstaller dir_watcher_client.spec
pyinstaller dir_watcher_server.spec
pyinstaller db_dump.spec
pyinstaller search_client.spec
pyinstaller db_init.spec

echo "Executables built successfully."