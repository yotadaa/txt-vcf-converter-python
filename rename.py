
import os
import glob
import string
import process
import shutil  # Needed for moving files

def create_process_folder():
    process_folders = [f for f in os.listdir() if f.startswith("Process")]
    folder_count = len(process_folders)
    new_folder_name = f"Process_{folder_count + 1}"
    os.makedirs(new_folder_name)
    return new_folder_name

def move_files_to_folder(files, folder):
    for file in files:
        shutil.move(file, folder)
    print(f"Moved files to {folder}")

def rename_files_to_mma(txt_files, output):
    process_folder=create_process_folder()
    # txt_files = [f"{i}" for i in txt_files]
    alphabet = string.ascii_uppercase
    output_files = []
    for i, file in enumerate(txt_files):
    #     new_name = f"{output}{alphabet[i]}.txt"
    #     try:
    #         os.rename(file, new_name)
    #         print(f"Renamed '{file}' to '{new_name}'")
    #     except:
    #         print(f"cannot find {file}")
        output_files.extend(process.main(file, f"{output}{alphabet[i]}"))
    move_files_to_folder(output_files, process_folder)
    print("Done processing...")
    
def move_files_to_folder(files, folder):
    for file in files:
        shutil.move(file, folder)
    print(f"Moved files to {folder}")
    
def main(txt_files,format):
    # text = []
    # for i in range(15):
    #     text.append(f"3_500_{97+i}")
    rename_files_to_mma(txt_files, format)

# if __name__ == "__main__":
#     process()
