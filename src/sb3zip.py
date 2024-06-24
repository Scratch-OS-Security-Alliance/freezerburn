import zipfile
from os import path, listdir, remove, walk


def unzipProject(filepath: str, destination: str) -> None:
    with zipfile.ZipFile(filepath, 'r') as f:
        f.extractall(destination)
        print(f"SB3 extracted.")

def zipProject(filepath: str, source: str) -> None:
    with zipfile.ZipFile(filepath, 'w', compression=zipfile.ZIP_DEFLATED) as f:
        for root, _, files in walk(source):
            for file in files:
                file_path = path.join(root, file)
                arcname = path.relpath(file_path, source)
                f.write(file_path, arcname)
    print(f"SB3 packed.")

def cleanup(destination: str) -> None:
    print("Cleaning up...")
    for i in listdir(destination):
        filePath = path.join(destination, i)
        remove(filePath)