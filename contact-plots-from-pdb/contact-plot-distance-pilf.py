import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys

#~~~~~~~~~~~~~~
# GET PDB DATA
#~~~~~~~~~~~~~~

data = pd.read_csv('contact-points-distance-measurements-pilf.tsv', sep='\t', names=['i', 'j', 'dist'])
data = data.sort_values('dist', ascending=False)

x =  data['i'].tolist() + data['j'].tolist()
y = data['j'].tolist() + data['i'].tolist()

#make empty square matrix of dimensions = protein length 
mtx = np.empty((253, 253))
mtx.fill(np.nan)

for ind, row in data.iterrows():
	i = int(row['i'])
	j = int(row['j'])
	s = row['dist']
	mtx[i,j] = s
	mtx[j,i] = s

# TPR data : 
tpr1 = range(35, 70)
tpr2 = range(71, 103)
tpr3 = range(104, 138)
tpr4 = range(140, 173)
tpr5 = range(174, 208)
tpr6 = range(208, 240)

mx = max(data['dist'].tolist())
mn = min(data['dist'].tolist())

s = [((30-1)*((x-mn)/(mx-mn)))+1 for x in data['dist']]

#~~~~~~~~~~
# PLOTTING
#~~~~~~~~~~

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
	if n == -1:
		n = cmap.N
	new_cmap = mcolors.LinearSegmentedColormap.from_list('trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
	return new_cmap

cp = truncate_colormap(plt.get_cmap('Blues_r'), 0, 0.8)

fig, ax = plt.subplots()
abc = plt.scatter(x, y, marker='.', s=s+s, c=mtx[x,y], cmap=cp)

plt.scatter(tpr1, tpr1, marker='.', color='darkviolet', s=5)
plt.scatter(tpr2, tpr2, marker='.', color='darkviolet', s=5)
plt.scatter(tpr3, tpr3, marker='.', color='darkviolet', s=5)
plt.scatter(tpr4, tpr4, marker='.', color='darkviolet', s=5)
plt.scatter(tpr5, tpr5, marker='.', color='darkviolet', s=5)
plt.scatter(tpr6, tpr6, marker='.', color='darkviolet', s=5)

plt.colorbar(abc)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.ylim(252, 0)
plt.xlim(0, 252)
ax.set_aspect(252/252)
plt.tight_layout()
plt.savefig('pilf-contact-distance-plot', dpi=300)
plt.show()
