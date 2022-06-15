names = ['John', "Bob", "Mosh", "Sam", "Pamela"]
print(names)
print(names[0])
# dernier element de la liste
print(names[-1])
# l'avant dernier
print(names[-2])
# les premiers elements de la liste sans le dernier
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
# ajouter un élément à la fin de la liste avec append
numbers.append(6)
print(numbers)
# insérer un élément
numbers.insert(0, 'a')
print(numbers)
# suprrimer un element de la liste
numbers.remove(3)
print(numbers)
# vérifier un élément de la liste      cequejecherche in maListe
print(10 in numbers)
# le nombre d'items de la liste avec     len( var )
print("la liste est constituée de "+ str(len(numbers)) +" éléments")
# supprimer tous les éléments de la liste
numbers.clear()
print(numbers)