#~!/usr/local/bin/python3
# BINF 6112 05Mar19
# Karen Lopez, Micaela Beckman
# group project PDB file parser
# joined scripts created by MB & KL
# added output file for saving helix & sheet structure counts in tab format
# changed output file for saving amino acid counts in tab format
# added code to create instances for all .pdb files in a given directory
# updated __str__ to handle files without organism name

from re import match, search

class PDBentry:
	#
	def __init__(self, file):
		self.file = file
		self.info = {}
		self.info['Sequence'] = ''
		chain = ''
		self.chains = []
		helix_chains = []
		sheet_chains = []
		#open file and iterate through lines to populate dictionary
		with open(self.file, 'r') as pdb:
			for line in pdb.readlines():
				l = line.split()

				#find & store ID to dictionary
				if match('HEADER', line):
					self.info['Toxin Peptide Name'] = l[-1]

				#find & store organism scientific to dictionary
				elif search('ORGANISM_SCIENTIFIC', line): #more than 1 in file			
					self.info['Scientific Name'] = ' '.join(l[3:]).rstrip(';')

				#find & store organism common name to dictionary
				elif search('ORGANISM_COMMON', line): #more than 1 in file					
					self.info['Common Name'] = ' '.join(l[3:]).rstrip(';')

				#find & store sequence to dictionary
				elif match('SEQRES', line):
					self.info['Sequence'] = self.info['Sequence'] + ' '.join(l[4:]) + ' '

				#find & store all chains to dictionary
				elif search('CHAIN:', line):
					chain = chain + ' '.join(l[3:]) + ' '
					chain = chain.replace(';', '').replace(',', '')
					self.info['Chains'] = chain.split(' ')[:-1]

				#find & append helix letters to list			
				elif match('HELIX', line):
					helix_chains.append(l[4])

				#find & append sheets letters to list
				elif match('SHEET', line):
					sheet_chains.append(l[5])
		
		#set the helix & sheet to remove duplicate
		self.helix_chains = set(helix_chains)
		self.sheet_chains = set(sheet_chains)
		
		#save length of helix & sheet sets to get counts		
		self.helix_count = len(self.helix_chains)
		self.sheet_count = len(self.sheet_chains)
		
		#open output file
		outfile = open("ScorpionSecondStructureCounts.txt", 'a')
		
		#write secondary sheet structure counts to output file
		outfile.write(self.info['Toxin Peptide Name'] + '\t' + str(self.helix_count) + '\t' + str(self.sheet_count) + '\n')
					

	def __str__(self):
		if 'Scientific Name' in self.info.keys():
			return self.info['Scientific Name']
		else:
			return 'Organism name not provided'
		
	def display(self):
		for i in self.info.keys():
			print(i + ' in PDB file is: {}'.format(self.info[i]))

	#iterate through sequence to get amino acid counts, access method?
	def aa_count(self):
		self.amino_acid = {}
		
		#create ss from sequence
		aa_List = self.info['Sequence'].split()
		
		#iterate through codon list, add to dictionary if new, else increment it's value
		for aa in aa_List:
			if aa not in self.amino_acid.keys():
				self.amino_acid[aa] = 1
			else:
				self.amino_acid[aa] += 1

		#open output file
		outfile =  open("ScorpionAminoAcidCounts.txt", 'a')
		
		#split dictionary and save as string
		for key, value in self.amino_acid.items():
			val = str(value)
			aa_dict = key.ljust(10), val.ljust(10)
			#write amino acid counts to output file in tab format
			outfile.write(self.info['Toxin Peptide Name'] + '\t' + '\t'.join(aa_dict) + '\n') #prints as dictionary - can clean up if needed

#calling methods across all files in a directory 
import os
directory='scorpion_data'
print(os.listdir(directory)) #check
for file in os.listdir(directory):
	if file.endswith('.pdb'):
		f = directory + '/' + file #added this to replace "with open(file) as f"
		print(f) #check
		#with open(file) as f:
		pdbtest=PDBentry(f)
		pdbtest.display()
		pdbtest.aa_count()
		print(pdbtest)	
	else:
		pass
	