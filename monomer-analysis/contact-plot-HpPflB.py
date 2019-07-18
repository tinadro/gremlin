import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys

data = 'other-e-proteobacteria/HpPflB-contact-prediction-scores.tsv'

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
mtx = np.empty((844, 844))
mtx.fill(np.nan)

for ind, row in gremlin.iterrows():
	i = row['i']
	j = row['j']
	s = row['s_sco']
	mtx[i,j] = s
	mtx[j,i] = s

s = [10*n for n in sco]

# TPR data : 
tpr1 = range(29, 62)
tpr2 = range(70, 103)
tpr3 = range(108, 141)
tpr4 = range(143, 176)
tpr5 = range(308, 341)
tpr6 = range(342, 375)
tpr7 = range(468, 501)
tpr8 = range(502, 535)
tpr9 = range(604, 637)
tpr10 = range(640, 673)
tpr11 = range(682, 715)
tpr12 = range(716, 749)
tpr13 = range(751, 784)
tpr14 = range(785, 818)

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
plt.scatter(tpr9, tpr9, marker='.', color='deeppink', s=2)
plt.scatter(tpr10, tpr10, marker='.', color='deeppink', s=2)
plt.scatter(tpr11, tpr11, marker='.', color='deeppink', s=2)
plt.scatter(tpr12, tpr12, marker='.', color='deeppink', s=2)
plt.scatter(tpr13, tpr13, marker='.', color='deeppink', s=2)
plt.scatter(tpr14, tpr14, marker='.', color='deeppink', s=2)
plt.colorbar(abc)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.ylim(844, 0)
plt.xlim(0, 844)
ax.set_aspect(844/844)
plt.tight_layout()
plt.savefig('../gremlin-plots/e-proteobacteria/HpPflB-gremlin-plot', dpi=300)
plt.show()
