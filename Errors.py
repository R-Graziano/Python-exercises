try:
    typeErr = 'str' + 8
except TypeError:
    print('TypeError caused by concatenate a str with an int')

try:
    valErr = int('cadenaDeTexto')
except ValueError:
    print('ValueError caused by int() function cannot convert a word to an integer')

try:
    idxErr = [1,2,3,4]
    for i in range (6):
        idxErr[i]
except IndexError:
    print('IndexError caused by trying to access a list out of range')

try: 
#    syntError =
    raise SyntaxError
except SyntaxError:
    print('SyntaxError can be caused by the code at the right of the assign operator is empty')

try:
    assert False
except AssertionError:
    print('AssertionError caused by an assertion hardcoded to fail')

try:
    nameErr = 23
    print(nameEr)
except NameError:
    print('NameError caused by a variable name misspelled.')

try:
    raise OSError
except OSError:
    print('Any error can be raised using the raise keyword')

try:
    zeroDivErr = 1 / 0
except ZeroDivisionError:
    print('ZeroDivisionError is triggered when someone tries to divide by zero')
finally:
    print('There are many other ArithmeticErrors.')