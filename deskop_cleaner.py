
import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def move_file_to_subfolder(file_path, subfolder_path):
    shutil.move(file_path, subfolder_path)

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                move_file_to_subfolder(file_path, subfolder_path)
                print(f"Verschoben: {filename} -> {subfolder_name}/")

if __name__ == "__main__":
    print("Desktop Cleaner Script")
    folder_path = 'C:\\Users\\mha\\Downloads\\Python-Cleaning-Ordner'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Reinigung vollständig.")
    else:
        print("Falscher Pfad. Bitte überprüfe den Pfad.")