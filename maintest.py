# *args, **kwargs excersise

def myfunc(*args, **kwargs):
    for text in args:
        print(text, end=" ")
    print("\n Hasta aqui lo que contiene args")
    for k in kwargs:
        print(k, end=" ")
    print("\n Hasta aqui lo que contiene kwargs como keys")
    for k,v in kwargs.items():
        print("{} -> {}".format(k,v), end=" ")

    print("\n Hasta aqui lo que contiene kwargs como key -> value")

myfunc(1,2,3, a=3,b=2,c=1,d=4)
print("------")

my_list = [1, 2, 3]
print(*my_list)