#!/usr/bin/env python3
#Micaela Beckman
#March 22, 2019


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab

snake_data = pd.read_csv('/users/micaelabeckman/desktop/SnakeAminoAcidCounts.txt',sep='\t')
snake_data.columns=['SampleID','Residue','Count']
snake_data.set_index('Residue','SampleID')
sorted_sndata=snake_data.sort_values(by='Residue',axis=0,ascending=True, inplace=False)
print(sorted_sndata.head(10)) 

x=sorted_sndata.Residue
y=sorted_sndata.Count
fname='snakeaminograph.pdf'
plot1 = plt.bar(x,y)
plt.xticks(rotation=45)
plt.tight_layout()
#pylab.show(plot1)
pylab.savefig(fname)



