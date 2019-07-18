import sys
from os.path import dirname, abspath
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

prot = sys.argv[1] # PflA or PflB
parentdir = dirname(dirname(abspath(__file__)))

fpath = parentdir+'/other-tpr-proteins/'+prot+'-contact-prediction-scores.tsv'

gremlin = pd.read_csv(fpath, sep='\t')
print(len(gremlin))
#gremlin.sort_values('s_sco', inplace=True)
dist = gremlin['distance']
coupling = gremlin['s_sco']

#~~~~~~~~~~~
# MAKE PLOT
#~~~~~~~~~~~

fig, ax = plt.subplots()
plt.scatter(dist, coupling, marker='.', s=15, c='k')

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

plt.xlabel('distance between coupled residues')
plt.ylabel('coupling strength')

plt.tight_layout()
plt.savefig('control-coupling-distance-'+prot, dpi=300)
plt.show()
