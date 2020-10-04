import os
from os import path

age = 17
ext = 'testfolder'
#allow = "Yes" if age >= 18 else 'No'

#print(allow)

#if isPath == False:
  #  print("makig extentin")
  #  print(ext)
  #  os.mkdir(ext)
isPath = path.exists(ext)
print(isPath)
os.mkdir(ext) if isPath == False else print("Folder Exists")

ignoreExt = input("Which extenstion do you want to ignore? ('',' ',py,ini,gitignore,md) - Press enter for default: ")
ignoreExt = ['', ' ', 'py', 'ini', 'gitignore','md'] if ignoreExt == '' else ignoreExt.split(',')
print(f"\nIgnoring these extensionts: {ignoreExt}\n")