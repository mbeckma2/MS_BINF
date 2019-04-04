#!/usr/bin/env python3
#Micaela Beckman
#March 22, 2019


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab

spider_data = pd.read_csv('/users/micaelabeckman/desktop/SpiderAminoAcidCounts.txt',sep='\t')
spider_data.columns=['SampleID','Residue','Count']
spider_data.set_index('Residue','SampleID')
sorted_spdata=spider_data.sort_values(by='Residue',axis=0,ascending=True, inplace=False)
print(sorted_spdata.head(10)) 

spx=sorted_spdata.Residue
spy=sorted_spdata.Count
spfname='spideraminograph.pdf'
plot2 = plt.bar(spx,spy)
plt.xticks(rotation=45)
plt.tight_layout()
pylab.show(plot2)
#pylab.savefig(spfname)