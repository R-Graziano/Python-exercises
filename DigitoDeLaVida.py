while True:
    try:
        fechaNacimiento = int(input('Ingresa tu fecha de nacimiento en formato AAAAMMDD, AAAADMM o MMDDAAAA: '))
        fechaNacimiento = str(fechaNacimiento)
        break
    except ValueError:
        print('No es una fecha valida.')

def stringToList(text):
    lista = []
    for c in text:
        lista.append(int(c))
    return lista

def digitoDeLaVida(fNacimiento):
    lifenumber = stringToList(fNacimiento)
        
    while True:
        if len(lifenumber) > 1:
            lifenumber = stringToList(str(sum(lifenumber)))
        else:
            return lifenumber[0]
            

print(digitoDeLaVida(fechaNacimiento))