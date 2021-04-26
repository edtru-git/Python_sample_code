

# Ed Trujillo

# programming task
# Creating a function that 
# 1. accepts a file name and search string parameter 
# 2. returns the number of times the search string appears in the file
# 3. accounts for user errors
# 4. lets the user decide when to quit searching 


import os
os.getcwd()
os.chdir('C:/Users/User/Desktop/code_sample/Python/project1')




#--------------------------------------------------------------
def count_instances_by_line(file_name, some_string):   
    """ Counts the instances a word appears in the file."""
    input_file=open(file_name,'r')                 
    lines= input_file.readlines()                  

    total_count=0                                   
    for a_line in lines:              
        if some_string in a_line:  
            total_count +=a_line.count(some_string)  

    input_file.close()                             
    return total_count




def ask_user():
    """Asks the user what file and word to search for. Returns the word count in that file."""
    try:
        file_name=input('Enter Text File Name (include file format(e.g., Dracula.txt)): ')
        some_string=input('Enter Text to Search For: ')
        resulting_count = count_instances_by_line(file_name,some_string)
    except:
        print('No file of that name found')
    else:
        string_in_string='{} appears in {} {} times'.format(some_string, file_name,resulting_count)
        print(string_in_string)
    
    
    
    
def search_fuct():  
    """Asks the user what file and word to search for. User chooses when to quit searching."""
    while True:
        resp = input("Search a word in text file? Yes or No?")
        while resp.lower() == "yes":
            ask_user()
            resp = input("Continue searching? Yes or No?")
        if resp.lower() == "no":
                break    
        else:
            print('Error')



search_fuct()






