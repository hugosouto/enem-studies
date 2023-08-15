from rdkit import Chem
from rdkit.Chem import Draw

def to_smiles(notation):
    
    # TODO: Replace to a GPT converter from molecular structure to SMILES 
    # notation.

    # Replace common patterns with corresponding SMILES notation
    smiles = (
        notation
        .replace("CH3", "C")
        .replace("(CH)2", "CC")
        .replace("(CH3)", "C(C)")
        .replace("CH2", "C")
        .replace("CO", "C(=O)")
        .replace("NH2", "N")
        .replace("NH", "NC")
        .replace("C6H5", "c1ccccc1")
    )
    return smiles

# Test notations
notations = [
    "CH3–(CH)2–CH(OH)–CO–NH–CH3",
    "CH3–(CH)2–CH(CH3)–CO–NH–CH3",
    "CH3–(CH)2–CH(CH3)–CO–NH2",
    "CH3–CH2–CH(CH3)–CO–NH–CH3",
    "C6H5–CH2–CO–NH–CH3",
]

# Convert to SMILES and print results
smiles_notations = [to_smiles(notation) for notation in notations]
print('smiles_notations list:', smiles_notations)

# Creating the molecule structure

for molecule_structure in smiles_notations:
    # Test i
    print('molecule_structure:', molecule_structure)

    # Creating a molecule object
    # molecule = Chem.MolFromSmiles(molecule_structure)

    # Drawing the molecule
    # molecule_image = Draw.MolToImage(molecule)
    # molecule_image.show()

    # TODO: Make Draw.MolToImage(molecule) work for the whole molecule, not 
    # only for the first atom.
