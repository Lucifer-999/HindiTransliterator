#!/usr/bin/python

import argparse

# Function to parse arguments
def parse_args () :

    parser = argparse.ArgumentParser(description="Hindi Transliteration tool")
    parser.add_argument ( "-s", help = "String to be Transliterated", required=True, nargs=1 )
    return parser.parse_args()

# Dictionaries for storing corresponding hindi characters
dict = { 
    'b' : '\U0000092c', 'c' : '\U00000915', 'd' : '\U00000926', 'f' : '\U0000092b', 'g' : '\U00000917', 'h' : '\U00000939', 'j' : '\U0000091c', 'k' : '\U00000915', 'l' : '\U00000932', 'm' : '\U0000092e', 'n' : '\U00000928', 'p' : '\U0000092a', 'q' : '\U00000915\U0000094d\U00000935', 'r' : '\U00000930', 's' : '\U00000938', 't' : '\U00000924', 'v' : '\U00000935', 'w' : '\U00000935', 'x' : '\U00000915\U0000094d\U00000938', 'y' : '\U0000092f', 'z' : '\U0000095b', 
    'kh' : '\U00000916', 'gh' : '\U00000918' , 'ch' : '\U0000091a', 'chh' : '\U0000091b', 'jh' : '\U0000091d', 'th' : '\U00000922', 'dh' : '\U00000927', 'ph' : '\U0000092b', 'bh' : '\U0000092d', 'sh' : '\U00000936', 'ce' : '\U00000938', 
    'a' : '\U00000905', 'aa' : '\U00000906', 'e' : '\U0000090f', 'ee' : '\U00000908', 'i' : '\U00000907', 'ii' : '\U00000908', 'o' : '\U00000913', 'oo' : '\U0000090a', 'u' : '\U00000909', 'uu' : '\U0000090a', 'ai' : '\U00000910', 'au' : '\U00000914', 'ea' : '\U00000908', 'ou' : 'U/00000914'
    }
    
# Dictionary for Corresponding Sound Characters
sound = {
    'a' : '', 'aa' : '\U0000093e', 'e' : '\U00000947', 'ee' : '\U00000940', 'i' : '\U0000093f', 'o' : '\U0000094a', 'oo' : '\U00000942', 'u' : '\U00000941', 'ea' : '\U00000940', 'ii' : '\U00000940', 'uu' : '\U00000942', 'ai' : '\U00000948', 'au' : '\U0000094c', 'ou' : '\U0000094c'
    }
    
    
#Lists for checking if the character is Vowel / Consonant / Special Sound
consonants = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' ]
vowels = [ 'a', 'e', 'i', 'o', 'u' ]
special = [ 'kh', 'gh', 'ch', 'chh', 'jh', 'th', 'dh', 'ph', 'bh', 'sh', 'ce', 'aa', 'ee', 'oo', 'ea', 'ii', 'uu', 'ai', 'au', 'ou' ]

# Parsing the arguments passed
args = parse_args()
string = args.s[0]

# Initialisation and storing values
string = str( string )
string = string.lower() + ' '
trans = []


# Conversion Loop
for i in range(len(string)):

    if i==0 :    trans.append(dict[string[i]])
    
    elif string[i] in vowels :
    
        if string[i-1] in consonants:
            trans.append(sound[string[i]])
            if string[i] == 'a' and string[i+1] == ' ' :
                trans.append(sound['aa'])
            
        elif string[i-1]+string[i] in special :
            trans.pop()
            if i == 1 or string[i-2] == ' ' :
                trans.append(dict[string[i-1]+string[i]])
            else :
                trans.append(sound[string[i-1]+string[i]])
            
        else :
            trans.append(dict[string[i]])
    
    elif string[i] in consonants :
        
        if string[i-1]+string[i] in special :
            if trans[-1] == '\U0000094d' : trans.pop()
            trans.pop()
            trans.append(dict[string[i-1]+string[i]])
            
        elif string[i+1]  != ' ' and string[i+1] not in vowels and string[i+1] != 'a' :
            trans.append(dict[string[i]])
            trans.append('\U0000094d')
            
        else:
            trans.append(dict[string[i]])
        
    else:
        trans.append(string[i])

# Print Loop, can be integrated with conversion loop
for i in trans:
    print ( i, end='' )