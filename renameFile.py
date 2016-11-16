import os
def rename_file():
    file_list = os.listdir(r"E:\BOOKS\CS\FullStackWebsite\rename\prank")
    save_path = os.getcwd()
    print(save_path)
    os.chdir(r"E:\BOOKS\CS\FullStackWebsite\rename\prank")
    to_remove = "0123456789"
    table = {ord(char): None for char in to_remove}
    for file_name in file_list:
        os.rename(file_name,file_name.translate(table))          
    print(file_list)
    os.chdir(save_path)
rename_file()
