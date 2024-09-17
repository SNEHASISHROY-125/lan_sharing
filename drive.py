'''
SYNC DRIVE's [C/D/E]
'''


import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def create_directory(dest_path):
    try:
        # if not os.path.exists(dest_path):
        os.makedirs(dest_path, exist_ok=True)
    except FileExistsError as e: ...

def replicate_tree(source_drive, destination_folder) -> list[list, list]:
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # send to client to create directories
    # Walk through the source drive and collect all directories | files
    all_dirs = [os.path.join(destination_folder, os.path.relpath(root, source_drive))
                for root, dirs, files in os.walk(source_drive)]
    
    # files to send to client
    all_files = [os.path.join(root, file)
                 for root, dirs, files in os.walk(source_drive)
                 for file in files]
    
    # print(all_dirs)
    return [all_dirs, all_files]

def create_directory_ALL(all_dirs):
    '''CREATE ALL DIRECTORIES'''
    # Count the total number of directories to process
    total_dirs = len(all_dirs)

    # Use ThreadPoolExecutor to create directories in parallel
    with tqdm(total=total_dirs, desc="Replicating directories", unit="dir") as pbar:
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(create_directory, dir_path) for dir_path in all_dirs]
            for future in futures:
                future.result()
                pbar.update(1)

# if __name__ == "__main__":
#     source_drive = 'C:\\xampp'  # Change to 'D:\\' or 'E:\\' as needed
#     destination_folder = 'D:\\drive_c\\'  # Change to your desired destination folder
#     replicate_tree(source_drive, destination_folder)