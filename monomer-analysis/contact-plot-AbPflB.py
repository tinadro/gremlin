import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys

data = 'other-e-proteobacteria/AbPflB-contact-prediction-scores.tsv'

#~~~~~~~~~~~~~~~~~~
# GET GREMLIN DATA
#~~~~~~~~~~~~~~~~~~

gremlin = pd.read_csv(data, sep='\t')
print(len(gremlin))
#gremlin = gremlin[gremlin['s_sco'] > 1]
gremlin.sort_values('s_sco', inplace=True)
print(len(gremlin))

x = gremlin['i'].tolist() + gremlin['j'].tolist()
y = gremlin['j'].tolist() + gremlin['i'].tolist()
sco = gremlin['s_sco'].tolist() + gremlin['s_sco'].tolist()

#make empty square matrix of dimensions = protein length 
mtx = np.empty((696, 696))
mtx.fill(np.nan)

for ind, row in gremlin.iterrows():
	i = row['i']
	j = row['j']
	s = row['s_sco']
	mtx[i,j] = s
	mtx[j,i] = s

s = [10*n for n in sco]

# TPR data : 
tpr1 = range(96, 129)
tpr2 = range(133, 166)
tpr3 = range(171, 204)
tpr4 = range(206, 239)
tpr5 = range(243, 276)
tpr6 = range(349, 382)
tpr7 = range(384, 417)
tpr8 = range(420, 453)


#~~~~~~~~~~
# PLOTTING
#~~~~~~~~~~

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
	if n == -1:
		n = cmap.N
	new_cmap = mcolors.LinearSegmentedColormap.from_list('trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
	return new_cmap

cp = truncate_colormap(plt.get_cmap('winter_r'), 0.05, 1)

fig, ax = plt.subplots()
abc = plt.scatter(x, y, marker='.', s=15, c=mtx[x,y], cmap=cp)
plt.scatter(tpr1, tpr1, marker='.', color='deeppink', s=2)
plt.scatter(tpr2, tpr2, marker='.', color='deeppink', s=2)
plt.scatter(tpr3, tpr3, marker='.', color='deeppink', s=2)
plt.scatter(tpr4, tpr4, marker='.', color='deeppink', s=2)
plt.scatter(tpr5, tpr5, marker='.', color='deeppink', s=2)
plt.scatter(tpr6, tpr6, marker='.', color='deeppink', s=2)
plt.scatter(tpr7, tpr7, marker='.', color='deeppink', s=2)
plt.scatter(tpr8, tpr8, marker='.', color='deeppink', s=2)
plt.colorbar(abc)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.ylim(696, 0)
plt.xlim(0, 696)
ax.set_aspect(696/696)
plt.tight_layout()
plt.savefig('../gremlin-plots/e-proteobacteria/AbPflB-gremlin-plot', dpi=300)
plt.show()
