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
# R_Pts - Point associated with
# Encoding_Resp.keys - Participants' Decisions
# Confidence_Resp.keys - Participants' Confidence in their memory
# Value_Slider.response - Subjective value associted with remembered option

#Filter data for relevant features
Columns = ['Participant', 'L_Pts', 'R_Pts', 'Encoding_Resp.keys', 'Confidence_Resp.keys', 'Value_Slider.response']
Enc_DF_A = Enc_DF_A.filter(Columns)

#Clean Data
Clean_A = Enc_DF_A.dropna().reset_index(drop=True)

##  Step 3: Feature engineering  ##
#Change text value of each choice to integer
Clean_A['L_Pts'] = [int(x[0:2].strip()) for x in Clean_A['L_Pts']]
Clean_A['R_Pts'] = [int(x[0:2].strip()) for x in Clean_A['R_Pts']]

#Create column for correct decision
#$Clean_A['Correct']
Answer_A = []
for i in range(len(Clean_A['R_Pts'])):
    if (Clean_A['L_Pts'].iloc[i] > Clean_A['R_Pts'].iloc[i]):
        Answer_A.append('q')
    else:
        Answer_A.append('p')

#Add column to existing dataframe
Clean_A['Answer Key'] = Answer_A

#Add column to determine response accuracy
Clean_A['Accuracy'] = [1 if x == y else 0 for x, y in zip(Clean_A['Encoding_Resp.keys'], Clean_A['Answer Key'])]

##  Step 4: Calculate Totals  ##
#Calculate a participants total points
Ppt_pts = []
for i in range(len(Clean_A['L_Pts'])):
    if Clean_A['Encoding_Resp.keys'].iloc[i] == 'p':
        Ppt_pts.append(Clean_A['R_Pts'].iloc[i])
    else:
        Ppt_pts.append(Clean_A['L_Pts'].iloc[i])

## Step 5: Sanity Checks ##
# Sanity check -- Value based decision making
#Create mapping for whether stimulus was remembered
DM_Rem = []
for i in range(len(Clean_A['Confidence_Resp.keys'])):
    if Clean_A['Confidence_Resp.keys'].iloc[i] == 'a':
        DM_Rem.append(0)
    elif Clean_A['Confidence_Resp.keys'].iloc[i] == 's':
        DM_Rem.append(0)
    elif Clean_A['Confidence_Resp.keys'].iloc[i] == 'd':
        DM_Rem.append(0)
    elif Clean_A['Confidence_Resp.keys'].iloc[i] == 'j':
        DM_Rem.append(1)
    elif Clean_A['Confidence_Resp.keys'].iloc[i] == 'k':
        DM_Rem.append(1)
    elif Clean_A['Confidence_Resp.keys'].iloc[i] == 'l':
        DM_Rem.append(1)
Clean_A['Chose_Rem'] = DM_Rem
#Make the floating point number an integer
Clean_A['Value_Slider.response'] = [int(x) for x in Clean_A['Value_Slider.response']] 
#Create a new column with decision purely informed by remembered value
Value_DM = []
for i in range(len(Clean_A['Value_Slider.response'])):
    if Clean_A['Chose_Rem'].iloc[i] == 0 and Clean_A['Value_Slider.response'].iloc[i] <= 3:
        Value_DM.append(1)
    elif Clean_A['Chose_Rem'].iloc[i] == 0 and Clean_A['Value_Slider.response'].iloc[i] > 3:
        Value_DM.append(0)
    elif Clean_A['Chose_Rem'].iloc[i] == 1 and Clean_A['Value_Slider.response'].iloc[i] <= 3:
        Value_DM.append(0)
    elif Clean_A['Chose_Rem'].iloc[i] == 1 and Clean_A['Value_Slider.response'].iloc[i] > 3:
        Value_DM.append(1)
    else:
        print('wut')
Clean_A['Value_DM'] = Value_DM
#If you report a high value, you should choose it, if the value is low, you should not choose it.

## Step 5: Report results  ##
# Participant accuracy
print(f'Decisions were optimal {round(sum(Clean_A["Accuracy"])/len(Clean_A["Answer Key"]), 3)*100}% of the time.')

# Participant points
print(f'The total points earned by this participant was {sum(Ppt_pts)} -- ${int(round(sum(Ppt_pts)/200,0))} bonus cash.')

# Memory bias in decision making
print(f'Participants chose the stimulus they rememebered seeing in {round(sum(Clean_A["Chose_Rem"]/len(Clean_A["Chose_Rem"])), 3)*100}% of choices.')

# Value-based decision-making
print(f'Participants were economically rational decision makers in  {round(sum(Clean_A["Value_DM"]/len(Clean_A["Value_DM"])), 3)*100}% of choices.')