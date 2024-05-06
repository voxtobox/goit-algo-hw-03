from pathlib import Path
from shutil import copy
from os import makedirs

                        
def put_file(file, files_store = {}):
    ext = file.suffix.replace('.', '')
    if ext not in files_store:
        files_store[ext] = []
    files_store[ext].append(file)
  
            
def parse(path: Path, files_store = {}):
    try:
        for child in path.iterdir():
            if child.is_dir():
                parse(child, files_store)
            else:
                put_file(child, files_store)
        return files_store
    except:
         print(f'{path} папка не доступна для читання')


def copy_files(src: str, dst: str = './dist'):
    srcPath = Path(src)
    dstPath = Path(dst)
    
    makedirs(dstPath, exist_ok=True)
    
    files = parse(srcPath)
    for ext, filelist in files.items():
        dstPathExt = dstPath.joinpath(ext)
        makedirs(dstPathExt, exist_ok=True)
        for file in filelist:
            try:
                copy(file, dstPathExt)
            except:
                print(f'{file} файл не доступний для читання')
    
            
if __name__ == "__main__":
    copy_files('./source', './distribution')
