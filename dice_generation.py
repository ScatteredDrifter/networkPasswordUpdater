# --- /
# -- / 

# --- / 
# -- / external imports 
from os import error
import random 
from io import open
import re

# --- / 
# -- / internal imports
from file_handling import gatherFilePath

# procedures to follow:
# - roll dices for N-words
# - cryptographically secure however 
# - read out the list but get only the words with the matching number of it


# --- / 
# -- / 

def roll_dice() -> int:
    '''
    rolls a dice (from 1,6) by utilizing **systemcall** for random generator
    @returns int
    '''
    # initializing random gen 
    system_random = random.SystemRandom()
    return system_random.randint(1,6)

# --- / 
# -- / 

def roll_n_times(n:int) -> list[int]:
    '''
    rolls dice **n** times 
    @returns 
    @return list with **n** entries as **int**
    '''
    array_of_numbers: list[int] = []
    for i in range(0,n):
        rolled_number = roll_dice()
        array_of_numbers.append(rolled_number)
    return array_of_numbers

# --- / 
# -- / 

def roll_word() -> int:
    '''
    function rolling dices 5 times 
    '''
    
    list_of_rolled_nums = roll_n_times(5)
    
    concatenated_number:int = 0
    number_position = 0
    for dice in list_of_rolled_nums:
        concatenated_number += (10**number_position) * dice
        # increasing position
        number_position +=1
    return concatenated_number

# --- / 
# -- / 

def get_word_from_list(word_number:int,file_path:str) -> str | None:
    '''
    looking up word from file supplied
    '''
    try:
        validated_file_path:str | None = gatherFilePath(file_path)
        assert (validated_file_path != None)
    except error:
        raise error
        
    # given_path:str = "dicepasswords/diceware_wordlist.txt"
    with open(validated_file_path,'r',encoding='UTF-8') as file:
        word = None
        for line in file:
            if str(word_number) in line:
                word = line
    return word
    
# --- / 
# -- / 

def generatePassword(n:int) -> str:
    '''
    takes **n** words from provided word-liste and forms a string out of it 
    @returns String containing all Words
    '''
    # TODO improve selection of file --> 
    filepath = "diceware_long_wordlist.txt"
    
    # list_of_words:list[str] = []
    resulting_word:str =""
    for i in range(0,n):
        word_number = roll_word()
        received_word = get_word_from_list(word_number,filepath)
        
        if received_word == None:
            raise Exception("could not read file {}".format(filepath))
        received_word = convert_string_to_word(received_word)
        # capitalied_letter = received_word[0].upper()
        # capitalized_word = capitalied_letter + received_word[1:]
        # list_of_words.append(received_word)
        resulting_word+= received_word
    
    # converting list of strings to single Word
    # print(list_of_words)
    return resulting_word

# --- / 
# -- / 

def select_wordlist() -> str:
    ''' 
    function listing available wordlists to choose from
    @returns string denoting choosen list
    '''
    decision:str = ""
    return decision

# --- / 
# -- / 

def convert_string_to_word(string:str) -> str:
    '''
    '''
    cleaned_string = remove_characters_from_word(string)
    formatted_word = capitalize_letter(cleaned_string)
    
    return formatted_word

# --- / 
# -- / 

def capitalize_letter(string_to_capitalize:str) -> str:
    ''' 
    '''
    processed_string:str = string_to_capitalize[0].upper() + string_to_capitalize[1:]
    
    return processed_string

# --- / 
# -- / 

def remove_characters_from_word(unprocessed_string:str) -> str :
    '''
    function cleanses numbers, whitespaces and newline characters form obtained string
    @param1 string containing unprocessed string
    @return string, processed string
    
    ### example usage:
    remove_characters_from_word("1234213   heythere\\n") -> "heythere"
    '''
    
    # stripping number and whitespaces
    processed_line = re.sub(r"\d+\s+","",unprocessed_string)
    # stripping newline characters
    processed_line = re.sub(r"\n+","",processed_line)
    return processed_line

# --- / 
# -- / 
    
if __name__ =="__main__":
    print("should not be runned, its a library")
    
    # exit("exiting program")
    
    # print(roll_n_times(5))
    sample_number = roll_word()
    print(generatePassword(4))
    