#!/usr/bin/env python3
#Micaela Beckman
#March 22, 2019


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab

scorpion_data = pd.read_csv('/users/micaelabeckman/desktop/ScorpionAminoAcidCounts.txt',sep='\t')
scorpion_data.columns=['SampleID','Residue','Count']
scorpion_data.set_index('Residue','SampleID')
sorted_data=scorpion_data.sort_values(by='Residue',axis=0,ascending=True, inplace=False)
print(sorted_data.head(10)) 

scx=sorted_data.Residue
scy=sorted_data.Count
scfname='scorpionaminograph.pdf'
plot3 = plt.bar(scx,scy)
plt.xticks(fontsize=7,rotation=45)
plt.tight_layout()
pylab.legend(loc='upper right')
pylab.savefig(scfname)