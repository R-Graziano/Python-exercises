def misplit(strng):
#
# coloca tu código aquí
#
    strngSplit = []
    curr = ""
    for c in strng:
        #print(strng.index(c),len(strng))
        if c.isspace():
            if curr != "":
                strngSplit.append(curr)
            curr = ""
        else:
            curr += c
    if curr != "":
        strngSplit.append(curr)
    
    return strngSplit

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))