import os

def find_file(folder, filename_base):

    filename_base = filename_base.lower().strip()

    for file in os.listdir(folder):
        file_name_no_ext = os.path.splitext(file)[0].lower()

        if filename_base == file_name_no_ext:
            return os.path.join(folder, file)

    return None