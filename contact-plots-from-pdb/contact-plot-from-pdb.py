import sys 
import Bio.PDB
import numpy

pdb_id = sys.argv[1]
pdb_filename = pdb_id+'.pdb'

def calc_residue_dist(residue_one, residue_two) :
    """Returns the C-alpha distance between two residues"""
    diff_vector  = residue_one["CA"].coord - residue_two["CA"].coord
    return numpy.sqrt(numpy.sum(diff_vector * diff_vector))

def calc_dist_matrix(chain_one, chain_two) :
    """Returns a matrix of C-alpha distances between two chains"""
    answer = numpy.zeros((len(chain_one), len(chain_two)), numpy.float)
    for row, residue_one in enumerate(chain_one) :
        for col, residue_two in enumerate(chain_two) :
            answer[row, col] = calc_residue_dist(residue_one, residue_two)
    return answer
 
structure = Bio.PDB.PDBParser().get_structure(pdb_id, pdb_filename)
model = structure[0]

print(structure)
print(model)

print(type(structure))
print(type(model))
