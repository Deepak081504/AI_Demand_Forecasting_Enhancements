# app/utils/file_handler.py
import os

def save_uploaded_stream_file(destination_path: str, content: bytes):
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    with open(destination_path, "wb") as f:
        f.write(content)