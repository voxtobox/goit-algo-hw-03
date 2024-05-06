from pathlib import Path
from shutil import copy

def display_tree(path: Path, indent: str = "") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")
            
def put_file(file, files_store = {}):
    ext = file.suffix
    if ext not in files_store:
        files_store[ext] = []
    files_store[ext].append(file)
  
            
def parse(path: Path, files_store = {}):
    for child in path.iterdir():
        if child.is_dir():
            parse(child, files_store)
        else:
            put_file(child, files_store)
    return files_store

def copy_files(src: str, dst: str = './dist'):
    srcPath = Path(src)
    dstPath = Path(dst)
    
    files = parse(srcPath)
    for ext, filelist in files.items():
        for file in filelist:
            copy(file, dstPath)
        
    
            
if __name__ == "__main__":
    copy_files('./source')    
