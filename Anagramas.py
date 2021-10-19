text1 = input('Ingresa un texto: ')
text2 = input('Ingresa otro texto: ')


def stringToList(text):
    text = text.lower().replace(" ","")
    listText = []
    for c in text:
        listText.append(c)
    
    return listText


def anagrama(text1, text2):
    list1 = stringToList(text1)
    list2 = stringToList(text2)
    
    list1.sort()
    list2.sort()
    
    if len(list1) != len(list2):
        print('No son anagramas.')
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return 'No son anagramas.'
        return 'Son Anagramas.'
    

print(anagrama(text1,text2))

