import os
import sys
import shutil
from pathlib import Path


def parse_args():
  exit_dir = sys.argv[1]
  enter_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'
  exit_path = Path(exit_dir)
  enter_path = Path(enter_dir)
  return exit_path, enter_path


def read_dir(exit_path, enter_path):
  try:
    if os.path.isdir(exit_path):
      for item in os.listdir(exit_path):
        item_path = os.path.join(exit_path, item)
        if os.path.isdir(item_path):
          read_dir(item_path, enter_path)
        elif os.path.isfile(item_path):
          copy_file(item_path, enter_path)
  except Exception as e:
        print(f"Error reading directory {exit_path}: {e}")


def copy_file(file_path, enter_path):
  try:
    _, ext = os.path.splitext(file_path)
    ext = ext.lstrip('.')
    dest_dir = os.path.join(enter_path, ext)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(file_path, dest_dir)
    print(f"Copied {file_path} to {dest_dir}")
  except Exception as e:
     print(f'Error copying file: {file_path}: {e}')


def main():
    exit_path, enter_path = parse_args()

    if not os.path.exists(exit_path):
        print(f"Source directory {exit_path} does not exist.")
        return

    if not os.path.exists(enter_path):
        os.makedirs(enter_path)

    read_dir(exit_path, enter_path)

if __name__ == "__main__":
    main()