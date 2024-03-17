import os

Folder_Name = input("Enter the name of the Folder : ")

print(Folder_Name)

if(not os.path.exists(Folder_Name)):
    os.mkdir(Folder_Name)

    Folder_Path = os.path.join(os.getcwd(),Folder_Name)



    All_File = ['index.html','style.css','script.js']

for File_Name in All_File:
    File_path = os.path.join(Folder_Path,File_Name)
    with open(File_path, 'w') as f:
        pass