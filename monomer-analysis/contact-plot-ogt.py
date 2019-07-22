import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys

data = 'other-tpr-proteins/ogt-contact-prediction-scores.tsv'

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
mtx = np.empty((464, 464))
mtx.fill(np.nan)

for ind, row in gremlin.iterrows():
	i = row['i']
	j = row['j']
	s = row['s_sco']
	mtx[i,j] = s
	mtx[j,i] = s

s = [10*n for n in sco]

# TPR data : 
tpr1 = range(43, 76)
tpr2 = range(79, 109)
tpr3 = range(113, 144)
tpr4 = range(147, 178)
tpr5 = range(181, 213)
tpr6 = range(215, 246)
tpr7 = range(247, 280)
tpr8 = range(281, 315)
tpr9 = range(316, 348)
tpr10 = range(350, 383)
tpr11 = range(26, 42)

tpra = range(31, 64)
tprb = range(65, 98)
tprc = range(99, 132)
tprd = range(133, 166)
tpre = range(167, 200)
tprf = range(201, 234)
tprg = range(235, 268)
tprh = range(269, 302)
tpri = range(303, 336)
tprj = range(337, 370)
tprk = range(377, 410)

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
plt.scatter(tpr1, tpr1, marker='.', color='darkviolet', s=2)
plt.scatter(tpr2, tpr2, marker='.', color='deeppink', s=2)
plt.scatter(tpr3, tpr3, marker='.', color='darkviolet', s=2)
plt.scatter(tpr4, tpr4, marker='.', color='deeppink', s=2)
plt.scatter(tpr5, tpr5, marker='.', color='darkviolet', s=2)
plt.scatter(tpr6, tpr6, marker='.', color='deeppink', s=2)
plt.scatter(tpr7, tpr7, marker='.', color='darkviolet', s=2)
plt.scatter(tpr8, tpr8, marker='.', color='deeppink', s=2)
plt.scatter(tpr9, tpr9, marker='.', color='darkviolet', s=2)
plt.scatter(tpr10, tpr10, marker='.', color='deeppink', s=2)
plt.scatter(tpr11, tpr11, marker='.', color='darkviolet', s=2)


# plt.scatter(tpra, tpra, marker='.', color='deeppink', s=2)
# plt.scatter(tprb, tprb, marker='.', color='darkviolet', s=2)
# plt.scatter(tprc, tprc, marker='.', color='deeppink', s=2)
# plt.scatter(tprd, tprd, marker='.', color='darkviolet', s=2)
# plt.scatter(tpre, tpre, marker='.', color='deeppink', s=2)
# plt.scatter(tprf, tprf, marker='.', color='darkviolet', s=2)
# plt.scatter(tprg, tprg, marker='.', color='deeppink', s=2)
# plt.scatter(tprh, tprh, marker='.', color='darkviolet', s=2)
# plt.scatter(tpri, tpri, marker='.', color='deeppink', s=2)
# plt.scatter(tprj, tprj, marker='.', color='darkviolet', s=2)
# plt.scatter(tprk, tprk, marker='.', color='deeppink', s=2)
plt.colorbar(abc)

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.ylim(464, 0)
plt.xlim(0, 464)
ax.set_aspect(464/464)
plt.tight_layout()
plt.savefig('../gremlin-plots/others/ogt-contact-plot-v2', dpi=300)
plt.show()
