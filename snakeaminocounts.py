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
print(snake_data.head(10)) 

x=snake_data.Residue
y=snake_data.Count
fname='snakeaminograph.pdf'
plot = plt.scatter(x,y)
plt.xticks(rotation=45)
plt.tight_layout()
pylab.savefig(fname)

