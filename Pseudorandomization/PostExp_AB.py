# This notebook:
# 1) Determines the right choices for each pseudorandomized list presentation 
# and output those as seperate files to use as answer keys in subsequent steps
# 2) Calculate points associated with participants actual choices
# 3) Determines how "correct" participants are based on value DM

#Import Packages
import sys
import os
import pandas as pd
import numpy as np
import random

##   Step 1: Read in participant data  ##
# Set Working Directory
pwd = os.getcwd() + str("/")

#List the files specified in the command line
inputFiles = sys.argv[1:]
RecFile = inputFiles[0]

# Specify Psuedoradomization A
DF_A = pwd + RecFile

# Read in dataframes
Enc_DF_A = pd.read_csv(DF_A)

##   Step 2: Clean Recognition data  ##
## Relevant Columns: 
# Participant - Unique subject ID (anonymized)
# L_Pts - Points associated with left image
# R_Pts - Point associated with right image
# Encoding_Resp.keys - Participants' Decisions

#Filter data for relevant features
Columns = ['Participant', 'L_Pts', 'R_Pts', 'Encoding_Resp.keys']
Enc_DF_A = Enc_DF_A.filter(Columns)

#Clean Data
Clean_A = Enc_DF_A.dropna().reset_index(drop=True)
Clean_A = Clean_A.iloc[10:].reset_index(drop=True)


##  Step 3: Feature engineering  ##
#Change text value of each choice to integer
Clean_A['L_Pts'] = [int(x[0:2].strip()) for x in Clean_A['L_Pts']]
Clean_A['R_Pts'] = [int(x[0:2].strip()) for x in Clean_A['R_Pts']]

#Create column for correct decision
Answer_A = []
for i in range(len(Clean_A['R_Pts'])):
    if (Clean_A['L_Pts'].iloc[i] > Clean_A['R_Pts'].iloc[i]):
        Answer_A.append('q')
    else:
        Answer_A.append('p')

#Add column to existing dataframe
Clean_A['Answer Key'] = Answer_A

#Change the confidence responses to be binary recognition
# Dictionary for mapping
transformation_dict = {'a': 'q', 's': 'q', 'd': 'q', 'j': 'p', 'k': 'p', 'l': 'p'}

# Applying the transformation
Clean_A['Transformed_enc'] = Clean_A['Encoding_Resp.keys'].map(transformation_dict)

#Add column to determine response accuracy
Clean_A['Accuracy'] = [1 if x == y else 0 for x, y in zip(Clean_A['Transformed_enc'], Clean_A['Answer Key'])]

##  Step 4: Calculate Totals  ##
#Calculate participants bonus points
Ppt_pts = []
for i in range(len(Clean_A['L_Pts'])):
    if Clean_A['Transformed_enc'].iloc[i] == 'p':
        Ppt_pts.append(Clean_A['R_Pts'].iloc[i])
    else:
        Ppt_pts.append(Clean_A['L_Pts'].iloc[i])

# Randomly sample and sum 2 values from Ppt_pts
sampled_values = sum(random.sample(Ppt_pts, 2))

## Step 5: Report results  ##
# Participant accuracy
print(f'Decisions were optimal {round(sum(Clean_A["Accuracy"])/len(Clean_A["Answer Key"]), 3)*100}% of the time.')

# Participant points
print(f'This participant earned ${sampled_values} bonus cash.')