import argparse
from file_watcher_stub import FileWatcherStub
import config
import os

def print_all_files(directory_uuid, search_term):
    stub = FileWatcherStub()
    response = stub.search(directory_uuid, search_term)
    print(f"All Files For {directory_uuid}:")
    for file in response.files:
        print(f"Path: {file.file_path}, Hash: {file.hash}, Update Time: {file.update_time.ToDatetime()}")

def main():
    parser = argparse.ArgumentParser(description="Search for files in a directory.")
    parser.add_argument("search_term", type=str, nargs=1, default="", help="The term to search for in file paths required.")
    parser.add_argument("directory_uuid", type=str, default="", nargs="?", help=f"The UUID of the directory to search in (optional). By default will check for {os.path.join(config.REPO_DIR, config.UUID_FILE)}.")
    
    args = parser.parse_args()
    if not args.directory_uuid:
        with open(os.path.join(config.REPO_DIR, config.UUID_FILE), 'r') as f:
            args.directory_uuid = f.read()
    if not args.search_term:
        print("Please provide a search term.")
        return
    
    print_all_files(args.directory_uuid, args.search_term[0])

if __name__ == "__main__":
    main()