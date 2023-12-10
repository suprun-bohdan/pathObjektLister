import os
import sys
import re

def sort_key(name):
    # Знаходимо числа на початку назви файлу
    match = re.match(r'(\d+)', name)
    # Якщо є число, повертаємо його як ключ для сортування
    if match:
        return int(match.group(1))
    # Інакше повертаємо саму назву
    return name

def list_files(directory):
    try:
        # List files and folders in the directory
        files = os.listdir(directory)
        # Sort using the custom sort key
        files.sort(key=sort_key)

        # Print sorted files
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Insufficient rights to access the directory: {directory}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python getPathList.py [path to directory]")
    else:
        list_files(sys.argv[1])
