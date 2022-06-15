weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
while not ( unit.lower() == 'l' or unit.lower() == 'k'):
    unit = input("(K)g or (L)bs: ")
if unit.lower() == 'l':
    weightInKg = weight * .45
    print("Weight in Kg: " + str(weightInKg))
else:
    weightInLb = weight / .45
    print("Weight in Lbs: " + str(weightInLb))
