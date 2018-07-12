import os
import urllib.request
import re

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter.messagebox

print(os.getcwd())
currentPath = os.getcwd()
filePath = currentPath+"/prank"
print(filePath)
def rename_file():
    file_list = filePath
    save_path = os.getcwd()
    print(save_path)
    tkinter.messagebox.showinfo("Say Hello", "Testing")
    os.chdir(filePath)
    to_remove = "0123456789"
    table = {ord(char): None for char in to_remove}
    for file_name in file_list:
        os.rename(file_name,file_name.translate(table))          
    print(file_list)
    os.chdir(save_path)
rename_file()

