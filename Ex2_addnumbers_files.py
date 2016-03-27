import os
import string
import random

def addnumbers_files():
    file_list = os.listdir(r"C:\Users\kiking\Desktop\Udacity\python\alphabet\alphabet")
    save_path = os.getcwd()
    os.chdir(r"C:\Users\kiking\Desktop\Udacity\python\alphabet\alphabet")

    for file_name in file_list:
        char = string.digits
        size = 2
        os.rename(file_name, file_name.join(random.choice(char) for _ in range(size)))

    os.chdir(save_path)

addnumbers_files()
