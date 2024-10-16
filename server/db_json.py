import json
import argparse
from sqlalchemy.orm import sessionmaker
from db_config import engine, Base
from db_models import Directory, File

# Create a new session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def directory_to_dict(directory):
    return {
        'id': directory.id,
        'update_time': directory.update_time.isoformat() if directory.update_time else None,
        'files': [file_to_dict(file) for file in directory.files]
    }

def file_to_dict(file):
    return {
        'id': file.id,
        'file_path': file.file_path,
        'hash': file.hash,
        'update_time': file.update_time.isoformat() if file.update_time else None,
    }

def db_to_json(output_file):
    try:
        directories = session.query(Directory).all()
        directories_list = [directory_to_dict(directory) for directory in directories]
        
        json_output = json.dumps(directories_list, indent=4)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(json_output)
        
        return json_output
    finally:
        session.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export database to JSON.')
    parser.add_argument('output_file', nargs='?', type=str, help='The output file for the JSON data (optional).')
    args = parser.parse_args()
    
    json_data = db_to_json(args.output_file)
    print(json_data)