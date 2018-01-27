#Python dictionary
#Program prints out a defiinition of an user input
#data.json contains dictionary

#imports
import json
import difflib

# Parsing json to python dictionary
data = json.load(open('data.json'))

def definition(word):
    suggestions = difflib.get_close_matches(word, data.keys())
    word = word.lower()
    i = 1
    if word in data:
        #Printing definitions
        for definition in data[word]:
            print(i,'. ', definition, sep='')
            i=i+1
    #Checking for a possible user input mistake
    elif suggestions :
        print('Did you mean',suggestions[0])
        ans = input("(Y/N)")
        if ans == 'n' or ans == 'N':
            exit(0)
        elif ans == 'Y' or ans =='y':
            for definition in data[suggestions[0]]:
                print(i, '. ', definition, sep='')
                i = i + 1

    else:
        print('Word not found, please try again.')


def main():
    #User input
    word = input('Type a word: ')
    #Dictionary function
    definition(word)

#Title
print('PYTHON INTERACTIVE DICTIONARY\n')

#Maintaining the program until the user says to stop it
while(1):
    main()
    q = input('Enter Q to exit program or any other key to continue: ')
    if q =='q' or q=='Q':
        print('Goodbye!')
        exit(0)
    else:
        continue