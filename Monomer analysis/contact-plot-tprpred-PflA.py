import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys
from os.path import dirname, abspath

#~~~~~~~~~~~~~~~~~~
# GET GREMLIN DATA
#~~~~~~~~~~~~~~~~~~

e = sys.argv[1] # -10 or -20
data = 'HHblits-eval1e'+e+'/PflA-contact-prediction-scores.tsv'
gremlin = pd.read_csv(data, sep='\t')
print(len(gremlin))
#gremlin = gremlin[gremlin['distance'] > 3]
print(len(gremlin))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAKE LISTS AND A MATRIX OF GREMLIN DATA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = gremlin['i'].tolist() + gremlin['j'].tolist()
y = gremlin['j'].tolist() + gremlin['i'].tolist()
sco = gremlin['s_sco'].tolist() + gremlin['s_sco'].tolist()

#make empty square matrix of dimensions = protein length 
mtx = np.empty((788, 788))
mtx.fill(np.nan)

for ind, row in gremlin.iterrows():
	i = row['i']
	j = row['j']
	s = row['s_sco']
	mtx[i,j] = s
	mtx[j,i] = s

# Define size of point on scatter plot as a function of the scaled score
s = [10*n for n in sco]

#~~~~~~~~~~~~~~~~~~
# GET TPRPRED DATA
#~~~~~~~~~~~~~~~~~~

parent = dirname(dirname(abspath(__file__)))
tpr = parent + '/tprpred/PflA-tprpred.tsv'
tpr = pd.read_csv(tpr, sep='\t')
tpr = tpr[tpr['accver'] == 'WP_002851328.1']
data = np.array([tpr['tpr-start'], tpr['tpr-end']])
print(data)
tpr1 = list(range(data[0,0], data[1,0]))
tpr2 = list(range(data[0,1], data[1,1]))
tpr3 = list(range(data[0,2], data[1,2]))
tpr4 = list(range(data[0,3], data[1,3]))
tpr5 = list(range(data[0,4], data[1,4]))
tpr6 = list(range(data[0,5], data[1,5]))
tpra = range(254, 287)
tprb = range(291, 324)
tprc = range(588, 621)
tprd = range(663, 696)

#~~~~~~~~~~
# PLOTTING
#~~~~~~~~~~

# Function truncates teh colormap to exclude the very light yellow portion
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
	if n == -1:
		n = cmap.N
	new_cmap = mcolors.LinearSegmentedColormap.from_list('trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
	return new_cmap

inferno_t = truncate_colormap(plt.get_cmap('inferno_r'), 0.15, 1)

# Define the scatter plot and colorbar
fig, ax = plt.subplots()
plt.scatter(x, y, marker='.', s=s, c=mtx[x,y], cmap=inferno_t)
plt.scatter(tpr1, tpr1, marker='.', color='green', s=5)
plt.scatter(tpr2, tpr2, marker='.', color='green', s=5)
plt.scatter(tpr3, tpr3, marker='.', color='green', s=5)
plt.scatter(tpr4, tpr4, marker='.', color='green', s=5)
plt.scatter(tpr5, tpr5, marker='.', color='green', s=5)
plt.scatter(tpr6, tpr6, marker='.', color='green', s=5)

plt.scatter(tpra, tpra, marker='.', color='green', s=5)
plt.scatter(tprb, tprb, marker='.', color='green', s=5)
plt.scatter(tprc, tprc, marker='.', color='green', s=5)
plt.scatter(tprd, tprd, marker='.', color='green', s=5)
#cbar = plt.colorbar()

# Define and format minor and major gridlines
ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

# Define axis limits and shape of plot area - square
plt.ylim(800, 0)
plt.xlim(0, 800)
ax.set_aspect(800/800)

# Save and draw plot
plt.tight_layout()
plt.savefig('PflA-gremlin-tprpred-plot-1e'+e, dpi=300)
plt.show()
