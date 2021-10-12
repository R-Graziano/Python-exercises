print(""" Exercise 1
Create a new list that contains fruits names only starting with a vowel.
fruits = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']""", end='\n\n')

fruits = ['Apples', 'Oranges', 'Guavas', 'Grapes', 'Mangoes', 'Apricots', 'Olives']
fruitsStartingWithAVowel = [fruit for fruit in fruits if fruit[0] in ['A', 'E', 'I', 'O', 'U']]
print(fruitsStartingWithAVowel, end="\n------------------------------------\n")

print(""" Exercise 2
What is the result of the code given below?
print([char.upper() for char in "python"])""", end='\n\n')

print("Converts each char in the string to upper case and print the list.")
print([char.upper() for char in "python"], end="\n------------------------------------\n")



print("""Exercise 3
Implement multiplication of a matrix with a scalar number with LC.""", end='\n\n')

scalar = int(input("Enter a scalar number: "))
matrix = eval(input("Enter a matrix (you could use list comprehension or leave it blank to use \
         a default matrix): ") or "[[i+(row*3) for i in range(1,4)] for row in range (3)]")

print('\n', [[value*scalar for value in row] for row in matrix], sep="")