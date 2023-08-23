#-----------sorting  the files according to the file type
#-----------and keeping in different folder
#-------importing libraries
import os
import shutil

#-------------receiving the folder path in which conntains the files to be sorted 
path=input("ENTER THE PATH OF THE FOLDER")

#-------------listing all the files and folders  present in the specified folder
listoffiles=(os.listdir(path))
#--------------looping through each file 
for i in listoffiles:
#--------------excepting error if the folder contain other than file (another folder)
    try:
#------------checking the extension of the file
#"ini" is a extension of dafault archieved file 
#(avoiding that file type from further operation)
        if i.split(".")[1]!="ini":
#------taking the file extension to create a folder 
            b=i.split(".")[1]
#------checking if the specified file format already  exists
            if not os.path.exists(path+r"/"+b+" files"):
#----------creating new folder with the extension name-files
                os.makedirs(path+r"/"+b+" files")
#----------checking if the copy of file exists 
            if i not in os.listdir(path+r"/"+b+" files"):
#--------moving the file to its filetype folder
                shutil.move(path+r"/"+i,path+r"/"+b+" files")

        else :
#------in case .uni file skip to next file
            continue
    except:
#--------in case if is  not a file skip to next file
        continue



