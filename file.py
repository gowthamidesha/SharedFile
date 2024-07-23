import os
import sys
import subprocess

def create_shared_directory(paths, group_name):
    for path in paths:
        try:
            os.makedirs(path, exist_ok=True)
            subprocess.run(['chown', f':{group_name}', path], check=True)
            subprocess.run(['chmod', '2775', path], check=True)
            print(f"Successfully created and configured the shared directory: {path}")
        except Exception as e:
            print(f"Error creating or configuring directory {path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_shared_dir.py <directory_path> [<directory_path> ...]")
        sys.exit(1)
    group_name = 'developers'
    paths = sys.argv[1:]
    create_shared_directory(paths, group_name)

if __name__ == "__main__":
    main()
