# --- /
# -- /
#
#

# --- / 
# -- / external imports 
from typing import Optional
import time 
import glob
import datetime
import os

    
# --- /
# -- / 
def gatherFilePath(filename,recursiveSearch:bool=True) -> Optional[str]:
    ''' 
    function searching for **filename** in current directory
    searches **recursively** relative from root of **environment** -> finds files in a directory too.
    '''
    convertedQueryPath = "**/"+filename
    try:
        listOfFiles = glob.glob(convertedQueryPath,recursive=recursiveSearch)
        return listOfFiles[0];
    except: 
        return None 

# --- /
# -- / 

def readFromFile(filename:str) -> Optional[str]:
    '''
    takes a filepath as argument -> type **string**
    returns content of file or **None** if not found 
    '''
    filePath: Optional[str] = gatherFilePath(filename)
    if (filePath == None):
        return None
    # no error checking necessary, is checked with aboves if condition
    with open(filePath,"r") as foundFile:
        fileContent:str = foundFile.read()
    return fileContent

# --- /
# -- / 

def writeToFile(filename:str,input:str) -> bool :
    '''
    inserts given **input** to the given filename
    returns None if an error occured
    '''
    filePath: Optional[str] = gatherFilePath(filename)
    if (filePath == None):
        # no previous file was found:
        filePath = filename
    try:
        createBackup(filePath)
        with open(filePath,"w") as file:
            file.write(input)
        return True
    except Exception as exception:
        raise exception

# --- /
# -- /

def filename_set_timestamp(filename:str) -> str:
    '''
    @param string, takes filename and appends current date in the following format
    date = **Year_Month_day__HourMinute**
    returns string, filename+date
    '''
    
    current_date:str = datetime.datetime.today().strftime('%Y_%m_%d__%H%M')
    new_filename:str = "{}_from_{}".format(filename,current_date)
    return new_filename
        
# --- /
# -- / 

def createBackup(fileName):
    '''
    takes **filePath** and creates a new file containing this files content. 
    the new file is constructed as follows: **filePath**+ **date_backup**
    in case of errors, it returns **False**
    **True** otherwise
    '''
    currentDate:str = str(datetime.datetime.now())
    # suffix:str = ".backup"
    backupName:str = "oldPassword"
    fileContent:str | None = readFromFile(fileName)
    if (fileContent == None):
        return False
    newFileName:str = "{}_{}".format(backupName,currentDate)
    print("creating backup of file {}. Saving to --> {}".format(fileName,newFileName))
    writeToFile(newFileName,fileContent)
    
    return True

# --- /
# -- / 
