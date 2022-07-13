import json
from html_text import extract_text

# Function to read the articles from the JSON file
def readJSON(filename):
    with open(filename, 'r') as file:
        articles = json.load(file)
    return articles

def saveListToJSON(input_list, filename):
    # Open the file with filename (if it exists, it gets 
    # overwritten because of the use of w instead of a)
    with open(filename, 'w') as file:
        file.write('[\n')
        for index, list_el in enumerate(input_list):
            json.dump(list_el, file, indent=4, default=str)
            if index < len(input_list) - 1:
                file.write(',\n')
        file.write('\n]')
    file.close()