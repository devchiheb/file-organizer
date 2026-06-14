import  os
import shutil

path=input("enter the path of the folder: ")
files=os.listdir(path)
for file in files:
    filename,extentions=os.path.splitext(file)
    extension=extentions[1:]

    if(os.path.exists(path+"/"+extension)) :
        shutil.move(path+"/"+file,path+"/"+extension+'/'+file)
    else:
        os.mkdir(path+'/'+extension)
        shutil.move(path+"/"+file,path+'/'+extension+'/'+file)
        