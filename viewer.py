import pandas as pd

import networkx as nx

import matplotlib.pyplot as plt

import sys

filename = sys.argv[1]
#%matplotlib inline

# read in the data

df = pd.read_csv(filename)

# create a graph

G = nx.from_pandas_edgelist(df, 'Source', 'Target')

# draw the graph

nx.draw(G, with_labels=True)

plt.show()
