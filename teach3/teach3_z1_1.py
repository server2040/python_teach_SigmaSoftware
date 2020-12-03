print('Please input value')

try:
 print('result: '+ str( (lambda x, y: x / y if y != 0 else None) ( float(input(' x: ')),float( input(' y: '))) )) 
except ValueError:
 print('Error: input value is not number')
