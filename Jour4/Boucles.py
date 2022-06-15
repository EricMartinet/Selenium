# range == plage de valeur
print(range(4))
# correspond à [0, 1, 2, 3]             4 étant le nombre total d'éléments
for i in range(4):
    print(i)
print("for i in [0, 1, 2, 3]:")
for i in [0, 1, 2, 3]:
    print(i)
print("for elt in tableau:")
tableau = [1, "e", 3.14, 5]
for elt in tableau:
    print(elt)
print("for lettre in mot:")
mot = "LeJoliMot"
for lettre in mot:
    print(lettre)
print("for i in range(len(mot)):")
for i in range(len(mot)):
    print(mot[i])
#    print(str(i)+" -> "+mot[i])