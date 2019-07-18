import sys
from os.path import dirname, abspath
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

pfl = sys.argv[1] # PflA or PflB
e = sys.argv[2] # -06, -10 or -20
msacov = sys.argv[3] # 50 or 25 
parentdir = dirname(dirname(abspath(__file__)))

fpath = parentdir+'/HHblits-eval1e'+e+'-msacoverage-'+msacov+'/'+pfl+'-contact-prediction-scores.tsv'

gremlin = pd.read_csv(fpath, sep='\t')
print(len(gremlin))
#gremlin.sort_values('s_sco', inplace=True)
dist = gremlin['distance']
coupling = gremlin['s_sco']
prob = gremlin['prob']

#~~~~~~~~~~~
# MAKE PLOT
#~~~~~~~~~~~

fig, ax = plt.subplots()
ax.scatter(dist, coupling, marker='^', c='C1')
ax.legend(['coupling'], loc='upper center')
ax.set_xlabel('distance between coupled residues')
ax.set_ylabel('coupling strength')

ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.grid(b=True, which='major', linestyle='-')
ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.xaxis.grid(b=True, which='major', linestyle='-')
ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
ax.set_axisbelow(True)

ax2 = ax.twinx() # instantiate a second axes that shares the same x-axis

ax2.set_ylabel('probability')
ax2.scatter(dist, prob, marker='.', s=15, c='C0')
ax2.legend(['probability'])



fig.tight_layout()
plt.savefig('coupling-distance-probability-'+pfl+'-eval1e'+e+'-msacoverage-'+msacov, dpi=300)
plt.show()
