# ---- / 
# --- / PASSWORD UPDATER  
# currently it requires **geckodriver** to be installed on the host running this script --> aint ideal!
# 
#

# --- / 
# -- / internal imports 


# --- / 
# -- / external imports
from typing import Optional
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time 
import glob
import datetime


# --- /
# -- / 

def requestPassword(length:int) -> str | None:
    '''
    queries diceware.dmuth.org and retrieves a **password** consisting of **length** words
    returns password if successful -> type **string**
    else None at failure 
    '''
    # TODO better way to wait for result
    # executing search for item:
    try:
        # TODO Extract to loadWebsite()
        requestUrl = "https://diceware.dmuth.org/?debug={}&skip_animation".format(length)
        browser:object = webdriver.Firefox()
        browser.get(requestUrl)
        time.sleep(4)
    
        passwordFields = browser.find_element(By.CLASS_NAME, "results_phrase_value")
        extractedPassword = passwordFields.get_attribute("innerText")
        browser.quit()
        return extractedPassword
    except: 
        return None
    
# --- /
# -- / 

def setNewPassword(passwordLength:int) -> bool:
    '''
    acquires new password from diceware website and saves it to **newPassword** 
    returns **True** if successfull
    '''
    newPassword:str | None = requestPassword(passwordLength)
    if (newPassword == None):
        raise Exception("Password could not be obtained")
    writeToFile("newPassword",newPassword)
    return True
    
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
    if fileContent == None:
        return False
    newFileName:str = "{}_{}".format(backupName,currentDate)
    print("creating backup of file {}. Saving to --> {}".format(fileName,newFileName))
    writeToFile(newFileName,fileContent)
    
    return True

# --- /
# -- / 

def interface()

# --- /
# -- / 
if __name__ == "__main__":
    print("executing script")
    print(setNewPassword(5))
    
    # writeToFile("newPassword","Das sollte funktionieren")
    
    