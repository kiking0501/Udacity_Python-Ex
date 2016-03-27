#check profanity words

import urllib
 
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" +text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    

def read_text():
    quotes = open(r"C:\Users\kiking\Desktop\Udacity\python\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close() 
    check_profanity(contents_of_file)

read_text()
