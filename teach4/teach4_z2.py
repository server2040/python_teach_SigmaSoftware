

def replease_next(s: str, repl_symb='_') -> str:
    '''
    Return string in which all next occurrences of its first character
    are replaced with '_' (underscore) except for the very first character. 
    '''

    first_char = s[:1]
    return first_char + s[1:].replace(first_char, repl_symb)



## Print variant 1
#string = 'abracadabra'
#print(f"'{string}'\t-> '{replease_next(string)}'")

# Print variant 2
print( (lambda s: f"'{s}'\t-> '{replease_next(s)}'")('abracadabra') ) 



 