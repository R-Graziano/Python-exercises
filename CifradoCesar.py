text = input('Ingresa un texto para encriptar: ')
encriptado = ""
key = 0
while key > 25 or key < 1:
    try:
        key = int(input('Ingresa un valor de cambio entre 1 y 25: '))
    except ValueError:
        print('No es un entero válido.')

for c in text:
    if 65 <= ord(c) <= 90:
        if ord(c)+key > 90:
            c = chr(65+key)
        else:
            c = chr(ord(c)+key)
    elif 97 <= ord(c) <= 122:
        if ord(c)+key > 122:
            c = chr(97+key)
        else:
            c = chr(ord(c)+key)
    encriptado += c

print(encriptado)