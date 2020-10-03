#For now this program will move files into the directory of its extension. So a "File.TXT" will be moved to \txt\file.txt
    #It also moves duplicate files to a \DuplicateFiles folder.
    #Future it will detect a new file and move the new file to location

#Importing necessecary files.
import os
import os.path
from os import path

#What this does:
print("""

  ______ _ _         _____            _
 |  ____(_) |       / ____|          | |
 | |__   _| | ___  | (___   ___  _ __| |_ ___ _ __
 |  __| | | |/ _ \  \___ \ / _ \| '__| __/ _ \ '__|
 | |    | | |  __/  ____) | (_) | |  | ||  __/ |
 |_|    |_|_|\___| |_____/ \___/|_|   \__\___|_|
                                   by: Max Derevencha
#Features:
    *Moves Files to the folder of it's extension.
    *Moves Duplicate Files to the "DuplicatesFolder"
    *Ignore's file with specified extensions.
    *Alot of verbose output.

#Features to Come:
    *Logging all actions to file.
    *Configuration file that includes; Extensions/Files/Directories to Ignore.
    *Option to do Sub-Directories a certain level deep.


#Instructions:
    1. Put this Pyton File into the desired folder to be sorted - run it again if moved to a different folder.
    2. Enter Extensions to be ignored once prompted as CSV.
    3. Sit back and enjoy
    4. Verify - I am human even though I did run this several hundred times.

""")
#Asking which extenstions to ignore
ignoreExt = input("Which extenstion do you want to ignore? ('',' ',py,ini) - Press enter for default: ")
if ignoreExt == '':
    ignoreExt = ['',' ','py','ini']
else:
    ignoreExt = ignoreExt.split(',')
print(ignoreExt)

#Getting current directory of program executing.
cwd = os.getcwd()
#Getting all the files in the directory
allFiles = os.listdir(cwd)

#starting the processing for all the files.
for x in allFiles:
    print("++++++++++STARTING HERE++++")

    #Spliting the file name between name and extension
    file = x.rsplit('.',1)
    print(file)

    try:
        print("++++++assiging extesnion")
        #Assinging variables of name and extesnion
        ext = file[1]
        name = file[0]
        #print(name + " ++ " + ext )
        #Starting the moving process but avoiding .py and empty file names.
        if ext not in ignoreExt:
            print("++++++checking if folder with ext name exists")
            #Checking if folder exists and if not then it will create it.
            isPath =  path.exists(ext)
            if isPath == False:
                print("makig extentin")
                print(ext)
                os.mkdir(ext)

            print("+++++Creating and moving file")
            print(file)

            #Moving file to new location
            newLoc = cwd +'\\' + ext +'\\' + x
            print(newLoc)
            os.rename(x,newLoc )
            print("+++++++++++Done moving file to new location")
        else:
            print("------------THis file is in teh Bypass Ext list: {}".format(file))
            print(file)
            continue

    except (IOError, Exception) as error:
        #print(error.errno)
        print("------------No Extension files")
        print(file)
        print(error)
        try:

            #
            if 'Cannot create a file when that file already exists' in str(error):
                #Creating a DuplicateFiles folder to move dups into into .
                isPath = path.exists('DuplicateFiles')
                if isPath == False:
                    print("making DuplicateFiles folder")
                    os.mkdir('DuplicateFiles')
                print("THis is a duplicate file  -- Moving it")
                newLoc = cwd + '\\' + 'DuplicateFiles' + '\\' + x
                print(newLoc)
                os.rename(x, newLoc)
                print("Done Moving)")

        except Exception as error:
            print("------Some Error")
            print(error)


print("!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!")
input('')
