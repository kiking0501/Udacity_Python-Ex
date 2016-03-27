import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\kiking\Desktop\Udacity\python\alphabet\alphabet")
    print(file_list)
    save_path = os.getcwd()
    print("Current Working Directory is "+save_path)
    os.chdir(r"C:\Users\kiking\Desktop\Udacity\python\alphabet\alphabet")

    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " +file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)            
rename_files()
