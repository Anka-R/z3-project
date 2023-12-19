from z3 import *

def generate_test_cases():
    # Déclaration des variables entières x et y
    x = Int('x')
    y = Int('y')

    # Solveur Z3
    solver = Solver()

    # Contrainte pour le premier chemin (x < y)
    solver.add(x < y)

    # Vérifier si le solveur a une solution
    if solver.check() == sat:
        model = solver.model()
        x_value = model[x].as_long()
        y_value = model[y].as_long()
        print(f"Cas de test généré : maxValue({x_value}, {y_value})")

    # Réinitialiser le solveur pour le chemin suivant
    solver.reset()

    # Contrainte pour le deuxième chemin (x > y)
    solver.add(x > y)

    # Vérifier si le solveur a une solution
    if solver.check() == sat:
        model = solver.model()
        x_value = model[x].as_long()
        y_value = model[y].as_long()
        print(f"Cas de test généré : maxValue({x_value}, {y_value})")

    # Réinitialiser le solveur pour le chemin suivant
    solver.reset()

    # Contrainte pour le troisième chemin (x == y)
    solver.add(x == y)

    # Vérifier si le solveur a une solution
    if solver.check() == sat:
        model = solver.model()
        x_value = model[x].as_long()
        y_value = model[y].as_long()
        print(f"Cas de test généré : maxValue({x_value}, {y_value})")

if __name__ == "__main__":
    generate_test_cases()
