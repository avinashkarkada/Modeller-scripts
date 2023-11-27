# A sample script for fully automated comparative modeling
from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
env.io.hetatm = True
a = AutoModel(env,
              # file with template codes and target sequence
              alnfile  = 'alignment.seg',
              # PDB codes of the templates
              knowns   = ('7yiv'),
              # code of the target
              sequence = '1fdx')
a.auto_align()                      # get an automatic alignment
a.starting_model= 1                 # index of the first model
a.ending_model  = 4                 # index of the last model
a.make()                            # do comparative modeling
