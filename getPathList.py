import os
import sys

def list_files(directory):
    try:
        # Перелічення файлів і папок у вказаній директорії
        for file in os.listdir(directory):
            print(file)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Insufficient rights to access the directory: {directory}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python getPathList.py [шлях до директорії]")
    else:
        list_files(sys.argv[1])