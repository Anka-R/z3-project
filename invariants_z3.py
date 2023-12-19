from z3 import *

def check_invariants(x, y):
    # Création des variables Z3
    x_val = Int('x_val')
    y_val = Int('y_val')
    maxVal = Int('maxVal')
    equals = Bool('equals')

    # Création du solveur Z3
    solver = Solver()

    # Initialisation des variables avec les valeurs fournies
    solver.add(x_val == x)
    solver.add(y_val == y)
    solver.add(maxVal == 0)
    solver.add(equals == False)

    # Expression des conditions du code en tant que contraintes logiques
    cond1 = Implies(x_val < y_val, maxVal == y_val)
    cond2 = Implies(x_val > y_val, maxVal == x_val)
    cond3 = Implies(x_val == y_val, equals == True)

    # Ajout des contraintes au solveur
    solver.add(Or(cond1, cond2, cond3))

    # Vérification des invariants
    result = solver.check()

    if result == sat:
        print("Les invariants sont satisfaits.")
    else:
        print("Les invariants ne sont pas satisfaits.")

if __name__ == "__main__":
    check_invariants(5, 3)
