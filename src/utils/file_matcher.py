import os
def find_file(folder, filename_base):
    filename_base = str(filename_base).strip().lower()
    for file in os.listdir(folder):
        file_clean = file.strip().lower()
        name_without_ext = os.path.splitext(file_clean)[0]
        if name_without_ext == filename_base:
            return os.path.join(folder, file)

    return None