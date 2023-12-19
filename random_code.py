# Programme simple qui affiche l'entier le plus grand entre les deux passés en paramètres
def maxValue(x, y):
    maxVal = 0
    equals = False

    if (x < y):
        maxVal = y
    elif x > y:
        maxVal = x
    else:
        equals = True

    if equals:
        print("Les deux nombres sont égaux !")
    else:
        print("Le nombre le plus grand est " + str(maxVal) + " !")


if __name__ == "__main__":
    maxValue(-5, 3)