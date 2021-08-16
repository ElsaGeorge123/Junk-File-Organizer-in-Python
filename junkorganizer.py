import os
from pathlib import Path
Directories={
    "HTML":{".html"},
    "IMAGES":{".jpeg",".jpg",".png"},
    "VIDEOS": {".mp4"},
    "AUDIO":{".mp3"},
    "TEXT DOCUMENTS": {".txt"},
    "PDF": {".pdf"},
    "PYTHON":{".py"}
    }

File_format_dict={}
for directory,file_formats in Directories.items():
    for file_format in file_formats:
        File_format_dict[file_format]=directory

for path in os.scandir():
    if path.is_dir():
        continue
    file_path=Path(path)
    file_format=file_path.suffix.lower()
    if file_format in File_format_dict:
        directory_path=Path(File_format_dict[file_format])
        directory_path.mkdir(exist_ok=True)
        file_path.rename(directory_path.joinpath(file_path))
    

            
    
    


    
