# afficher
print("Aloha")

#
annee_naissance = input("saisissez votre année de naissance ")
# age = 2022 - annee_naissance  => crash car essaie de soustraire int avec str
# convertir en int avec la fonction int()
age = 2022 - int(annee_naissance)
# print("Votre age est : "+ age) => crash car essaie de concatener str avec int
# convertire int en str avec str()
print("Votre age est : "+ str(age))

# ajouter deux nombres :
nb1 = input("Saisir nombre 1: ")
nb2 = input("Saisir nombre 2: ")
# si j'essaie d'ajouter les deux ensembles... fail : concatenation à la place
sum = nb1 + nb2
print("leur somme est : "+ sum)
#
print("j'essaie encore...")
# sum = int(nb1) + int(nb2) => crash si nb est un float
# convertir les nombres en float
sum = float(nb1) + float(nb2)
print("leur somme est : "+ str(sum))

# on peut encore faire autrement en convertissant directement en float les variables saisies
nb1 = float(input("Saisir nombre 1: "))
nb2 = float(input("Saisir nombre 2: "))
sum = nb1 + nb2
print("leur somme est : "+ str(sum))