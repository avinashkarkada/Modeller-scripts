from modeller import *
from modeller.scripts import complete_pdb
import os

env = Environ()
env.io.atom_files_directory = ['.', '../atom_files']
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')


current_dir = os.getcwd()
files = os.listdir(current_dir)
pdb_files = [f for f in files if f.endswith('.pdb')]
final_dope = []

for pdb_file in pdb_files:
    mdl = complete_pdb(env, pdb_file)
    atmsel = selection(mdl.chains[0])
    score = atmsel.assess_dope()
    fin = (pdb_file, score)
    final_dope.append(fin)


print(final_dope)
