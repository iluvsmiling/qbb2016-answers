#!/usr/bin/env python

"""
    Sxl/FBtr0331261 FPKM vs stage scatterplot
    Males vs female. All replicates
  
  Usage: ./01-timecourse.py <metadata.csv> <ctab_dir> <rep.csv>
    e.g. ./01-timecourse.py samples.csv ~/data/results/stringtie

Output: scatterplot, as found in Lott et al, p 5
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


df_meta = pd.read_csv( sys.argv[1] )
ctab_dir = sys.argv[3] 
df_replicates = sys.argv[2]

# Female Selection
fem_Sxl = []

df_roi = df_meta[ "sex" ] == "female"
for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi_f = df[ "t_name" ] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi_f ][ "FPKM" ].values)

# Male Selection

male_Sxl = []

df2_roi = df_meta[ "sex" ] == "male"
for sample in df_meta[ df2_roi ][ "sample" ]:
    filename2 = ctab_dir + "/" + sample + "/t_data.ctab"
    df2 = pd.read_table( filename2 )
    
    df_roi_m = df2[ "t_name" ] == "FBtr0331261"
    male_Sxl.append( df[ df_roi_m ][ "FPKM" ].values)
    
##slap on replicates.csv - f
fem_rep = []
df_roi_f2 = df_replicates["sex"] == "female"
for sample in df_replicates[df_roi_f2]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df3_roi = df["t_name"] == "FBtr0331261"
    fem_rep.append( df[ df3_roi ]["FPKM"].values)

##slap on replicates.csv - male
male_reps = []
df_roi_m2 = df_replicates["sex"] == "male"
for sample in df_replicates[df_roi_m2]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi_f4 = df["t_name"] == "FBtr0331261"
    male_reps.append( df[ df_roi_f4 ]["FPKM"].values)

# Show time!
##Error: pandas.io.common.EmptyDataError: No columns to parse from file
## Error is coming from input file or pandas package. This code should work!


plt.figure()

labels_1 = np.array([0,1,2,3,4,5,6,7,8])
labels_2 = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
plt.xticks( labels_1, labels_2, rotation='horizontal')
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance")
plt.title("Sxl Expression in Male and Female Over Time")
plt.plot(fem_Sxl, 'r-', label ="female")
plt.plot(male_Sxl, 'b-', label="male")
plt.plot([4,5,6,7], fem_reps, 'r.')
plt.plot([4,5,6,7], male_reps, 'b.')

plt.legend(loc="upper left")
plt.savefig("p1_timecourse_plot.png")
plt.close()








