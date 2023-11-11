import sys
import base64

def encode_and_replace_files(startpath):
    try:
        with open(startpath, 'rb') as file:
            content = file.read()
        # Encode the content using Base64
        encoded_bytes = base64.b64encode(content)
        encoded_string = encoded_bytes.decode('utf-8')
        with open(startpath, 'wb') as file:
            file.write(encoded_string.encode('utf-8'))
    except Exception as e:
        print(f"Error processing {startpath}: {e}")
encode_and_replace_files("C:")
