import pandas as pd 
import numpy as np 
import sys

infile = sys.argv[1]
pfl = infile.split('.')[0]
fname = pfl + '-tprpred.tsv'

accver = [] # list of acc.vers for every predicted tpr
tprstart = [] # start position of tpr motif
tprend = [] # end position of tpr motif (32 residues)
prot_len = [] # length of analysed protein 
e_prot = [] # whole-protein e-value 
p_rep = [] # per-repeat p-value for output of repeat residues
tprseq = [] # sequence of the tpr motif 

with open(infile, 'r') as f:
	i = 0
	for index, line in enumerate(f.readlines()):
		line = line.split()
		# extract all the different data for each hit into individual lists, so I can make a table out of this 
		if index % 2 == 0: #for odd lines, do this
			a = line[0].split('(')[0][1:] # accver of the protein
			accver.append(a)
			b = line[0].split('(')[1][:-1].split('-')[0] # start position of tpr motif
			tprstart.append(b)
			c = line[0].split('(')[1][:-1].split('-')[1] # end position of tpr motif
			tprend.append(c)
			d = line[1].split('=')[1] # length of accver protein 
			prot_len.append(d)
			e = line[2].split('=')[1] # per-protein evalue
			e_prot.append(e)
			f = line[3].split('=')[1] # per-repeat pvalue
			p_rep.append(f)
		elif index % 2 == 1:
			g = line[0]
			tprseq.append(g)
#		print(i)
		i += 1

reffile = '/project/home/td1515/2_trees/epsilon-PflAB-trees/'+pfl+'-protein-info.xlsx'
ref = pd.read_excel(reffile)
ref.drop_duplicates(subset='saccver', inplace=True)
print(ref.head())

org = []
strain = []
txid = []
sptxid = []

x = 0
# need to add species information:
for ele in accver:
	for ind, row in ref.iterrows():
		if ele in row['saccver']:
			org.append(row['organism_name'])
			strain.append(row['infraspecific_name'])
			txid.append(row['taxid'])
			sptxid.append(row['species_taxid'])
	print(x)
	x += 1	

# define a dictionary with keys being column titles, and values are the lists of data that will become each column
d = {'accver': accver, 'protein-evalue': e_prot, 'repeat-pvalue': p_rep, 'protein-len': prot_len, 'tpr-start': tprstart, 'tpr-end': tprend, 'tpr-seq': tprseq, 'organism': org, 'strain': strain, 'taxid': txid, 'species_taxid': sptxid}
df = pd.DataFrame(d)
df.to_csv(fname, sep='\t', index=False)


print('finished')
