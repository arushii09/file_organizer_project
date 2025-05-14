'''
import os
import shutil
audio=[".mp3", ".wav", "wma", "aac"]
video=[".mp4", ".mkv", ".avi", "wmv"]
documents=[".pdf", "docx", ".txt", ".pptx"]
images=[".jpg", ".jpeg", ".png", ".gif"]
zips=[".zip", "rar"]
software=[".exe", ".apk"]
path= "C:\\Users\\Arushi\\OneDrive\\Desktop\\docs"
files= os.listdir(path) #list all the directory of the path that we will give


os.mkdir(path+"\\"+"audio")
os.mkdir(path+"\\"+"video")
os.mkdir(path+"\\"+"documents")
os.mkdir(path+"\\"+"images")
os.mkdir(path+"\\"+"zips")
os.mkdir(path+"\\"+"software")
os.mkdir(path+"\\"+"unknown")


for folder in ["audio", "video", "documents", "images", "zips", "software", "unknown"]:
    folder_path = path + "\\" + folder
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


for file in files:
    extension = os.path.splitext(file)[1] #give the path
    if extension == "": #if extension is empty it means it is a folder
        files1 = os.listdir(path+"\\"+file)  #folder inside folder
        for file1 in files1:
            ext = os.path.splitext(file1)[1]  #check the extension of file1
            newpath = path+"\\"+file+"\\"  #extension is extracted into this variable
            if ext in audio:
                shutil.move(newpath + file1,path+"\\"+"audio")  #moving into new path
            elif ext in video:
                shutil.move(newpath + file1,path+"\\"+"video")      #all condition run when we have a folder inside folder
            elif ext in images:
                shutil.move(newpath + file1,path+"\\"+"images")
            elif ext in zips:
                shutil.move(newpath + file1,path+"\\"+"zips")
            elif ext in software:
                shutil.move(newpath + file1,path+"\\"+"software")
            elif ext in documents:
                shutil.move(newpath + file1,path+"\\"+"documents")
            else:
                shutil.move(newpath + file1,path+"\\"+"unknown")
    elif extension in audio:
        shutil.move(path+"\\" + file,path+"\\"+"audio")  #moving into new path
    elif extension in video:
        shutil.move(path+"\\" + file,path+"\\"+"video")
    elif extension in images:
        shutil.move(path+"\\" + file,path+"\\"+"images")
    elif extension in zips:
        shutil.move(path+"\\" + file,path+"\\"+"zips")  #all this condition will run for 1st folder
    elif extension in software:
        shutil.move(path+"\\" + file,path+"\\"+"software")
    elif extension in documents:
        shutil.move(path+"\\" + file,path+"\\"+"documents")
    else:
        shutil.move(path+"\\" + file,path+"\\"+"unknown")
print("✅ Files organized successfully!")
'''

import os
import shutil

audio = [".mp3", ".wav", ".wma", ".aac"]
video = [".mp4", ".mkv", ".avi", ".wmv"]
documents = [".pdf", ".docx", ".txt", ".pptx"]
images = [".jpg", ".jpeg", ".png", ".gif"]
zips = [".zip", ".rar"]
software = [".exe", ".apk"]

path = "C:\\Users\\Arushi\\OneDrive\\Desktop\\docs"
files = os.listdir(path)  #to get a list of all files and subdirectories in the specified path

for folder in ["audio", "video", "documents", "images", "zips", "software", "unknown"]:  # Create folders if they don't exist
    folder_path = os.path.join(path, folder)  
    if not os.path.exists(folder_path):  # checks if the folder already exists using os.path.exists()
        os.mkdir(folder_path)  #If the folder does not exist, it creates the folder using os.mkdir()

# Move files
for file in files:
    extension = os.path.splitext(file)[1]  #Extracts the file extension of each file by splitting the file name from its extension
    full_file_path = os.path.join(path, file)  #Constructs the complete path for the file 

    if extension == "":                                  #If the file doesn’t have an extension the code moves on to check if it's a subfolder
        subfolder_path = os.path.join(path, file)   #checks if file is a folder then it lists all files inside that subfolder
        if os.path.isdir(subfolder_path):  
            for file1 in os.listdir(subfolder_path):
                ext = os.path.splitext(file1)[1]     #each file inside the subfolder(file1), it checks the extension and determines           which folder to move it to (e.g., audio, video  etc.)
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
                    shutil.move(source, dest)  # moves the file to the appropriate destination folder, but only if it doesn’t already exist there

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
