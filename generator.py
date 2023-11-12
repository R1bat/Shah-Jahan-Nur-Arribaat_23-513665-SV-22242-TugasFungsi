# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:02:29 2023

@author: Arribaat
"""
#import os
import os
#import time
import time

#fungsi greet
def greet():
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    title = "TEXTS"
    description = "WE STORE TEXTS FOR YOU"
    separator = "-" * 60

    print(separator.center(90))
    print(f"{BOLD}{title.center(90)}{RESET}")
    print(f"{UNDERLINE}{description.center(90)}{RESET}")
    print("ANYWHERE ANYTIME".center(90))
    print(separator.center(90))
    print("")

#fungsi inisiasi program sekaligus penyatu fungsi
def init():
    global var_read
    print('PRESS "Q" TO QUIT FROM THIS PROGRAM')
    var_read = input("Do you want to open your existing text? [Y/N]: ")
    print("")
    if var_read.lower() == "y":
        print("Please insert your text name")
        global file_name
        file_name = input("Your text name: ")
        file_name += ".txt"
        print("")
        time.sleep(2)
        try :
            open(file_name,"r")
            os.system('cls')
            greet()
            open_text()
        except:
            print("You dont have any text yet, please create a text")
            print("")
            time.sleep(2)
            os.system('cls')
            greet()
            init()
      
    elif var_read.lower() == "n":
        print("Please create a new text name")
        global new_file
        new_file = input("Text name : ")
        new_file += ".txt"
        time.sleep(2)
        try:
            open(new_file,"r")
            file_exist = True
        except:
            file_exist = False
        
        if file_exist == True:
            print("Text already exist, please create a uniqe name")
            print("")
            time.sleep(2)
            os.system('cls')
            greet()
            init()
        elif file_exist == False:
            print("Loading..")
            time.sleep(2)
            os.system('cls')
            greet()
            add_text()
            
    elif var_read.lower() == "q":
        ext(var_read)

    else:
        print("Invalid input, please try again")
        print("")
        time.sleep(2)
        os.system('cls')
        greet()
        init()   

#fungsi menambahkan data
def add_text():
    open(new_file, "x")
    print("Succesfull")
    print("")
    time.sleep(2)
    os.system('cls')
    greet()
    init()
    
#fungsi menampilkan data
def open_text():
    try:
        with open(file_name, "r") as file:
            global content
            content = file.read()
            print(content)
        print("")
        print('PRESS "Q" TO QUIT FROM THIS PROGRAM')
        check_edit = input("Do you want to edit your text? [Y/N]: ")
        if check_edit.lower() == "y":
            print("")
            os.system('cls')
            greet()
            edit_text()
        elif check_edit.lower() == "n":
            print("")
            os.system('cls')
            greet()
            init()
        elif var_read.lower() == "q":
            n = "q"
            ext(n)
        else :
            print("Invalid input")
            init()
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        print("")
        time.sleep(2)
        os.system('cls')
        greet()
        init()

#fungsi edit data
def edit_text():
    print(content)
    print("")
    append_file = input("Pleases add your content:\n")
    with open(file_name,"a") as filex:
        filex.write(" ")
        filex.write(append_file)
    print("")    
    os.system('cls')
    greet()
    open_text()

def ext(n):
    if n.lower == "q":
        exit()

#pemanggilan fungsi supaya aplikasi berjalan
greet()
init()