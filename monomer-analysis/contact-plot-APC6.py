import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys

data = 'other-tpr-proteins/apc6-contact-prediction-scores.tsv'

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
mtx = np.empty((620, 620))
mtx.fill(np.nan)

for ind, row in gremlin.iterrows():
	i = row['i']
	j = row['j']
	s = row['s_sco']
	mtx[i,j] = s
	mtx[j,i] = s

s = [10*n for n in sco]

# TPR data : 
tpr1 = range(231, 266)
tpr2 = range(267, 294)
tpr3 = range(299, 332)
tpr4 = range(334, 367)
tpr5 = range(368, 401)
tpr6 = range(402, 435)
tpr7 = range(446, 478)
tpr8 = range(479, 512)

tpra = range(3, 36)
tprb = range(130, 163)


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
plt.scatter(x, y, marker='.', s=15, c=mtx[x,y], cmap=cp)
plt.scatter(tpr1, tpr1, marker='.', color='darkviolet', s=2)
plt.scatter(tpr2, tpr2, marker='.', color='darkviolet', s=2)
plt.scatter(tpr3, tpr3, marker='.', color='darkviolet', s=2)
plt.scatter(tpr4, tpr4, marker='.', color='darkviolet', s=2)
plt.scatter(tpr5, tpr5, marker='.', color='darkviolet', s=2)
plt.scatter(tpr6, tpr6, marker='.', color='darkviolet', s=2)
plt.scatter(tpr7, tpr7, marker='.', color='darkviolet', s=2)
plt.scatter(tpr8, tpr8, marker='.', color='darkviolet', s=2)


plt.scatter(tpra, tpra, marker='.', color='deeppink', s=2)
plt.scatter(tprb, tprb, marker='.', color='deeppink', s=2)
# plt.colorbar()

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.ylim(620, 0)
plt.xlim(0, 620)
ax.set_aspect(620/620)
plt.tight_layout()
plt.savefig('../contact-plots/others/APC6-contact-plot', dpi=300)
plt.show()
