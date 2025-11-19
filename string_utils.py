def split_before_uppercases(formula):
    """Splits a formula before each uppercase letter.
    Example: 'C6H12O6' → ['C6', 'H12', 'O6']"""
    parts = []
    current = ""

    for ch in formula:
        if ch.isupper() and current != "":
            parts.append(current)
            current = ch
        else:
            current += ch

    if current:
        parts.append(current)

    return parts


def split_at_digit(formula):
    """Splits a formula segment into atom and number.
    Examples:
        'H2' → ('H', 2)
        'Na' → ('Na', 1)
        'Cl3' → ('Cl', 3)
    """
    atom = ""
    number = ""

    for ch in formula:
        if ch.isdigit():
            number += ch
        else:
            atom += ch

    # If no number appears, quantity defaults to 1
    number = int(number) if number else 1
    return atom, number


def count_atoms_in_molecule(molecular_formula):
    """Returns a dictionary with element counts in a molecule."""
    atoms_count = {}

    # Step 1: Split the formula into parts like ['C6', 'H12', 'O6']
    for atom_part in split_before_uppercases(molecular_formula):
        atom_name, atom_number = split_at_digit(atom_part)

        # Step 2: Update the dictionary
        atoms_count[atom_name] = atoms_count.get(atom_name, 0) + atom_number

    return atoms_count


def parse_chemical_reaction(reaction_equation):
    """Splits a reaction equation into reactants and products."""
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Returns atom dictionaries for each molecule in a list."""
    return [count_atoms_in_molecule(m) for m in molecules_list]

