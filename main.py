# ---- / 
# --- / PASSWORD UPDATER  
# currently it requires **geckodriver** to be installed on the host running this script --> aint ideal!
# 
#

# --- / 
# -- / internal imports 
from file_handling import filename_set_timestamp, readFromFile,gatherFilePath
from dice_generation import generatePassword

# --- / 
# -- / external imports
from typing import Optional
import time 
import glob
import datetime
import os

def generate_password_for_each_device_in_list(host_file:str,length:int) -> bool:
    ''' 
    @param1 string, denotes file to generate passwords for 
    @param2 integer, denotes length of passwords ( amount of words per password)
    function checks whether file exists, ( raises exception if not!) and
    - reads every line 
    - generates a password per line 
    - writes the updated line to a new file, denoted with **param1**+timestamp
    @returns bool, **True** if successfull, **False** if error occurred
    
    '''
    
    file_path:str | None = gatherFilePath(host_file)
    if file_path == None:
        raise Exception("host_file was not found, aborting")
    
    # going through file
    #TODO Refactor 
    updated_lines:list[str] = []
    with open(file_path,"r",encoding="UTF-8") as hosts_file:
        for line in hosts_file:
            line =line.rstrip()
            password_for_line:str = generatePassword(length) 
            new_line = "{},{}".format(line,password_for_line)
            updated_lines.append(new_line)
            print( "updated password {}".format(new_line))
    
    # creating new file to update content
    new_file_path:str = filename_set_timestamp(file_path)
    try:
        write_list_to_file(new_file_path,updated_lines)
        return True
    except:
        return False
    
# --- / 
# -- / 

def write_list_to_file(filename:str,list_of_items:list[str])-> bool:
    '''
    @param1 string, denoting filename to write to 
    @param2 list[str], denoting which list to write to file
    function truncates and generates file and inserts every item of the list in **a newline**.
    @returns bool, **True** if successfull, **False** if errors occurred
     
    '''
    #TODO add backup-check
    try:
        with open(filename,"w",encoding='UTF-8') as new_file:
            for item in list_of_items:
                new_file.write("{}\n".format(item))
        return True
    except  Exception as error:
        raise error
        
     
    

def interface():
    '''
    this function acts as primary interface to access and operate this script 
    '''
    programmHeader = readFromFile("overview.txt")
    
    menuOptions= [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
    ]
    
    primaryLoop = True
    while primaryLoop:
        # executing loop of interface
        clearScreen()
        print(programmHeader)
        displayMenu(menuOptions)
        selection:int = int(input("enter an integer"))
        print("selected {} -> {}".format(selection,menuOptions[selection] ))
        break
        
def clearScreen():
    # taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python#2084628
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMenu(options): 
    
    for i in range(0,len(options)):
        print("{}. -- {}".format(i,options[i]))

# --- /
# -- / 
if __name__ == "__main__":
    print("executing script")
    generate_password_for_each_device_in_list("hosts",5)
    
    