


def my_file(fname: str, text: str) -> list:
    '''
    The function takes a file path and a string.
    The function writes to the bytearray file from the received string,
    then it reads the file and returns a list of characters
    in the original string in byte representation.
    '''
    
    text_read = ''

    try:

        with open(fname,'wb') as f:
            f.write( bytearray(text, 'utf-8') )

        with open(fname,'rb') as f:
            text_read = f.read()

    except FileNotFoundError as e:
        print('Error:', str(e) )

    return list(text_read)


print( my_file('test.txt', 'Hello Python') )


