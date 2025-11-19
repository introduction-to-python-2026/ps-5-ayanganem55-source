def split_before_uppercases(formula):
    
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
   
    atom = ""
    number = ""

    for ch in formula:
        if ch.isdigit():
            number += ch
        else:
            atom += ch

    if number == "":
        number = 1
    else:
        number = int(number)

    return atom, number


def count_atoms_in_molecule(molecular_formula):

    atoms_count = {}

    # Step 1: Split by uppercase
    for atom_part in split_before_uppercases(molecular_formula):
        atom_name, atom_number = split_at_digit(atom_part)

        # Step 2: Add to dictionary
        if atom_name in atoms_count:
            atoms_count[atom_name] += atom_number
        else:
            atoms_count[atom_name] = atom_number

    # Step 3: Return final dictionary
    return atoms_count


def parse_chemical_reaction(reaction_equation):
   
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
   
    return [count_atoms_in_molecule(m) for m in molecules_list]
