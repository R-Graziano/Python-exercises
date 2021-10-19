def findWordInText(word, text):
    word = word.lower()
    text = text.lower()
    
    for c in word:
        if text.find(c) == -1:
            return 'No'
            break
        else:
            text = text[text.find(c):]
            
        
    return 'Si'
        
    

word = input('Enter a word:')
text = input('Enter a text:')

print(findWordInText(word,text))