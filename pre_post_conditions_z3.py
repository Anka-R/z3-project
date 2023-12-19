from z3 import *

def random_code(x, y):
    # Déclaration des variables
    maxVal = Int('maxVal')
    equals = Bool('equals')

    # Solveur Z3
    solver = Solver()

    # Ajout des préconditions
    solver.add(Or(x < y, x > y, x == y))

    # Exécution du code Python dans Z3
    solver.add(If(x < y, maxVal == y, If(x > y, maxVal == x, And(equals, maxVal == 0))))

    # Ajout des postconditions
    solver.add(If(Not(equals), maxVal == max(x, y), maxVal == 0))

    # Vérification des contraintes
    result = solver.check()

    # Affichage du résultat
    if result == sat:
        print("Les pré-post conditions sont satisfaites !")
    else:
        print("Les pré-post conditions ne sont pas satisfaites !")

if __name__ == "__main__":
    random_code(5, 3)
