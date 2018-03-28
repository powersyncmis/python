import os,shutil,time


x=0
for dirPath, dirNames, fileNames in os.walk("\\\\192.168.0.20\\部門共用區\\行銷部\\POWERSYNC\\產品照片"):
    #print(dirPath)
    for f in fileNames:
        #print(os.path.join(dirPath, f))
        if f[-4:]==".jpg" and ("800x800" in dirPath) and f[-6:-4]=="-1":
            y=(os.path.join(dirPath, f))
            z="f:\\pcpong\\pic\\" + f
            if os.path.isfile(z):
                if os.path.getsize(y) > os.path.getsize(z):
                    shutil.copy(y,z)
                    x=x+1
                    print(x)
            else:
                shutil.copy(y,z)
                x=x+1
                print(x)
