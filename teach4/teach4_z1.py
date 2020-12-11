

def get_first_and_last_2symb(s: str) -> str:
    '''  Return string consist first and last 2 symbols in input string.  '''
    return s[:2] + s[-2:] if len(s)>=2 else ''


print('demonstration example strings:')
for string in ['Winter', 'r2', 'p']:
    print(f"'{string}'\t-> '{get_first_and_last_2symb(string)}'")
 
string = input('\ninput user string: ')
print(f"'{string}' -> '{get_first_and_last_2symb(string)}'")



 
