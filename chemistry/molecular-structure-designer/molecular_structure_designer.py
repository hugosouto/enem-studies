from rdkit import Chem
from rdkit.Chem import Draw

# Creating the molecule structure
molecule_structure = "CC(O)CC(=O)NC"

# Creating a molecule object
molecule = Chem.MolFromSmiles(molecule_structure)

# Drawing the molecule
molecule_image = Draw.MolToImage(molecule)
molecule_image.show()
