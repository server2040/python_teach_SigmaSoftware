
def ret_word_isaldijit(s: str) -> list:
    '''
    This is a function that takes a string and returns
    a list of words from this line, only which
    contain both numbers and letters
    '''

    words_all = s.split(' ')
    words_aldijit = []

    for word in words_all:
    
        digit_exist = False
        alpha_exist = False
    
        for char in word:
    
            if char.isalpha():
                alpha_exist = True
    
            elif char.isdigit():
                digit_exist = True
    
            if alpha_exist and digit_exist:
                words_aldijit.append(word)
                break
    
    return words_aldijit


print( ret_word_isaldijit('Dash100 apps are rendered in the web3 browser55') )


 
