import os

directory = "."

for subdir, dirs, files in os.walk(directory):
    print (subdir)
    for file in files:   
        filepath = subdir + os.sep + file
        print (filepath)
        if(filepath.find(" ")):
            os.rename(filepath, filepath.replace(" ", "-"))