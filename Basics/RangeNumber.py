# genere une liste de 0 à 5 exclu
numbers = range(5)
# genere une liste de 5 à 10 exlcus
numbers = range(5,10)
# genere une liste de 5 à 10 exclus avec un pas de 2
# numbers = range(5,10,2)
print(numbers)
for number in numbers:
    print(number)
##### on aurait pu aussi bien coder sans la liste numbers directement avec range
print("range directement dans la boucle for ")
for number in range(3, 12, 2):
    print(number)