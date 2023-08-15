from rdkit import Chem
from rdkit.Chem import Draw

# SMILES notations for the given structures
smiles_notations = [
    "CCC(O)C(=O)NC",
    "CCC(C)C(=O)NC",
    "CCC(C)C(=O)N",
    "CC(C)C(=O)NC",
    "c1ccccc1CC(=O)NC",
]

# Creating molecule objects
molecules = [Chem.MolFromSmiles(smiles) for smiles in smiles_notations]

# Drawing the molecules
molecule_images = Draw.MolsToGridImage(molecules, molsPerRow=2)
molecule_images.show()
