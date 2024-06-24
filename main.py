import argparse
import os
from src.sb3zip import zipProject, unzipProject, cleanup
from src.sb3patcher import patchProjectJSON

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='FreezerBurn', description='pastaOS Anticheat Patcher')
    parser.add_argument('-F', '--filedir', type=str, required=True)
    parser.add_argument('-T', '--tmpdir', type=str, required=False, default=os.path.join(os.getcwd(), 'tmp'))
    args = parser.parse_args()

    fileDir = args.filedir
    tmpDir = args.tmpdir
    projectJSONPath = os.path.join(tmpDir, 'project.json')

    welcomeText = """
=======================================
FreezerBurn - pastaOS Anticheat Patcher
      by bambus80 - 24.06.2024
=======================================
    """
    print(welcomeText)

    unzipProject(fileDir, tmpDir)

    if os.path.exists(projectJSONPath):
        patchProjectJSON(projectJSONPath)
    else:
        print(f"[ERROR] {projectJSONPath} does not exist.")
        exit(1)

    zipProject(fileDir, tmpDir)
    cleanup(tmpDir)
    print("=== Project successfully patched! ===")