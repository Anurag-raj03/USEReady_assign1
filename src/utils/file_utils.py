import os
def list_files(folder_path):
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith((".docx", ".png", ".jpg", ".jpeg"))
    ]