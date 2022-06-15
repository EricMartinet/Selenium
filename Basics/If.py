#
temperature = int(input("Saisir la temperature : "))

if temperature > 30:
    print("It's a hot day")
    print('It\'s a very hot day ')
elif temperature > 20:
    print("temperature entre 20 et 30")
elif temperature > 10: # (10, 20]
    print("il fait froid")
print("cette instruction s'effectue tout le temps")
