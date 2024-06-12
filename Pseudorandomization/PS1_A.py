# This notebook will create the stimulus set for the second part (Recognition) of the episodic decision-making study (EPIDM) 
# — ie. Pseudorandomize stimulus presentation based on individuals choices from the encoding portion of the study

#Import Packages
import sys
import os
import pandas as pd
import numpy as np

#List the files specified in the command line
inputFiles = sys.argv[1:] 
EncFile = inputFiles[0] #Participants encoding experiment file (provides recongition information)
PS = inputFiles[1] #Provides information regarding which images are old, and which are new in "new"
Select = inputFiles[2] #List of 240 intermixed previously seen and new trials to combine with 360 choices for pseudorandomization // actual old trials differ for each participant
Old = inputFiles[3] #Provides pairing of which trials in the encoding responses are used to create old-old trials

#   Step 1: Read in participant data
Enc_DF = pd.read_csv(EncFile)

#   Step 2: Clean training data
## Relevant Columns: 
#  L_Scene (Picture on Left)
#  R_Scene (Picture on Right)
#  Points_L (Trial Points)
#  Attn_resp.keys (Attention trial responses)
#  Encoding_Resp.keys (Image selection)
#  Transition_Enc.keys (End of instructions)

## Remove training data

#Define function to determine where to filter training data
def resps_idx(df):
#Determine when the participant started the experiment to filter rows accordingly
    resp_start = int(np.argwhere(df['Transition_Enc.keys'].values == "space")[-1]) + 1
    return resp_start

def filter_columns(df):
#Pull out only the columns we are interested in analyzing
    filtered_df = df.filter(['L_Scene', 'R_Scene', 'Points_L', 'Encoding_Resp.keys'])
    return filtered_df

#Filter training data trials
Enc_clean = filter_columns(Enc_DF.loc[resps_idx(Enc_DF):].reset_index(drop=True))

# Sanity check #1: Number of trials in the data
print(f'SANITY CHECK #1 (Trial Numbers): Participant\'s data has {Enc_clean.shape[0]} trials, it should be 240.')

#   Step 3: Evaluate response rate
def resp_num(df):
#Evaluate number of responses
    resps = len([data for data in df['Encoding_Resp.keys'] if data == 'p' or data == 'q'])
    return resps
#Calculate number of responses    
Ppt_respnum = resp_num(Enc_clean)

# Sanity check #2: Evaluate the number of missing responses
print(f'SANITY CHECK #2 (Missing Responses): Participant had {240-Ppt_respnum} missing trials, it should be <= 5.')

#   Step 4: Evaluate attention performance
#Define function to pull out responses to attention check
def attn_num(df):
    #Evaluate responses
    resps = [data for data in df['Attn_resp.keys'] if data == 0 or data == 1 or data == 2 or data == 3 or data == 4 or data == 5][2:] #indexing from 1 removes training trials
    attn_len = len(resps) #indexing from 2 removes both training trials
    return resps, attn_len
#Pull out responses to attention checks
Ppt_attn, Ppt_attnum = attn_num(Enc_DF)

# Sanity check #3: Evaluate the number of attention check responses
print(f'SANITY CHECK #3 (Attention Responses): Participant responded {Ppt_attnum} times, it should be 20.')

#Specify Answer Key (for attention checks)
Attn_Ans = [4, 5, 2, 1, 2, 5, 1, 2, 0, 2, 4, 2, 3, 4, 2, 4, 3, 1, 1, 2]

#Define function to calculate attention check accuracy
def Attn_check(df):
    correct = 0
    resps = [data for data in df['Attn_resp.keys'] if data == 0 or data == 1 or data == 2 or data == 3 or data == 4 or data == 5][2:] #indexing from 2 removes both training trials
    for i in range(len(resps)):
        if resps[i] == Attn_Ans[i]:
            correct += 1
    return (correct/20)*100

# Inclusion check #1: Evaluate the number of attention check responses
print(f'INCLUSION CHECK (Attention Accuracy): Participant\'s accuracy was {Attn_check(Enc_DF)}%, should be >=90%')

###    Step 5: Extract Responses & Correct for missing data
#Define function to pull out responses to encoding task
def extract_enc(df):
    # Pull out the 360 potential responses (necessary because some NAs & blanks in data)
    # Filter out NAs and blank spaces
    enc_resps_filtered = [resp for resp in df['Encoding_Resp.keys'] if resp in ['p', 'q', 'None']][10:] 

    # Create indices of choice and missing selection trials based on filtered responses
    choice_idx_filtered = [idx for idx, data in enumerate(enc_resps_filtered) if data in ['p', 'q']]
    missing_idx_filtered = [idx for idx, data in enumerate(enc_resps_filtered) if data == 'None']

    # Subset the DataFrame using filtered indices and filtered responses
    df_filtered = df.loc[df['Encoding_Resp.keys'].isin(['p', 'q', 'None'])].iloc[10:]
    df_filtered = df_filtered.iloc[choice_idx_filtered]

    # Pull out choice trials from the filtered DataFrame
    clean_L = np.array(df_filtered['L_Scene'])
    clean_R = np.array(df_filtered['R_Scene'])
    clean_pts = np.array(df_filtered['Points_L'])
    clean_enc = np.array(df_filtered['Encoding_Resp.keys'])

    # Iterate through choices and save selected image
    selections = []
    for i in range(len(clean_pts)):
        if clean_enc[i] == 'q':
            selections.append(clean_L[i])
        else:
            selections.append(clean_R[i])

    return selections, clean_pts, choice_idx_filtered, missing_idx_filtered

#Extract encoding responses
selections, clean_pts, choice_idx_filtered, missing_idx_filtered = extract_enc(Enc_DF)
clean_pts = [x for x in clean_pts]

#Define function to correct for missing data by selecting for missed trials and inserting selections with points
Missed_stim =  []
Missed_mon = []
for i in range(len(missing_idx_filtered)):
    Missed_mon.append(Enc_DF.iloc[missing_idx_filtered[i]].Points_L)
    if i % 2:
       Missed_stim.append(Enc_DF.iloc[missing_idx_filtered[i]].L_Scene)
       selections.insert(missing_idx_filtered[i], Missed_stim[i])
       clean_pts.insert(missing_idx_filtered[i], Missed_mon[i])
    else:
        Missed_stim.append(Enc_DF.iloc[missing_idx_filtered[i]].R_Scene)
        selections.insert(missing_idx_filtered[i], Missed_stim[i])
        clean_pts.insert(missing_idx_filtered[i], Missed_mon[i])

#Sanity Check #4: Evaluate the number the stimuli after filling in missing encoding response selections
print(f'SANITY CHECK #4 (Fixed DF): The amount of data and points after filling in missing selections was {len(selections)} and {len(clean_pts)}, respectively')

#   Step 6: Pseudorandomize recognition stimulus list
# Get list of Old/New trials
ON = pd.read_csv(PS, header=None)[0].values
# Create Boolean list of Old/New
ON_Bool = []
for i in range(len(ON)):
    if ON[i] == 'New':
        ON_Bool.append(True)
    else: 
        ON_Bool.append(False)
# Pull out Old stimuli for O/N trials
# Matched Old selections for new trials
Old_ON  = list(np.array(selections)[ON_Bool]) 
Old_pts = list(np.array(clean_pts)[ON_Bool])
# Import new stimuli
PS1_New = list(pd.read_csv(Select, header=None)[0].values)
# Pull out New stimuli for O/N trials
New_ON = list(np.array(PS1_New)[ON_Bool])

#Import old recognition list
PS1_Old = list(pd.read_csv(Old, header=None)[0].values)

#Create function to split paired stimuli
def splitr(pair):
    duo = [x.strip() for x in pair.split(',')]
    return duo

#Create new stimulus lists
Left_Pseudo = []
Right_Pseudo = []
Left_Pts = []
Right_Pts = []
tracker = 0
old_tracker = 0
for i in range(160):
    if i % 2:
        if tracker % 2:
            Left_Pseudo.append(New_ON.pop(0))
            Right_Pseudo.append(Old_ON.pop(0))
            Temp = Old_pts.pop(0)
            # Split the Temp string and take the first part
            point_value = Temp.split()[0]
            if point_value.isdigit():  # Check if the extracted part is a digit
                New_Temp = str(5 - int(point_value)) + ' Points'
            else:
                New_Temp = 'Invalid Points'  # Handle non-numeric values
            Right_Pts.append(Temp)
            Left_Pts.append(New_Temp)
            tracker += 1
        else:
            Left_Pseudo.append(Old_ON.pop(0))
            Right_Pseudo.append(New_ON.pop(0))
            Temp = Old_pts.pop(0)
            # Split the Temp string and take the first part
            point_value = Temp.split()[0]
            if point_value.isdigit():  # Check if the extracted part is a digit
                New_Temp = str(5 - int(point_value)) + ' Points'
            else:
                New_Temp = 'Invalid Points'  # Handle non-numeric values
            Left_Pts.append(Temp)
            Right_Pts.append(New_Temp)
            tracker += 1
    else:
        if old_tracker <= 80:
            split_set = splitr(PS1_Old[old_tracker - 1])
            Left_Pseudo.append(selections[int(split_set[0]) - 2])
            Right_Pseudo.append(selections[int(split_set[1]) - 2])
            Left_Pts.append(clean_pts[int(split_set[0]) - 2])
            Right_Pts.append(clean_pts[int(split_set[1]) - 2])
            old_tracker += 1





#Create pseudorandomized stimulus dataframe
Pseudo_df = pd.DataFrame(zip(Left_Pseudo, Right_Pseudo, Left_Pts, Right_Pts), columns = ["L_Scene", "R_Scene", "L_Pts", "R_Pts"])

#Determine Participant ID
PID = EncFile[:-4]

#Check if files do not exist
if not os.path.exists('PID.txt'):
    with open('PID.txt', 'w') as file:
        file.write("0\n")
if not os.path.exists('SONA.txt'):
    with open('SONA.txt', 'w') as file:
        pass
if not os.path.exists('Grp.txt'):
    with open('Grp.txt', 'w') as file:
        pass
if os.path.exists('PID.txt') and os.path.exists('SONA.txt'):
    #Read in file it does exist
    with open('PID.txt', 'r') as in_file:
        #Turn the content into a string
        PID_list = in_file.readlines()
        latest_Ppt = int(PID_list[-1])+1
    #Append new entry to list
    with open('PID.txt', 'a') as out_file:
         #Write data to the file
        out_file.write(str(latest_Ppt)+"\n")
    with open('SONA.txt', 'a') as out_file:
         #Write data to the file
        out_file.write(str(PID)+"\n")
    with open('Grp.txt', 'a') as out_file:
         #Write data to the file
        out_file.write("A\n")

#Export newly created pseuforandomized dataframe
PS_df_name = str(latest_Ppt) +'_R.csv'
Pseudo_df.to_csv(PS_df_name, index=False)