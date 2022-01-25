import os
import shutil
from fastapi.responses import FileResponse
from tempfile import TemporaryFile
from config import Config


async def create_file(file_name: str, file: TemporaryFile):
    full_file_path = os.path.join(Config.STORAGE_DIR, file_name)
    contents = await file.read()
    new_file = open(full_file_path, "wb")
    new_file.write(contents)


async def get_file(file_name: str):
    full_file_path = os.path.join(Config.STORAGE_DIR, file_name)
    return FileResponse(full_file_path)