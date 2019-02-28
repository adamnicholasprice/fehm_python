import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

for hist in glob.glob("*.hist"):
    print(hist)

nodes = pd.read_csv(hist,skiprows=2,nrows=1,header=None)
nodes = int(nodes[0])

node_coords = pd.read_csv(hist,skiprows=6,nrows=nodes,header=None,delim_whitespace=True)

fp = open(hist)

total_line_count = sum(1 for line in fp)

with open(hist) as fp:
    for num, line in enumerate(fp,1):
        heading = "headings"
        if heading in line:
            col_names = num
    node_one = node_coords.iloc[0, 0]
    for node_one in line:
            coord_start = line

#
#
# headings = pd.read_csv(hist,skiprows=col_names,nrows=1,header=None,delimiter='\t+')




