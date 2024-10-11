import os
from time import sleep
import hashlib

def compute_sha256(file_path):
    """Compute the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def traverse_and_hash(directory):
    """Recursively traverse the directory and compute SHA-256 hash for each file."""
    d = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = compute_sha256(file_path)
            d = {file_path: file_hash}
    
def scan(directory):
    """Scan the directory for changes."""
    return traverse_and_hash(directory)

def submit_scan_results(scan_results, url):
    """Submit the scan results to the specified URL."""
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(scan_results), headers=headers)
    return response.status_code, response.text

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python watcher.py <directory> <url>")
        sys.exit(1)
    directory = sys.argv[1]
    url = sys.argv[2]
    while True:
        scan_results = scan(directory)
        status_code, response_text = submit_scan_results(scan_results, url)
        print(f"Submitted scan results: {status_code} - {response_text}")
        sleep(0.25)

