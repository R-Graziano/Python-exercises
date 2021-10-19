text = input('Ingresa un texto: ')
textInverted = ''

text = text.lower()
text = text.replace(' ','')

for i in range(1,len(text)+1):
    textInverted += text[-i]

print(textInverted)

if textInverted == text and not(text.isspace()):
    print('Es un palindromo.')
else:
    print('No es un palindromo.')