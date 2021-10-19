def sevenSegmentDisplay():
    entrada = -1
    
    sevenSegmentDisplayer = [['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###'],
                             ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
                             ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###'],
                             ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
                             ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']]
    

    while int(entrada) < 0:
        try:
            entrada = str(int(input('Ingrese un numero entero positivo:')))
        except ValueError:
            print("Tiene que ser un número...")
    
    for i in range(5):
        for num in entrada:
            print(sevenSegmentDisplayer[i][int(num)], end=' ')
        print()

sevenSegmentDisplay()