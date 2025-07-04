#!/usr/bin/env python3

import sys
import json
import struct
import logging
import os
import hashlib
from pathlib import Path

# Add logging 
logging.basicConfig(
    filename='/tmp/backend_debug.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_downloads_folder():
    """Uses the default Downloads folder path"""
    return str(Path.home() / "Downloads")

def file_to_hash(file_path):
    """Calculate SHA-256 hash of a file"""
    try:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b''):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def find_duplicates(file_name):
    """Find and remove duplicates in Downloads folder"""
    try:
        downloads_dir = get_downloads_folder()
        file_path = os.path.join(downloads_dir, file_name)
        
        if not os.path.exists(file_path):
            logging.warning(f"File {file_path} does not exist")
            return 0
        
        # Calculate hash of the new file
        main_hash = file_to_hash(file_path)
        if not main_hash:
            return 0
        
        extension = os.path.splitext(file_name)[1]
        duplicates_removed = 0
        
        logging.info(f"Looking for duplicates of {file_name} in {downloads_dir}")
        
        # Check all files in Downloads
        for existing_file in os.listdir(downloads_dir):
            if existing_file == file_name:
                continue  # Skip the same file
            
            if not existing_file.endswith(extension):
                continue  # Skip different extensions
            
            existing_path = os.path.join(downloads_dir, existing_file)
            if not os.path.isfile(existing_path):
                continue
            
            # Calculate hash of existing file
            existing_hash = file_to_hash(existing_path)
            if existing_hash and existing_hash == main_hash:
                try:
                    os.remove(existing_path)
                    logging.info(f"Removed duplicate: {existing_path}")
                    duplicates_removed += 1
                except Exception as e:
                    logging.error(f"Error removing {existing_path}: {e}")
        
        return duplicates_removed
        
    except Exception as e:
        logging.error(f"Error in find_duplicates: {e}")
        return 0

def main():
    logging.info("=== BACKEND STARTED ===")  
    
    try:
        while True:
            # Read message length
            raw_length = sys.stdin.buffer.read(4)
            if not raw_length:
                logging.info("No input received, exiting")
                break
            
            message_length = struct.unpack('<I', raw_length)[0]
            logging.info(f"Message length: {message_length}")

            # Read message
            message_data = sys.stdin.buffer.read(message_length)
            message = json.loads(message_data.decode('utf-8'))
            logging.info(f"Received message: {message}")

            # Process message
            file_name = message.get('fileName')
            if not file_name:
                response = {"status": "error", "message": "No fileName provided"}
            elif file_name == "test-connection.txt":  
                response = {"status": "success", "message": "Connection successful"}
            else:
                # Find and remove duplicates
                duplicates_removed = find_duplicates(file_name)
                response = {
                    "status": "success", 
                    "fileName": file_name,
                    "duplicatesRemoved": duplicates_removed,
                }
            
            # Send response
            response_json = json.dumps(response)
            response_bytes = response_json.encode('utf-8')
            
            sys.stdout.buffer.write(struct.pack('<I', len(response_bytes)))
            sys.stdout.buffer.write(response_bytes)
            sys.stdout.buffer.flush()
            
            logging.info(f"Sent response: {response}")
            
    except Exception as e:
        logging.error(f"Error in main: {e}")
    finally:
        logging.info("=== BACKEND TERMINATED ===")

if __name__ == "__main__":
    main()