import os,shutil;
path= r"C:\Users\muham\Desktop\ABD_VARIS"
listoffiles=(os.listdir(path))
for i in listoffiles:
    try:
        if i.split(".")[1]!="ini":
            b=i.split(".")[1] 
            if not os.path.exists(path+r"/"+b+" files"):
                os.makedirs(path+r"/"+b+" files")
            if i not in os.listdir(path+r"/"+b+" files"):
                shutil.move(path+r"/"+i,path+r"/"+b+" files")

        else :
            continue
    except:
        continue
#print(os.path.exists(path))


