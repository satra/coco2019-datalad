
import bids
layout = bids.BIDSLayout('/data/ds000003')
from nipype.interfaces.fsl import BET
res = BET(in_file=layout.get(subject='01', suffix='T1w', return_type='file')[0], 
          out_file='brain.nii.gz').run()
