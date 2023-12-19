from z3 import *

def new_level():
    # Création des variables pour représenter les conditions
    new_val = Int('new_val')
    level = Int('level')

    # Déclaration des contraintes basées sur le code
    constraint1 = Or(new_val < 0, new_val > 0)
    constraint2 = level == If(new_val < 0, new_val * -1, new_val)
    constraint3 = level < 0

    # Solveur Z3
    solver = Solver()
    solver.add(constraint1)
    solver.add(constraint2)
    solver.add(constraint3)

    # Vérification de l'atteignabilité
    if solver.check() == sat:
        # Des modèles existent, ce qui signifie que le code est atteignable
        print("Le code est atteignable !")
        model = solver.model()
        print("Modèle :")
        print("new_val =", model[new_val])
        print("level =", model[level])
    else:
        # Aucun modèle trouvé, le code n'est pas atteignable
        print("Code non atteignable !")

if __name__ == "__main__":
    new_level()
