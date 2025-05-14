import os
import shutil

audio = [".mp3", ".wav", ".wma", ".aac"]
video = [".mp4", ".mkv", ".avi", ".wmv"]
documents = [".pdf", ".docx", ".txt", ".pptx"]
images = [".jpg", ".jpeg", ".png", ".gif"]
zips = [".zip", ".rar"]
software = [".exe", ".apk"]

path = "C:\\Users\\Arushi\\OneDrive\\Desktop\\docs"
files = os.listdir(path) 

for folder in ["audio", "video", "documents", "images", "zips", "software", "unknown"]: 
    folder_path = os.path.join(path, folder)  
    if not os.path.exists(folder_path): 
        os.mkdir(folder_path) 

# Move files
for file in files:
    extension = os.path.splitext(file)[1]  
    full_file_path = os.path.join(path, file)  

    if extension == "":                                
        subfolder_path = os.path.join(path, file)  
        if os.path.isdir(subfolder_path):  
            for file1 in os.listdir(subfolder_path):
                ext = os.path.splitext(file1)[1]    
                source = os.path.join(subfolder_path, file1)

                if ext in audio:
                    dest = os.path.join(path, "audio", file1)
                elif ext in video:
                    dest = os.path.join(path, "video", file1)
                elif ext in images:
                    dest = os.path.join(path, "images", file1)
                elif ext in zips:
                    dest = os.path.join(path, "zips", file1)
                elif ext in software:
                    dest = os.path.join(path, "software", file1)
                elif ext in documents:
                    dest = os.path.join(path, "documents", file1)
                else:
                    dest = os.path.join(path, "unknown", file1)

                if not os.path.exists(dest):
                    shutil.move(source, dest) 
    else:
        if extension in audio:
            dest_folder = "audio"
        elif extension in video:
            dest_folder = "video"
        elif extension in images:
            dest_folder = "images"
        elif extension in zips:
            dest_folder = "zips"
        elif extension in software:
            dest_folder = "software"
        elif extension in documents:
            dest_folder = "documents"
        else:
            dest_folder = "unknown"

        dest = os.path.join(path, dest_folder, file)
        if not os.path.exists(dest):
            shutil.move(full_file_path, dest)
        else:
            print(f"Skipped (already exists): {dest}")

print("Files organized successfully!")
