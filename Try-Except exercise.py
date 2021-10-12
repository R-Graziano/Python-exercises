def readint(prompt, min, max):
#
# tu codigo aqui
#
    while True:
        try:
            num = int(input(prompt))
            assert min <= num <= max
            break
        except ValueError:
            print("Error: entrada incorrecta")
        except AssertionError:
            print("Error: el valor no está dentro del rango permitido (",min,"..",max,")")
        
    return num
    
v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)