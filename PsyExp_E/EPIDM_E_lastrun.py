#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sun Jun 23 09:22:27 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '0'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'EPIDM'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'Group': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/johnnycastillo/Desktop/EpiDM/PsyExp_E/EPIDM_E_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions" ---
Instructions_Resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from filename_code
if int(expInfo['participant']):
    Group = 'A'
else:
    Group = 'B'
fileName = "Group"+str(expInfo['Group'])+".csv"
#winSize = psychoJS.Window.size;
Instructions_Stim = visual.ImageStim(
    win=win,
    name='Instructions_Stim', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Redo_Instructions" ---
Redo_Instructions_Resp = keyboard.Keyboard()
Redo_Instructions_Top_Stim = visual.TextStim(win=win, name='Redo_Instructions_Top_Stim',
    text='',
    font='Open Sans',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
Redo_Instructions_Bottom_Stim = visual.TextStim(win=win, name='Redo_Instructions_Bottom_Stim',
    text='',
    font='Open Sans',
    pos=(0, +.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Instructions" ---
Instructions_Resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from filename_code
if int(expInfo['participant']):
    Group = 'A'
else:
    Group = 'B'
fileName = "Group"+str(expInfo['Group'])+".csv"
#winSize = psychoJS.Window.size;
Instructions_Stim = visual.ImageStim(
    win=win,
    name='Instructions_Stim', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Practice_Intro" ---
Practice_Intro_Stim = visual.TextStim(win=win, name='Practice_Intro_Stim',
    text='You will now complete a shortened version of this experiment for practice',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.14, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Pre_Encoding_Break" ---
Continue_Enc_Space = visual.TextStim(win=win, name='Continue_Enc_Space',
    text='press SPACE to continue',
    font='Open Sans',
    units='norm', pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Transition_Prompt_Enc = visual.TextStim(win=win, name='Transition_Prompt_Enc',
    text="you will now select cards\n\nReminder:\npress 'Q' to select the left card\npress 'P' to select the right card\n\nYou have 4 seconds to respond, please respond during this time",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Transition_Enc = keyboard.Keyboard()

# --- Initialize components for Routine "Title_Encoding" ---
Title_Encoding_Stim = visual.TextStim(win=win, name='Title_Encoding_Stim',
    text='Card Selection',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Deck" ---
Deck_Stim = visual.TextStim(win=win, name='Deck_Stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation" ---
Dealer_Stim = visual.ImageStim(
    win=win,
    name='Dealer_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.35, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Encoding" ---
L_Sq_Stim = visual.Rect(
    win=win, name='L_Sq_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=0.0, interpolate=True)
R_Sq_Stim = visual.Rect(
    win=win, name='R_Sq_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
Encoding_Resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from Key_Tracking_Code
Choice_List = []
Loop_Count = 0
Enc_Loop_Count = 0
PrcLoop_Count = 0
PrcEnc_Loop_Count = 0
ProT = 0
L_Scene_Stim = visual.ImageStim(
    win=win,
    name='L_Scene_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
R_Scene_Stim = visual.ImageStim(
    win=win,
    name='R_Scene_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Response_Fail" ---
Fail_Too_Text = visual.TextStim(win=win, name='Fail_Too_Text',
    text='Too',
    font='Open Sans',
    units='norm', pos=(-0.2, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
Fail_Slow_Text = visual.TextStim(win=win, name='Fail_Slow_Text',
    text='Slow!',
    font='Open Sans',
    units='norm', pos=(0.2, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Feedback" ---
R_Sq_FB_Stim = visual.Rect(
    win=win, name='R_Sq_FB_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=1.0, depth=-1.0, interpolate=True)
L_Sq_FB_Stim = visual.Rect(
    win=win, name='L_Sq_FB_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=1.0, depth=-2.0, interpolate=True)
R_Scene_FB_Stim = visual.ImageStim(
    win=win,
    name='R_Scene_FB_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
L_Scene_FB_Stim = visual.ImageStim(
    win=win,
    name='L_Scene_FB_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
L_Point_FB_Stim = visual.TextStim(win=win, name='L_Point_FB_Stim',
    text='',
    font='Open Sans',
    units='norm', pos=(-0.5, .8), height=0.25, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
R_Point_FB_Stim = visual.TextStim(win=win, name='R_Point_FB_Stim',
    text='',
    font='Open Sans',
    units='norm', pos=(0.5, 0.8), height=0.25, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
L_Point_Mask = visual.Rect(
    win=win, name='L_Point_Mask',units='norm', 
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0.0, pos=(-0.5, .1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=0.0, depth=-7.0, interpolate=True)
R_Point_Mask = visual.Rect(
    win=win, name='R_Point_Mask',units='norm', 
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0.0, pos=(.5, .1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=0.0, depth=-8.0, interpolate=True)

# --- Initialize components for Routine "Attention" ---
Attn_Stim = visual.ImageStim(
    win=win,
    name='Attn_Stim', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Attn_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Coins" ---
Coin_Animation = visual.MovieStim(
    win, name='Coin_Animation',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=0.0,
    pos=(0, 0), size=[.6, .75], units=None,
    ori=0.0, anchor='center',opacity=1.0, contrast=None,
)

# --- Initialize components for Routine "Encoding_Break" ---
EncBrk_Prompt = visual.TextStim(win=win, name='EncBrk_Prompt',
    text='please take a short break before continuing',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Cont_Enc_Stim = visual.TextStim(win=win, name='Cont_Enc_Stim',
    text='press SPACE to continue',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EncBrk_Warning_Prompt = visual.TextStim(win=win, name='EncBrk_Warning_Prompt',
    text='!WARNING!\nonly 10 seconds remain',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Cont_EncBrk_Prompt = visual.TextStim(win=win, name='Cont_EncBrk_Prompt',
    text='please continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
EncBrk_Resp = keyboard.Keyboard()
Point_Report_Prompt = visual.TextStim(win=win, name='Point_Report_Prompt',
    text='So far your point total is:',
    font='Open Sans',
    pos=(0,.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Point_Report_Stim = visual.TextStim(win=win, name='Point_Report_Stim',
    text='',
    font='Open Sans',
    pos=(0,.15), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.2157, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Progress_Tracker = visual.ImageStim(
    win=win,
    name='Progress_Tracker', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -.2), size=(1, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
Perc_stim = visual.ImageStim(
    win=win,
    name='Perc_stim', 
    image='Perc.png', mask=None, anchor='center',
    ori=0.0, pos=(0.03, -0.28), size=(1.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Practice_End" ---
practice_encoding_stim = visual.TextStim(win=win, name='practice_encoding_stim',
    text='this is the end of practice',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Exp_Intro" ---
Transition_Stim_Response = keyboard.Keyboard()
Transition_Stim = visual.TextStim(win=win, name='Transition_Stim',
    text='you will now complete the full experiment',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Space_Stim = visual.TextStim(win=win, name='Space_Stim',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, 0-.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Pre_Encoding_Break" ---
Continue_Enc_Space = visual.TextStim(win=win, name='Continue_Enc_Space',
    text='press SPACE to continue',
    font='Open Sans',
    units='norm', pos=(0, -.75), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Transition_Prompt_Enc = visual.TextStim(win=win, name='Transition_Prompt_Enc',
    text="you will now select cards\n\nReminder:\npress 'Q' to select the left card\npress 'P' to select the right card\n\nYou have 4 seconds to respond, please respond during this time",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Transition_Enc = keyboard.Keyboard()

# --- Initialize components for Routine "Title_Encoding" ---
Title_Encoding_Stim = visual.TextStim(win=win, name='Title_Encoding_Stim',
    text='Card Selection',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Deck" ---
Deck_Stim = visual.TextStim(win=win, name='Deck_Stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation" ---
Dealer_Stim = visual.ImageStim(
    win=win,
    name='Dealer_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.35, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Encoding" ---
L_Sq_Stim = visual.Rect(
    win=win, name='L_Sq_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=0.0, interpolate=True)
R_Sq_Stim = visual.Rect(
    win=win, name='R_Sq_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
Encoding_Resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from Key_Tracking_Code
Choice_List = []
Loop_Count = 0
Enc_Loop_Count = 0
PrcLoop_Count = 0
PrcEnc_Loop_Count = 0
ProT = 0
L_Scene_Stim = visual.ImageStim(
    win=win,
    name='L_Scene_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
R_Scene_Stim = visual.ImageStim(
    win=win,
    name='R_Scene_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Response_Fail" ---
Fail_Too_Text = visual.TextStim(win=win, name='Fail_Too_Text',
    text='Too',
    font='Open Sans',
    units='norm', pos=(-0.2, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
Fail_Slow_Text = visual.TextStim(win=win, name='Fail_Slow_Text',
    text='Slow!',
    font='Open Sans',
    units='norm', pos=(0.2, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Feedback" ---
R_Sq_FB_Stim = visual.Rect(
    win=win, name='R_Sq_FB_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=1.0, depth=-1.0, interpolate=True)
L_Sq_FB_Stim = visual.Rect(
    win=win, name='L_Sq_FB_Stim',units='norm', 
    width=(0.9, 1.2)[0], height=(0.9, 1.2)[1],
    ori=0.0, pos=(-0.5, 0.1), anchor='center',
    lineWidth=7.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=1.0, depth=-2.0, interpolate=True)
R_Scene_FB_Stim = visual.ImageStim(
    win=win,
    name='R_Scene_FB_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
L_Scene_FB_Stim = visual.ImageStim(
    win=win,
    name='L_Scene_FB_Stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.05), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
L_Point_FB_Stim = visual.TextStim(win=win, name='L_Point_FB_Stim',
    text='',
    font='Open Sans',
    units='norm', pos=(-0.5, .8), height=0.25, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
R_Point_FB_Stim = visual.TextStim(win=win, name='R_Point_FB_Stim',
    text='',
    font='Open Sans',
    units='norm', pos=(0.5, 0.8), height=0.25, wrapWidth=None, ori=0.0, 
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
L_Point_Mask = visual.Rect(
    win=win, name='L_Point_Mask',units='norm', 
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0.0, pos=(-0.5, .1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=0.0, depth=-7.0, interpolate=True)
R_Point_Mask = visual.Rect(
    win=win, name='R_Point_Mask',units='norm', 
    width=(1, 2)[0], height=(1, 2)[1],
    ori=0.0, pos=(.5, .1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=0.0, depth=-8.0, interpolate=True)

# --- Initialize components for Routine "Attention" ---
Attn_Stim = visual.ImageStim(
    win=win,
    name='Attn_Stim', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Attn_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Coins" ---
Coin_Animation = visual.MovieStim(
    win, name='Coin_Animation',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=0.0,
    pos=(0, 0), size=[.6, .75], units=None,
    ori=0.0, anchor='center',opacity=1.0, contrast=None,
)

# --- Initialize components for Routine "Encoding_Break" ---
EncBrk_Prompt = visual.TextStim(win=win, name='EncBrk_Prompt',
    text='please take a short break before continuing',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Cont_Enc_Stim = visual.TextStim(win=win, name='Cont_Enc_Stim',
    text='press SPACE to continue',
    font='Open Sans',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EncBrk_Warning_Prompt = visual.TextStim(win=win, name='EncBrk_Warning_Prompt',
    text='!WARNING!\nonly 10 seconds remain',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Cont_EncBrk_Prompt = visual.TextStim(win=win, name='Cont_EncBrk_Prompt',
    text='please continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
EncBrk_Resp = keyboard.Keyboard()
Point_Report_Prompt = visual.TextStim(win=win, name='Point_Report_Prompt',
    text='So far your point total is:',
    font='Open Sans',
    pos=(0,.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Point_Report_Stim = visual.TextStim(win=win, name='Point_Report_Stim',
    text='',
    font='Open Sans',
    pos=(0,.15), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.2157, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Progress_Tracker = visual.ImageStim(
    win=win,
    name='Progress_Tracker', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -.2), size=(1, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
Perc_stim = visual.ImageStim(
    win=win,
    name='Perc_stim', 
    image='Perc.png', mask=None, anchor='center',
    ori=0.0, pos=(0.03, -0.28), size=(1.12, 0.12),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "Reward_Reveal" ---
Reward_Stim = visual.TextStim(win=win, name='Reward_Stim',
    text='Based on your points you earned:',
    font='Open Sans',
    pos=(0, .2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Bonus_Cash = visual.TextStim(win=win, name='Bonus_Cash',
    text='9 Dollars',
    font='Open Sans',
    pos=(0, -.05), height=0.15, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -0.2157, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Experiment_End" ---
Experiment_End_Stim = visual.TextStim(win=win, name='Experiment_End_Stim',
    text='This is the end of the experiment\n\nThank you for participating',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
Instructions_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encoding_Instructions.csv'),
    seed=None, name='Instructions_Loop')
thisExp.addLoop(Instructions_Loop)  # add the loop to the experiment
thisInstructions_Loop = Instructions_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_Loop.rgb)
if thisInstructions_Loop != None:
    for paramName in thisInstructions_Loop:
        exec('{} = thisInstructions_Loop[paramName]'.format(paramName))

for thisInstructions_Loop in Instructions_Loop:
    currentLoop = Instructions_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_Loop.rgb)
    if thisInstructions_Loop != None:
        for paramName in thisInstructions_Loop:
            exec('{} = thisInstructions_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Instructions_Resp.keys = []
    Instructions_Resp.rt = []
    _Instructions_Resp_allKeys = []
    Instructions_Stim.setColor([1,1,1], colorSpace='rgb')
    Instructions_Stim.setSize([2, 2])
    Instructions_Stim.setImage(Scene)
    # keep track of which components have finished
    InstructionsComponents = [Instructions_Resp, Instructions_Stim]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Resp* updates
        waitOnFlip = False
        if Instructions_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Resp.frameNStart = frameN  # exact frame index
            Instructions_Resp.tStart = t  # local t and not account for scr refresh
            Instructions_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Resp, 'tStartRefresh')  # time at next scr refresh
            Instructions_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instructions_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instructions_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instructions_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Instructions_Resp.getKeys(keyList=['space'], waitRelease=False)
            _Instructions_Resp_allKeys.extend(theseKeys)
            if len(_Instructions_Resp_allKeys):
                Instructions_Resp.keys = _Instructions_Resp_allKeys[-1].name  # just the last key pressed
                Instructions_Resp.rt = _Instructions_Resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Stim* updates
        if Instructions_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Stim.frameNStart = frameN  # exact frame index
            Instructions_Stim.tStart = t  # local t and not account for scr refresh
            Instructions_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Stim, 'tStartRefresh')  # time at next scr refresh
            Instructions_Stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_Stim]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_Stim* updates
        if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_Stim.frameNStart = frameN  # exact frame index
            ITI_Stim.tStart = t  # local t and not account for scr refresh
            ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
            ITI_Stim.setAutoDraw(True)
        if ITI_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                ITI_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_Stim]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_Stim* updates
        if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_Stim.frameNStart = frameN  # exact frame index
            ITI_Stim.tStart = t  # local t and not account for scr refresh
            ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
            ITI_Stim.setAutoDraw(True)
        if ITI_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                ITI_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
# completed 1.0 repeats of 'Instructions_Loop'


# --- Prepare to start Routine "Redo_Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Redo_Instructions_Resp.keys = []
Redo_Instructions_Resp.rt = []
_Redo_Instructions_Resp_allKeys = []
Redo_Instructions_Top_Stim.setText("to practice the experiment, press 'P'")
Redo_Instructions_Bottom_Stim.setText("to repeat the instructions, press 'R'")
# keep track of which components have finished
Redo_InstructionsComponents = [Redo_Instructions_Resp, Redo_Instructions_Top_Stim, Redo_Instructions_Bottom_Stim]
for thisComponent in Redo_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Redo_Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Redo_Instructions_Resp* updates
    waitOnFlip = False
    if Redo_Instructions_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Redo_Instructions_Resp.frameNStart = frameN  # exact frame index
        Redo_Instructions_Resp.tStart = t  # local t and not account for scr refresh
        Redo_Instructions_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Redo_Instructions_Resp, 'tStartRefresh')  # time at next scr refresh
        Redo_Instructions_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Redo_Instructions_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Redo_Instructions_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Redo_Instructions_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Redo_Instructions_Resp.getKeys(keyList=['p','r'], waitRelease=False)
        _Redo_Instructions_Resp_allKeys.extend(theseKeys)
        if len(_Redo_Instructions_Resp_allKeys):
            Redo_Instructions_Resp.keys = _Redo_Instructions_Resp_allKeys[-1].name  # just the last key pressed
            Redo_Instructions_Resp.rt = _Redo_Instructions_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Redo_Instructions_Top_Stim* updates
    if Redo_Instructions_Top_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Redo_Instructions_Top_Stim.frameNStart = frameN  # exact frame index
        Redo_Instructions_Top_Stim.tStart = t  # local t and not account for scr refresh
        Redo_Instructions_Top_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Redo_Instructions_Top_Stim, 'tStartRefresh')  # time at next scr refresh
        Redo_Instructions_Top_Stim.setAutoDraw(True)
    
    # *Redo_Instructions_Bottom_Stim* updates
    if Redo_Instructions_Bottom_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Redo_Instructions_Bottom_Stim.frameNStart = frameN  # exact frame index
        Redo_Instructions_Bottom_Stim.tStart = t  # local t and not account for scr refresh
        Redo_Instructions_Bottom_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Redo_Instructions_Bottom_Stim, 'tStartRefresh')  # time at next scr refresh
        Redo_Instructions_Bottom_Stim.setAutoDraw(True)
    # Run 'Each Frame' code from Repeat_Instructions_Trigger
    if Redo_Instructions_Resp.keys == 'p':
        RedoLoop = 0
    else:
        RedoLoop = 1
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Redo_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Redo_Instructions" ---
for thisComponent in Redo_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Redo_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Redo_Instructions_Loop = data.TrialHandler(nReps=RedoLoop, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Encoding_Instructions.csv'),
    seed=None, name='Redo_Instructions_Loop')
thisExp.addLoop(Redo_Instructions_Loop)  # add the loop to the experiment
thisRedo_Instructions_Loop = Redo_Instructions_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRedo_Instructions_Loop.rgb)
if thisRedo_Instructions_Loop != None:
    for paramName in thisRedo_Instructions_Loop:
        exec('{} = thisRedo_Instructions_Loop[paramName]'.format(paramName))

for thisRedo_Instructions_Loop in Redo_Instructions_Loop:
    currentLoop = Redo_Instructions_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisRedo_Instructions_Loop.rgb)
    if thisRedo_Instructions_Loop != None:
        for paramName in thisRedo_Instructions_Loop:
            exec('{} = thisRedo_Instructions_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Instructions_Resp.keys = []
    Instructions_Resp.rt = []
    _Instructions_Resp_allKeys = []
    Instructions_Stim.setColor([1,1,1], colorSpace='rgb')
    Instructions_Stim.setSize([2, 2])
    Instructions_Stim.setImage(Scene)
    # keep track of which components have finished
    InstructionsComponents = [Instructions_Resp, Instructions_Stim]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Resp* updates
        waitOnFlip = False
        if Instructions_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Resp.frameNStart = frameN  # exact frame index
            Instructions_Resp.tStart = t  # local t and not account for scr refresh
            Instructions_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Resp, 'tStartRefresh')  # time at next scr refresh
            Instructions_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instructions_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instructions_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instructions_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Instructions_Resp.getKeys(keyList=['space'], waitRelease=False)
            _Instructions_Resp_allKeys.extend(theseKeys)
            if len(_Instructions_Resp_allKeys):
                Instructions_Resp.keys = _Instructions_Resp_allKeys[-1].name  # just the last key pressed
                Instructions_Resp.rt = _Instructions_Resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Stim* updates
        if Instructions_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Stim.frameNStart = frameN  # exact frame index
            Instructions_Stim.tStart = t  # local t and not account for scr refresh
            Instructions_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Stim, 'tStartRefresh')  # time at next scr refresh
            Instructions_Stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_Stim]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_Stim* updates
        if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_Stim.frameNStart = frameN  # exact frame index
            ITI_Stim.tStart = t  # local t and not account for scr refresh
            ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
            ITI_Stim.setAutoDraw(True)
        if ITI_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                ITI_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_Stim]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_Stim* updates
        if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_Stim.frameNStart = frameN  # exact frame index
            ITI_Stim.tStart = t  # local t and not account for scr refresh
            ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
            ITI_Stim.setAutoDraw(True)
        if ITI_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                ITI_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
# completed RedoLoop repeats of 'Redo_Instructions_Loop'


# --- Prepare to start Routine "Practice_Intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_IntroComponents = [Practice_Intro_Stim]
for thisComponent in Practice_IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_Intro" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Practice_Intro_Stim* updates
    if Practice_Intro_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Practice_Intro_Stim.frameNStart = frameN  # exact frame index
        Practice_Intro_Stim.tStart = t  # local t and not account for scr refresh
        Practice_Intro_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Practice_Intro_Stim, 'tStartRefresh')  # time at next scr refresh
        Practice_Intro_Stim.setAutoDraw(True)
    if Practice_Intro_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Practice_Intro_Stim.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Practice_Intro_Stim.tStop = t  # not accounting for scr refresh
            Practice_Intro_Stim.frameNStop = frameN  # exact frame index
            Practice_Intro_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_Intro" ---
for thisComponent in Practice_IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Pre_Encoding_Break" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Transition_Enc.keys = []
Transition_Enc.rt = []
_Transition_Enc_allKeys = []
# keep track of which components have finished
Pre_Encoding_BreakComponents = [Continue_Enc_Space, Transition_Prompt_Enc, Transition_Enc]
for thisComponent in Pre_Encoding_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Pre_Encoding_Break" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_Enc_Space* updates
    if Continue_Enc_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_Enc_Space.frameNStart = frameN  # exact frame index
        Continue_Enc_Space.tStart = t  # local t and not account for scr refresh
        Continue_Enc_Space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_Enc_Space, 'tStartRefresh')  # time at next scr refresh
        Continue_Enc_Space.setAutoDraw(True)
    
    # *Transition_Prompt_Enc* updates
    if Transition_Prompt_Enc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Prompt_Enc.frameNStart = frameN  # exact frame index
        Transition_Prompt_Enc.tStart = t  # local t and not account for scr refresh
        Transition_Prompt_Enc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Prompt_Enc, 'tStartRefresh')  # time at next scr refresh
        Transition_Prompt_Enc.setAutoDraw(True)
    
    # *Transition_Enc* updates
    waitOnFlip = False
    if Transition_Enc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Enc.frameNStart = frameN  # exact frame index
        Transition_Enc.tStart = t  # local t and not account for scr refresh
        Transition_Enc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Enc, 'tStartRefresh')  # time at next scr refresh
        Transition_Enc.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Transition_Enc.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Transition_Enc.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Transition_Enc.status == STARTED and not waitOnFlip:
        theseKeys = Transition_Enc.getKeys(keyList=['space'], waitRelease=False)
        _Transition_Enc_allKeys.extend(theseKeys)
        if len(_Transition_Enc_allKeys):
            Transition_Enc.keys = _Transition_Enc_allKeys[-1].name  # just the last key pressed
            Transition_Enc.rt = _Transition_Enc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pre_Encoding_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Pre_Encoding_Break" ---
for thisComponent in Pre_Encoding_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Transition_Enc.keys in ['', [], None]:  # No response was made
    Transition_Enc.keys = None
thisExp.addData('Transition_Enc.keys',Transition_Enc.keys)
if Transition_Enc.keys != None:  # we had a response
    thisExp.addData('Transition_Enc.rt', Transition_Enc.rt)
thisExp.nextEntry()
# the Routine "Pre_Encoding_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Title_Encoding" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from Deck_Loop
Cur_Deck = 1
Deck_Lpr = 'Deck '+str(Cur_Deck)
Enc_Loop_Count = 0
# keep track of which components have finished
Title_EncodingComponents = [Title_Encoding_Stim]
for thisComponent in Title_EncodingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Title_Encoding" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Title_Encoding_Stim* updates
    if Title_Encoding_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Title_Encoding_Stim.frameNStart = frameN  # exact frame index
        Title_Encoding_Stim.tStart = t  # local t and not account for scr refresh
        Title_Encoding_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Title_Encoding_Stim, 'tStartRefresh')  # time at next scr refresh
        Title_Encoding_Stim.setAutoDraw(True)
    if Title_Encoding_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Title_Encoding_Stim.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Title_Encoding_Stim.tStop = t  # not accounting for scr refresh
            Title_Encoding_Stim.frameNStop = frameN  # exact frame index
            Title_Encoding_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Title_EncodingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Title_Encoding" ---
for thisComponent in Title_EncodingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Deck" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Deck_Stim.setText(Deck_Lpr
)
# keep track of which components have finished
DeckComponents = [Deck_Stim]
for thisComponent in DeckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Deck" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Deck_Stim* updates
    if Deck_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Deck_Stim.frameNStart = frameN  # exact frame index
        Deck_Stim.tStart = t  # local t and not account for scr refresh
        Deck_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Deck_Stim, 'tStartRefresh')  # time at next scr refresh
        Deck_Stim.setAutoDraw(True)
    if Deck_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Deck_Stim.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            Deck_Stim.tStop = t  # not accounting for scr refresh
            Deck_Stim.frameNStop = frameN  # exact frame index
            Deck_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DeckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Deck" ---
for thisComponent in DeckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Deck_Loopr
Cur_Deck += 1
Deck_Lpr = 'Deck '+str(Cur_Deck)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# set up handler to look after randomisation of conditions etc
Practice_Encoding_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practice.csv'),
    seed=None, name='Practice_Encoding_Loop')
thisExp.addLoop(Practice_Encoding_Loop)  # add the loop to the experiment
thisPractice_Encoding_Loop = Practice_Encoding_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_Encoding_Loop.rgb)
if thisPractice_Encoding_Loop != None:
    for paramName in thisPractice_Encoding_Loop:
        exec('{} = thisPractice_Encoding_Loop[paramName]'.format(paramName))

for thisPractice_Encoding_Loop in Practice_Encoding_Loop:
    currentLoop = Practice_Encoding_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Encoding_Loop.rgb)
    if thisPractice_Encoding_Loop != None:
        for paramName in thisPractice_Encoding_Loop:
            exec('{} = thisPractice_Encoding_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Dealer_Stim.setImage('Dealer.png')
    # keep track of which components have finished
    FixationComponents = [Dealer_Stim]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Dealer_Stim* updates
        if Dealer_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Dealer_Stim.frameNStart = frameN  # exact frame index
            Dealer_Stim.tStart = t  # local t and not account for scr refresh
            Dealer_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dealer_Stim, 'tStartRefresh')  # time at next scr refresh
            Dealer_Stim.setAutoDraw(True)
        if Dealer_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Dealer_Stim.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Dealer_Stim.tStop = t  # not accounting for scr refresh
                Dealer_Stim.frameNStop = frameN  # exact frame index
                Dealer_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation" ---
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Encoding" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Encoding_Resp.keys = []
    Encoding_Resp.rt = []
    _Encoding_Resp_allKeys = []
    # Run 'Begin Routine' code from Key_Tracking_Code
    Attn = 0
    Brk_Enc = 0
    PrcAttn = 0
    PrcBrk_Enc = 0
    Resp_Fail = 0
    FB = 1
    L_Sq_FB_Stim.lineColor=[-1.0000, -1.0000, -1.0000]
    R_Sq_FB_Stim.lineColor=[-1.0000, -1.0000, -1.0000]
        
    
    L_Scene_Stim.setImage(L_Scene)
    R_Scene_Stim.setImage(R_Scene)
    # keep track of which components have finished
    EncodingComponents = [L_Sq_Stim, R_Sq_Stim, Encoding_Resp, L_Scene_Stim, R_Scene_Stim]
    for thisComponent in EncodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Encoding" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *L_Sq_Stim* updates
        if L_Sq_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_Sq_Stim.frameNStart = frameN  # exact frame index
            L_Sq_Stim.tStart = t  # local t and not account for scr refresh
            L_Sq_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_Sq_Stim, 'tStartRefresh')  # time at next scr refresh
            L_Sq_Stim.setAutoDraw(True)
        if L_Sq_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_Sq_Stim.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                L_Sq_Stim.tStop = t  # not accounting for scr refresh
                L_Sq_Stim.frameNStop = frameN  # exact frame index
                L_Sq_Stim.setAutoDraw(False)
        
        # *R_Sq_Stim* updates
        if R_Sq_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_Sq_Stim.frameNStart = frameN  # exact frame index
            R_Sq_Stim.tStart = t  # local t and not account for scr refresh
            R_Sq_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_Sq_Stim, 'tStartRefresh')  # time at next scr refresh
            R_Sq_Stim.setAutoDraw(True)
        if R_Sq_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R_Sq_Stim.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                R_Sq_Stim.tStop = t  # not accounting for scr refresh
                R_Sq_Stim.frameNStop = frameN  # exact frame index
                R_Sq_Stim.setAutoDraw(False)
        
        # *Encoding_Resp* updates
        waitOnFlip = False
        if Encoding_Resp.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
            # keep track of start time/frame for later
            Encoding_Resp.frameNStart = frameN  # exact frame index
            Encoding_Resp.tStart = t  # local t and not account for scr refresh
            Encoding_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Encoding_Resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Encoding_Resp.started')
            Encoding_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Encoding_Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Encoding_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Encoding_Resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Encoding_Resp.tStartRefresh + 3.7-frameTolerance:
                # keep track of stop time/frame for later
                Encoding_Resp.tStop = t  # not accounting for scr refresh
                Encoding_Resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Encoding_Resp.stopped')
                Encoding_Resp.status = FINISHED
        if Encoding_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Encoding_Resp.getKeys(keyList=['q','p'], waitRelease=False)
            _Encoding_Resp_allKeys.extend(theseKeys)
            if len(_Encoding_Resp_allKeys):
                Encoding_Resp.keys = _Encoding_Resp_allKeys[-1].name  # just the last key pressed
                Encoding_Resp.rt = _Encoding_Resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *L_Scene_Stim* updates
        if L_Scene_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_Scene_Stim.frameNStart = frameN  # exact frame index
            L_Scene_Stim.tStart = t  # local t and not account for scr refresh
            L_Scene_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_Scene_Stim, 'tStartRefresh')  # time at next scr refresh
            L_Scene_Stim.setAutoDraw(True)
        if L_Scene_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_Scene_Stim.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                L_Scene_Stim.tStop = t  # not accounting for scr refresh
                L_Scene_Stim.frameNStop = frameN  # exact frame index
                L_Scene_Stim.setAutoDraw(False)
        
        # *R_Scene_Stim* updates
        if R_Scene_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_Scene_Stim.frameNStart = frameN  # exact frame index
            R_Scene_Stim.tStart = t  # local t and not account for scr refresh
            R_Scene_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_Scene_Stim, 'tStartRefresh')  # time at next scr refresh
            R_Scene_Stim.setAutoDraw(True)
        if R_Scene_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R_Scene_Stim.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                R_Scene_Stim.tStop = t  # not accounting for scr refresh
                R_Scene_Stim.frameNStop = frameN  # exact frame index
                R_Scene_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Encoding" ---
    for thisComponent in EncodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Encoding_Resp.keys in ['', [], None]:  # No response was made
        Encoding_Resp.keys = None
    Practice_Encoding_Loop.addData('Encoding_Resp.keys',Encoding_Resp.keys)
    if Encoding_Resp.keys != None:  # we had a response
        Practice_Encoding_Loop.addData('Encoding_Resp.rt', Encoding_Resp.rt)
    # Run 'End Routine' code from Key_Tracking_Code
    if Encoding_Resp.keys == 'q':
        Choice_List.append('L')
    else:
        Choice_List.append('R')
    Loop_Count += 1
    if Loop_Count >= 12:
        Attn = 1
        Loop_Count = 0
    Enc_Loop_Count += 1
    if Enc_Loop_Count >= 24:
        Brk_Enc = 1
        Enc_Loop_Count = 0
        ProT += 1
    PrcLoop_Count += 1
    if PrcLoop_Count >= 5:
        PrcAttn = 1
        PrcLoop_Count = 0
    PrcEnc_Loop_Count += 1
    if PrcEnc_Loop_Count >= 10:
        PrcBrk_Enc = 1
        PrcEnc_Loop_Count = 0
    if not Encoding_Resp.keys:
        Resp_Fail = 1
        FB = 0
    ProTracker = "Picture"+str(ProT)+".png"
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # set up handler to look after randomisation of conditions etc
    Practice_Response_Fail_Loop = data.TrialHandler(nReps=Resp_Fail, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Practice_Response_Fail_Loop')
    thisExp.addLoop(Practice_Response_Fail_Loop)  # add the loop to the experiment
    thisPractice_Response_Fail_Loop = Practice_Response_Fail_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Response_Fail_Loop.rgb)
    if thisPractice_Response_Fail_Loop != None:
        for paramName in thisPractice_Response_Fail_Loop:
            exec('{} = thisPractice_Response_Fail_Loop[paramName]'.format(paramName))
    
    for thisPractice_Response_Fail_Loop in Practice_Response_Fail_Loop:
        currentLoop = Practice_Response_Fail_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Response_Fail_Loop.rgb)
        if thisPractice_Response_Fail_Loop != None:
            for paramName in thisPractice_Response_Fail_Loop:
                exec('{} = thisPractice_Response_Fail_Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Response_Fail" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Response_FailComponents = [Fail_Too_Text, Fail_Slow_Text]
        for thisComponent in Response_FailComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Response_Fail" ---
        while continueRoutine and routineTimer.getTime() < 2.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fail_Too_Text* updates
            if Fail_Too_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fail_Too_Text.frameNStart = frameN  # exact frame index
                Fail_Too_Text.tStart = t  # local t and not account for scr refresh
                Fail_Too_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fail_Too_Text, 'tStartRefresh')  # time at next scr refresh
                Fail_Too_Text.setAutoDraw(True)
            if Fail_Too_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fail_Too_Text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fail_Too_Text.tStop = t  # not accounting for scr refresh
                    Fail_Too_Text.frameNStop = frameN  # exact frame index
                    Fail_Too_Text.setAutoDraw(False)
            
            # *Fail_Slow_Text* updates
            if Fail_Slow_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fail_Slow_Text.frameNStart = frameN  # exact frame index
                Fail_Slow_Text.tStart = t  # local t and not account for scr refresh
                Fail_Slow_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fail_Slow_Text, 'tStartRefresh')  # time at next scr refresh
                Fail_Slow_Text.setAutoDraw(True)
            if Fail_Slow_Text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fail_Slow_Text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fail_Slow_Text.tStop = t  # not accounting for scr refresh
                    Fail_Slow_Text.frameNStop = frameN  # exact frame index
                    Fail_Slow_Text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Response_FailComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Response_Fail" ---
        for thisComponent in Response_FailComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.500000)
    # completed Resp_Fail repeats of 'Practice_Response_Fail_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Practice_FB_Loop = data.TrialHandler(nReps=FB, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Practice_FB_Loop')
    thisExp.addLoop(Practice_FB_Loop)  # add the loop to the experiment
    thisPractice_FB_Loop = Practice_FB_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_FB_Loop.rgb)
    if thisPractice_FB_Loop != None:
        for paramName in thisPractice_FB_Loop:
            exec('{} = thisPractice_FB_Loop[paramName]'.format(paramName))
    
    for thisPractice_FB_Loop in Practice_FB_Loop:
        currentLoop = Practice_FB_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_FB_Loop.rgb)
        if thisPractice_FB_Loop != None:
            for paramName in thisPractice_FB_Loop:
                exec('{} = thisPractice_FB_Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Border_code
        if Encoding_Resp.keys:
            if Encoding_Resp.keys[-1] == 'q':
                L_Sq_FB_Stim.lineColor=[1.0000, -1.0000, -1.0000]
                R_Scene_FB_Stim.opacity=0
                R_Point_Mask.opacity=1
                R_Sq_FB_Stim.opacity=0
            elif Encoding_Resp.keys[-1]  == 'p':
                R_Sq_FB_Stim.lineColor=[1.0000, -1.0000, -1.0000]
                L_Scene_FB_Stim.opacity=0
                L_Point_Mask.opacity=1
                L_Sq_FB_Stim.opacity=0
        R_Scene_FB_Stim.setImage(R_Scene)
        L_Scene_FB_Stim.setImage(L_Scene)
        L_Point_FB_Stim.setText(Points_L)
        R_Point_FB_Stim.setText(Points_R)
        # keep track of which components have finished
        FeedbackComponents = [R_Sq_FB_Stim, L_Sq_FB_Stim, R_Scene_FB_Stim, L_Scene_FB_Stim, L_Point_FB_Stim, R_Point_FB_Stim, L_Point_Mask, R_Point_Mask]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback" ---
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *R_Sq_FB_Stim* updates
            if R_Sq_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Sq_FB_Stim.frameNStart = frameN  # exact frame index
                R_Sq_FB_Stim.tStart = t  # local t and not account for scr refresh
                R_Sq_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Sq_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                R_Sq_FB_Stim.setAutoDraw(True)
            if R_Sq_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Sq_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Sq_FB_Stim.tStop = t  # not accounting for scr refresh
                    R_Sq_FB_Stim.frameNStop = frameN  # exact frame index
                    R_Sq_FB_Stim.setAutoDraw(False)
            
            # *L_Sq_FB_Stim* updates
            if L_Sq_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Sq_FB_Stim.frameNStart = frameN  # exact frame index
                L_Sq_FB_Stim.tStart = t  # local t and not account for scr refresh
                L_Sq_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Sq_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                L_Sq_FB_Stim.setAutoDraw(True)
            if L_Sq_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Sq_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Sq_FB_Stim.tStop = t  # not accounting for scr refresh
                    L_Sq_FB_Stim.frameNStop = frameN  # exact frame index
                    L_Sq_FB_Stim.setAutoDraw(False)
            
            # *R_Scene_FB_Stim* updates
            if R_Scene_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Scene_FB_Stim.frameNStart = frameN  # exact frame index
                R_Scene_FB_Stim.tStart = t  # local t and not account for scr refresh
                R_Scene_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Scene_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                R_Scene_FB_Stim.setAutoDraw(True)
            if R_Scene_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Scene_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Scene_FB_Stim.tStop = t  # not accounting for scr refresh
                    R_Scene_FB_Stim.frameNStop = frameN  # exact frame index
                    R_Scene_FB_Stim.setAutoDraw(False)
            
            # *L_Scene_FB_Stim* updates
            if L_Scene_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Scene_FB_Stim.frameNStart = frameN  # exact frame index
                L_Scene_FB_Stim.tStart = t  # local t and not account for scr refresh
                L_Scene_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Scene_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                L_Scene_FB_Stim.setAutoDraw(True)
            if L_Scene_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Scene_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Scene_FB_Stim.tStop = t  # not accounting for scr refresh
                    L_Scene_FB_Stim.frameNStop = frameN  # exact frame index
                    L_Scene_FB_Stim.setAutoDraw(False)
            
            # *L_Point_FB_Stim* updates
            if L_Point_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Point_FB_Stim.frameNStart = frameN  # exact frame index
                L_Point_FB_Stim.tStart = t  # local t and not account for scr refresh
                L_Point_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Point_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                L_Point_FB_Stim.setAutoDraw(True)
            if L_Point_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Point_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Point_FB_Stim.tStop = t  # not accounting for scr refresh
                    L_Point_FB_Stim.frameNStop = frameN  # exact frame index
                    L_Point_FB_Stim.setAutoDraw(False)
            
            # *R_Point_FB_Stim* updates
            if R_Point_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Point_FB_Stim.frameNStart = frameN  # exact frame index
                R_Point_FB_Stim.tStart = t  # local t and not account for scr refresh
                R_Point_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Point_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_Point_FB_Stim.started')
                R_Point_FB_Stim.setAutoDraw(True)
            if R_Point_FB_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Point_FB_Stim.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Point_FB_Stim.tStop = t  # not accounting for scr refresh
                    R_Point_FB_Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'R_Point_FB_Stim.stopped')
                    R_Point_FB_Stim.setAutoDraw(False)
            
            # *L_Point_Mask* updates
            if L_Point_Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Point_Mask.frameNStart = frameN  # exact frame index
                L_Point_Mask.tStart = t  # local t and not account for scr refresh
                L_Point_Mask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Point_Mask, 'tStartRefresh')  # time at next scr refresh
                L_Point_Mask.setAutoDraw(True)
            if L_Point_Mask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Point_Mask.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Point_Mask.tStop = t  # not accounting for scr refresh
                    L_Point_Mask.frameNStop = frameN  # exact frame index
                    L_Point_Mask.setAutoDraw(False)
            
            # *R_Point_Mask* updates
            if R_Point_Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Point_Mask.frameNStart = frameN  # exact frame index
                R_Point_Mask.tStart = t  # local t and not account for scr refresh
                R_Point_Mask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Point_Mask, 'tStartRefresh')  # time at next scr refresh
                R_Point_Mask.setAutoDraw(True)
            if R_Point_Mask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Point_Mask.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Point_Mask.tStop = t  # not accounting for scr refresh
                    R_Point_Mask.frameNStop = frameN  # exact frame index
                    R_Point_Mask.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from Border_code
        R_Scene_FB_Stim.opacity=1.0
        R_Point_Mask.opacity=0
        L_Scene_FB_Stim.opacity=1.0
        L_Point_Mask.opacity=0
        L_Sq_FB_Stim.opacity=1
        R_Sq_FB_Stim.opacity=1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
    # completed FB repeats of 'Practice_FB_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Practice_Attention_Loop = data.TrialHandler(nReps=PrcAttn, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Practice_Attention_Loop')
    thisExp.addLoop(Practice_Attention_Loop)  # add the loop to the experiment
    thisPractice_Attention_Loop = Practice_Attention_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Attention_Loop.rgb)
    if thisPractice_Attention_Loop != None:
        for paramName in thisPractice_Attention_Loop:
            exec('{} = thisPractice_Attention_Loop[paramName]'.format(paramName))
    
    for thisPractice_Attention_Loop in Practice_Attention_Loop:
        currentLoop = Practice_Attention_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Attention_Loop.rgb)
        if thisPractice_Attention_Loop != None:
            for paramName in thisPractice_Attention_Loop:
                exec('{} = thisPractice_Attention_Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Attention" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Attn_Stim.setImage('AttnSlide.png')
        Attn_resp.keys = []
        Attn_resp.rt = []
        _Attn_resp_allKeys = []
        # keep track of which components have finished
        AttentionComponents = [Attn_Stim, Attn_resp]
        for thisComponent in AttentionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Attention" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Attn_Stim* updates
            if Attn_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Attn_Stim.frameNStart = frameN  # exact frame index
                Attn_Stim.tStart = t  # local t and not account for scr refresh
                Attn_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Attn_Stim, 'tStartRefresh')  # time at next scr refresh
                Attn_Stim.setAutoDraw(True)
            
            # *Attn_resp* updates
            waitOnFlip = False
            if Attn_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Attn_resp.frameNStart = frameN  # exact frame index
                Attn_resp.tStart = t  # local t and not account for scr refresh
                Attn_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Attn_resp, 'tStartRefresh')  # time at next scr refresh
                Attn_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Attn_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Attn_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Attn_resp.status == STARTED and not waitOnFlip:
                theseKeys = Attn_resp.getKeys(keyList=['0', '1', '2', '3', '4', '5'], waitRelease=False)
                _Attn_resp_allKeys.extend(theseKeys)
                if len(_Attn_resp_allKeys):
                    Attn_resp.keys = _Attn_resp_allKeys[-1].name  # just the last key pressed
                    Attn_resp.rt = _Attn_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AttentionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Attention" ---
        for thisComponent in AttentionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Attn_resp.keys in ['', [], None]:  # No response was made
            Attn_resp.keys = None
        Practice_Attention_Loop.addData('Attn_resp.keys',Attn_resp.keys)
        if Attn_resp.keys != None:  # we had a response
            Practice_Attention_Loop.addData('Attn_resp.rt', Attn_resp.rt)
        # the Routine "Attention" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed PrcAttn repeats of 'Practice_Attention_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Practice_EncBrk_Loop = data.TrialHandler(nReps=PrcBrk_Enc, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Practice_EncBrk_Loop')
    thisExp.addLoop(Practice_EncBrk_Loop)  # add the loop to the experiment
    thisPractice_EncBrk_Loop = Practice_EncBrk_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_EncBrk_Loop.rgb)
    if thisPractice_EncBrk_Loop != None:
        for paramName in thisPractice_EncBrk_Loop:
            exec('{} = thisPractice_EncBrk_Loop[paramName]'.format(paramName))
    
    for thisPractice_EncBrk_Loop in Practice_EncBrk_Loop:
        currentLoop = Practice_EncBrk_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_EncBrk_Loop.rgb)
        if thisPractice_EncBrk_Loop != None:
            for paramName in thisPractice_EncBrk_Loop:
                exec('{} = thisPractice_EncBrk_Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Coins" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Coin_Animation.setOpacity(1.0)
        Coin_Animation.setContrast(None)
        Coin_Animation.setMovie('coin.mp4')
        # keep track of which components have finished
        CoinsComponents = [Coin_Animation]
        for thisComponent in CoinsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Coins" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Coin_Animation* updates
            if Coin_Animation.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                Coin_Animation.frameNStart = frameN  # exact frame index
                Coin_Animation.tStart = t  # local t and not account for scr refresh
                Coin_Animation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Coin_Animation, 'tStartRefresh')  # time at next scr refresh
                Coin_Animation.setAutoDraw(True)
                Coin_Animation.play()
            if Coin_Animation.status == FINISHED:  # force-end the routine
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CoinsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Coins" ---
        for thisComponent in CoinsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Coin_Animation.stop()
        # the Routine "Coins" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Encoding_Break" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        EncBrk_Resp.keys = []
        EncBrk_Resp.rt = []
        _EncBrk_Resp_allKeys = []
        Point_Report_Stim.setText(PtTotal)
        Progress_Tracker.setImage(ProTracker)
        # keep track of which components have finished
        Encoding_BreakComponents = [EncBrk_Prompt, Cont_Enc_Stim, EncBrk_Warning_Prompt, Cont_EncBrk_Prompt, EncBrk_Resp, Point_Report_Prompt, Point_Report_Stim, Progress_Tracker, Perc_stim]
        for thisComponent in Encoding_BreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encoding_Break" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EncBrk_Prompt* updates
            if EncBrk_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EncBrk_Prompt.frameNStart = frameN  # exact frame index
                EncBrk_Prompt.tStart = t  # local t and not account for scr refresh
                EncBrk_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncBrk_Prompt, 'tStartRefresh')  # time at next scr refresh
                EncBrk_Prompt.setAutoDraw(True)
            if EncBrk_Prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncBrk_Prompt.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    EncBrk_Prompt.tStop = t  # not accounting for scr refresh
                    EncBrk_Prompt.frameNStop = frameN  # exact frame index
                    EncBrk_Prompt.setAutoDraw(False)
            
            # *Cont_Enc_Stim* updates
            if Cont_Enc_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cont_Enc_Stim.frameNStart = frameN  # exact frame index
                Cont_Enc_Stim.tStart = t  # local t and not account for scr refresh
                Cont_Enc_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cont_Enc_Stim, 'tStartRefresh')  # time at next scr refresh
                Cont_Enc_Stim.setAutoDraw(True)
            
            # *EncBrk_Warning_Prompt* updates
            if EncBrk_Warning_Prompt.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
                # keep track of start time/frame for later
                EncBrk_Warning_Prompt.frameNStart = frameN  # exact frame index
                EncBrk_Warning_Prompt.tStart = t  # local t and not account for scr refresh
                EncBrk_Warning_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncBrk_Warning_Prompt, 'tStartRefresh')  # time at next scr refresh
                EncBrk_Warning_Prompt.setAutoDraw(True)
            if EncBrk_Warning_Prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EncBrk_Warning_Prompt.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    EncBrk_Warning_Prompt.tStop = t  # not accounting for scr refresh
                    EncBrk_Warning_Prompt.frameNStop = frameN  # exact frame index
                    EncBrk_Warning_Prompt.setAutoDraw(False)
            
            # *Cont_EncBrk_Prompt* updates
            if Cont_EncBrk_Prompt.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
                # keep track of start time/frame for later
                Cont_EncBrk_Prompt.frameNStart = frameN  # exact frame index
                Cont_EncBrk_Prompt.tStart = t  # local t and not account for scr refresh
                Cont_EncBrk_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cont_EncBrk_Prompt, 'tStartRefresh')  # time at next scr refresh
                Cont_EncBrk_Prompt.setAutoDraw(True)
            
            # *EncBrk_Resp* updates
            waitOnFlip = False
            if EncBrk_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EncBrk_Resp.frameNStart = frameN  # exact frame index
                EncBrk_Resp.tStart = t  # local t and not account for scr refresh
                EncBrk_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EncBrk_Resp, 'tStartRefresh')  # time at next scr refresh
                EncBrk_Resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EncBrk_Resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EncBrk_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EncBrk_Resp.status == STARTED and not waitOnFlip:
                theseKeys = EncBrk_Resp.getKeys(keyList=['space'], waitRelease=False)
                _EncBrk_Resp_allKeys.extend(theseKeys)
                if len(_EncBrk_Resp_allKeys):
                    EncBrk_Resp.keys = _EncBrk_Resp_allKeys[-1].name  # just the last key pressed
                    EncBrk_Resp.rt = _EncBrk_Resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *Point_Report_Prompt* updates
            if Point_Report_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Point_Report_Prompt.frameNStart = frameN  # exact frame index
                Point_Report_Prompt.tStart = t  # local t and not account for scr refresh
                Point_Report_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Point_Report_Prompt, 'tStartRefresh')  # time at next scr refresh
                Point_Report_Prompt.setAutoDraw(True)
            if Point_Report_Prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Point_Report_Prompt.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    Point_Report_Prompt.tStop = t  # not accounting for scr refresh
                    Point_Report_Prompt.frameNStop = frameN  # exact frame index
                    Point_Report_Prompt.setAutoDraw(False)
            
            # *Point_Report_Stim* updates
            if Point_Report_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Point_Report_Stim.frameNStart = frameN  # exact frame index
                Point_Report_Stim.tStart = t  # local t and not account for scr refresh
                Point_Report_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Point_Report_Stim, 'tStartRefresh')  # time at next scr refresh
                Point_Report_Stim.setAutoDraw(True)
            if Point_Report_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Point_Report_Stim.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    Point_Report_Stim.tStop = t  # not accounting for scr refresh
                    Point_Report_Stim.frameNStop = frameN  # exact frame index
                    Point_Report_Stim.setAutoDraw(False)
            
            # *Progress_Tracker* updates
            if Progress_Tracker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Progress_Tracker.frameNStart = frameN  # exact frame index
                Progress_Tracker.tStart = t  # local t and not account for scr refresh
                Progress_Tracker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Progress_Tracker, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Progress_Tracker.started')
                Progress_Tracker.setAutoDraw(True)
            
            # *Perc_stim* updates
            if Perc_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Perc_stim.frameNStart = frameN  # exact frame index
                Perc_stim.tStart = t  # local t and not account for scr refresh
                Perc_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Perc_stim, 'tStartRefresh')  # time at next scr refresh
                Perc_stim.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encoding_Break" ---
        for thisComponent in Encoding_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EncBrk_Resp.keys in ['', [], None]:  # No response was made
            EncBrk_Resp.keys = None
        Practice_EncBrk_Loop.addData('EncBrk_Resp.keys',EncBrk_Resp.keys)
        if EncBrk_Resp.keys != None:  # we had a response
            Practice_EncBrk_Loop.addData('EncBrk_Resp.rt', EncBrk_Resp.rt)
        # the Routine "Encoding_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed PrcBrk_Enc repeats of 'Practice_EncBrk_Loop'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Practice_Encoding_Loop'


# --- Prepare to start Routine "ITI" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
ITIComponents = [ITI_Stim]
for thisComponent in ITIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ITI" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ITI_Stim* updates
    if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ITI_Stim.frameNStart = frameN  # exact frame index
        ITI_Stim.tStart = t  # local t and not account for scr refresh
        ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
        ITI_Stim.setAutoDraw(True)
    if ITI_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            ITI_Stim.tStop = t  # not accounting for scr refresh
            ITI_Stim.frameNStop = frameN  # exact frame index
            ITI_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ITI" ---
for thisComponent in ITIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "Practice_End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Practice_EndComponents = [practice_encoding_stim]
for thisComponent in Practice_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Practice_End" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_encoding_stim* updates
    if practice_encoding_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_encoding_stim.frameNStart = frameN  # exact frame index
        practice_encoding_stim.tStart = t  # local t and not account for scr refresh
        practice_encoding_stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_encoding_stim, 'tStartRefresh')  # time at next scr refresh
        practice_encoding_stim.setAutoDraw(True)
    if practice_encoding_stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_encoding_stim.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            practice_encoding_stim.tStop = t  # not accounting for scr refresh
            practice_encoding_stim.frameNStop = frameN  # exact frame index
            practice_encoding_stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Practice_End" ---
for thisComponent in Practice_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Exp_Intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Transition_Stim_Response.keys = []
Transition_Stim_Response.rt = []
_Transition_Stim_Response_allKeys = []
# keep track of which components have finished
Exp_IntroComponents = [Transition_Stim_Response, Transition_Stim, Space_Stim]
for thisComponent in Exp_IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Exp_Intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Transition_Stim_Response* updates
    waitOnFlip = False
    if Transition_Stim_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Stim_Response.frameNStart = frameN  # exact frame index
        Transition_Stim_Response.tStart = t  # local t and not account for scr refresh
        Transition_Stim_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Stim_Response, 'tStartRefresh')  # time at next scr refresh
        Transition_Stim_Response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Transition_Stim_Response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Transition_Stim_Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Transition_Stim_Response.status == STARTED and not waitOnFlip:
        theseKeys = Transition_Stim_Response.getKeys(keyList=['space'], waitRelease=False)
        _Transition_Stim_Response_allKeys.extend(theseKeys)
        if len(_Transition_Stim_Response_allKeys):
            Transition_Stim_Response.keys = _Transition_Stim_Response_allKeys[-1].name  # just the last key pressed
            Transition_Stim_Response.rt = _Transition_Stim_Response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Transition_Stim* updates
    if Transition_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Stim.frameNStart = frameN  # exact frame index
        Transition_Stim.tStart = t  # local t and not account for scr refresh
        Transition_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Stim, 'tStartRefresh')  # time at next scr refresh
        Transition_Stim.setAutoDraw(True)
    
    # *Space_Stim* updates
    if Space_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space_Stim.frameNStart = frameN  # exact frame index
        Space_Stim.tStart = t  # local t and not account for scr refresh
        Space_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space_Stim, 'tStartRefresh')  # time at next scr refresh
        Space_Stim.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Exp_IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Exp_Intro" ---
for thisComponent in Exp_IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Exp_Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Pre_Encoding_Break" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Transition_Enc.keys = []
Transition_Enc.rt = []
_Transition_Enc_allKeys = []
# keep track of which components have finished
Pre_Encoding_BreakComponents = [Continue_Enc_Space, Transition_Prompt_Enc, Transition_Enc]
for thisComponent in Pre_Encoding_BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Pre_Encoding_Break" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Continue_Enc_Space* updates
    if Continue_Enc_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue_Enc_Space.frameNStart = frameN  # exact frame index
        Continue_Enc_Space.tStart = t  # local t and not account for scr refresh
        Continue_Enc_Space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_Enc_Space, 'tStartRefresh')  # time at next scr refresh
        Continue_Enc_Space.setAutoDraw(True)
    
    # *Transition_Prompt_Enc* updates
    if Transition_Prompt_Enc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Prompt_Enc.frameNStart = frameN  # exact frame index
        Transition_Prompt_Enc.tStart = t  # local t and not account for scr refresh
        Transition_Prompt_Enc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Prompt_Enc, 'tStartRefresh')  # time at next scr refresh
        Transition_Prompt_Enc.setAutoDraw(True)
    
    # *Transition_Enc* updates
    waitOnFlip = False
    if Transition_Enc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Transition_Enc.frameNStart = frameN  # exact frame index
        Transition_Enc.tStart = t  # local t and not account for scr refresh
        Transition_Enc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transition_Enc, 'tStartRefresh')  # time at next scr refresh
        Transition_Enc.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Transition_Enc.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Transition_Enc.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Transition_Enc.status == STARTED and not waitOnFlip:
        theseKeys = Transition_Enc.getKeys(keyList=['space'], waitRelease=False)
        _Transition_Enc_allKeys.extend(theseKeys)
        if len(_Transition_Enc_allKeys):
            Transition_Enc.keys = _Transition_Enc_allKeys[-1].name  # just the last key pressed
            Transition_Enc.rt = _Transition_Enc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pre_Encoding_BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Pre_Encoding_Break" ---
for thisComponent in Pre_Encoding_BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Transition_Enc.keys in ['', [], None]:  # No response was made
    Transition_Enc.keys = None
thisExp.addData('Transition_Enc.keys',Transition_Enc.keys)
if Transition_Enc.keys != None:  # we had a response
    thisExp.addData('Transition_Enc.rt', Transition_Enc.rt)
thisExp.nextEntry()
# the Routine "Pre_Encoding_Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Title_Encoding" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from Deck_Loop
Cur_Deck = 1
Deck_Lpr = 'Deck '+str(Cur_Deck)
Enc_Loop_Count = 0
# keep track of which components have finished
Title_EncodingComponents = [Title_Encoding_Stim]
for thisComponent in Title_EncodingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Title_Encoding" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Title_Encoding_Stim* updates
    if Title_Encoding_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Title_Encoding_Stim.frameNStart = frameN  # exact frame index
        Title_Encoding_Stim.tStart = t  # local t and not account for scr refresh
        Title_Encoding_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Title_Encoding_Stim, 'tStartRefresh')  # time at next scr refresh
        Title_Encoding_Stim.setAutoDraw(True)
    if Title_Encoding_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Title_Encoding_Stim.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Title_Encoding_Stim.tStop = t  # not accounting for scr refresh
            Title_Encoding_Stim.frameNStop = frameN  # exact frame index
            Title_Encoding_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Title_EncodingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Title_Encoding" ---
for thisComponent in Title_EncodingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Encoding_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Group_"+expInfo['Group']+".csv"),
    seed=None, name='Encoding_Loop')
thisExp.addLoop(Encoding_Loop)  # add the loop to the experiment
thisEncoding_Loop = Encoding_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncoding_Loop.rgb)
if thisEncoding_Loop != None:
    for paramName in thisEncoding_Loop:
        exec('{} = thisEncoding_Loop[paramName]'.format(paramName))

for thisEncoding_Loop in Encoding_Loop:
    currentLoop = Encoding_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisEncoding_Loop.rgb)
    if thisEncoding_Loop != None:
        for paramName in thisEncoding_Loop:
            exec('{} = thisEncoding_Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Deck" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Deck_Stim.setText(Deck_Lpr
)
    # keep track of which components have finished
    DeckComponents = [Deck_Stim]
    for thisComponent in DeckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Deck" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Deck_Stim* updates
        if Deck_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Deck_Stim.frameNStart = frameN  # exact frame index
            Deck_Stim.tStart = t  # local t and not account for scr refresh
            Deck_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Deck_Stim, 'tStartRefresh')  # time at next scr refresh
            Deck_Stim.setAutoDraw(True)
        if Deck_Stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Deck_Stim.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Deck_Stim.tStop = t  # not accounting for scr refresh
                Deck_Stim.frameNStop = frameN  # exact frame index
                Deck_Stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DeckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Deck" ---
    for thisComponent in DeckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Deck_Loopr
    Cur_Deck += 1
    Deck_Lpr = 'Deck '+str(Cur_Deck)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    EncStim_Loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blockFile),
        seed=None, name='EncStim_Loop')
    thisExp.addLoop(EncStim_Loop)  # add the loop to the experiment
    thisEncStim_Loop = EncStim_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncStim_Loop.rgb)
    if thisEncStim_Loop != None:
        for paramName in thisEncStim_Loop:
            exec('{} = thisEncStim_Loop[paramName]'.format(paramName))
    
    for thisEncStim_Loop in EncStim_Loop:
        currentLoop = EncStim_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisEncStim_Loop.rgb)
        if thisEncStim_Loop != None:
            for paramName in thisEncStim_Loop:
                exec('{} = thisEncStim_Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Dealer_Stim.setImage('Dealer.png')
        # keep track of which components have finished
        FixationComponents = [Dealer_Stim]
        for thisComponent in FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Dealer_Stim* updates
            if Dealer_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Dealer_Stim.frameNStart = frameN  # exact frame index
                Dealer_Stim.tStart = t  # local t and not account for scr refresh
                Dealer_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Dealer_Stim, 'tStartRefresh')  # time at next scr refresh
                Dealer_Stim.setAutoDraw(True)
            if Dealer_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Dealer_Stim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Dealer_Stim.tStop = t  # not accounting for scr refresh
                    Dealer_Stim.frameNStop = frameN  # exact frame index
                    Dealer_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation" ---
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Encoding" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Encoding_Resp.keys = []
        Encoding_Resp.rt = []
        _Encoding_Resp_allKeys = []
        # Run 'Begin Routine' code from Key_Tracking_Code
        Attn = 0
        Brk_Enc = 0
        PrcAttn = 0
        PrcBrk_Enc = 0
        Resp_Fail = 0
        FB = 1
        L_Sq_FB_Stim.lineColor=[-1.0000, -1.0000, -1.0000]
        R_Sq_FB_Stim.lineColor=[-1.0000, -1.0000, -1.0000]
            
        
        L_Scene_Stim.setImage(L_Scene)
        R_Scene_Stim.setImage(R_Scene)
        # keep track of which components have finished
        EncodingComponents = [L_Sq_Stim, R_Sq_Stim, Encoding_Resp, L_Scene_Stim, R_Scene_Stim]
        for thisComponent in EncodingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encoding" ---
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *L_Sq_Stim* updates
            if L_Sq_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Sq_Stim.frameNStart = frameN  # exact frame index
                L_Sq_Stim.tStart = t  # local t and not account for scr refresh
                L_Sq_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Sq_Stim, 'tStartRefresh')  # time at next scr refresh
                L_Sq_Stim.setAutoDraw(True)
            if L_Sq_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Sq_Stim.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Sq_Stim.tStop = t  # not accounting for scr refresh
                    L_Sq_Stim.frameNStop = frameN  # exact frame index
                    L_Sq_Stim.setAutoDraw(False)
            
            # *R_Sq_Stim* updates
            if R_Sq_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Sq_Stim.frameNStart = frameN  # exact frame index
                R_Sq_Stim.tStart = t  # local t and not account for scr refresh
                R_Sq_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Sq_Stim, 'tStartRefresh')  # time at next scr refresh
                R_Sq_Stim.setAutoDraw(True)
            if R_Sq_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Sq_Stim.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Sq_Stim.tStop = t  # not accounting for scr refresh
                    R_Sq_Stim.frameNStop = frameN  # exact frame index
                    R_Sq_Stim.setAutoDraw(False)
            
            # *Encoding_Resp* updates
            waitOnFlip = False
            if Encoding_Resp.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Encoding_Resp.frameNStart = frameN  # exact frame index
                Encoding_Resp.tStart = t  # local t and not account for scr refresh
                Encoding_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Encoding_Resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Encoding_Resp.started')
                Encoding_Resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Encoding_Resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Encoding_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Encoding_Resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Encoding_Resp.tStartRefresh + 3.7-frameTolerance:
                    # keep track of stop time/frame for later
                    Encoding_Resp.tStop = t  # not accounting for scr refresh
                    Encoding_Resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Encoding_Resp.stopped')
                    Encoding_Resp.status = FINISHED
            if Encoding_Resp.status == STARTED and not waitOnFlip:
                theseKeys = Encoding_Resp.getKeys(keyList=['q','p'], waitRelease=False)
                _Encoding_Resp_allKeys.extend(theseKeys)
                if len(_Encoding_Resp_allKeys):
                    Encoding_Resp.keys = _Encoding_Resp_allKeys[-1].name  # just the last key pressed
                    Encoding_Resp.rt = _Encoding_Resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *L_Scene_Stim* updates
            if L_Scene_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                L_Scene_Stim.frameNStart = frameN  # exact frame index
                L_Scene_Stim.tStart = t  # local t and not account for scr refresh
                L_Scene_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(L_Scene_Stim, 'tStartRefresh')  # time at next scr refresh
                L_Scene_Stim.setAutoDraw(True)
            if L_Scene_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > L_Scene_Stim.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    L_Scene_Stim.tStop = t  # not accounting for scr refresh
                    L_Scene_Stim.frameNStop = frameN  # exact frame index
                    L_Scene_Stim.setAutoDraw(False)
            
            # *R_Scene_Stim* updates
            if R_Scene_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                R_Scene_Stim.frameNStart = frameN  # exact frame index
                R_Scene_Stim.tStart = t  # local t and not account for scr refresh
                R_Scene_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(R_Scene_Stim, 'tStartRefresh')  # time at next scr refresh
                R_Scene_Stim.setAutoDraw(True)
            if R_Scene_Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > R_Scene_Stim.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    R_Scene_Stim.tStop = t  # not accounting for scr refresh
                    R_Scene_Stim.frameNStop = frameN  # exact frame index
                    R_Scene_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EncodingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encoding" ---
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Encoding_Resp.keys in ['', [], None]:  # No response was made
            Encoding_Resp.keys = None
        EncStim_Loop.addData('Encoding_Resp.keys',Encoding_Resp.keys)
        if Encoding_Resp.keys != None:  # we had a response
            EncStim_Loop.addData('Encoding_Resp.rt', Encoding_Resp.rt)
        # Run 'End Routine' code from Key_Tracking_Code
        if Encoding_Resp.keys == 'q':
            Choice_List.append('L')
        else:
            Choice_List.append('R')
        Loop_Count += 1
        if Loop_Count >= 12:
            Attn = 1
            Loop_Count = 0
        Enc_Loop_Count += 1
        if Enc_Loop_Count >= 24:
            Brk_Enc = 1
            Enc_Loop_Count = 0
            ProT += 1
        PrcLoop_Count += 1
        if PrcLoop_Count >= 5:
            PrcAttn = 1
            PrcLoop_Count = 0
        PrcEnc_Loop_Count += 1
        if PrcEnc_Loop_Count >= 10:
            PrcBrk_Enc = 1
            PrcEnc_Loop_Count = 0
        if not Encoding_Resp.keys:
            Resp_Fail = 1
            FB = 0
        ProTracker = "Picture"+str(ProT)+".png"
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # set up handler to look after randomisation of conditions etc
        Response_Fail_Loop = data.TrialHandler(nReps=Resp_Fail, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Response_Fail_Loop')
        thisExp.addLoop(Response_Fail_Loop)  # add the loop to the experiment
        thisResponse_Fail_Loop = Response_Fail_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisResponse_Fail_Loop.rgb)
        if thisResponse_Fail_Loop != None:
            for paramName in thisResponse_Fail_Loop:
                exec('{} = thisResponse_Fail_Loop[paramName]'.format(paramName))
        
        for thisResponse_Fail_Loop in Response_Fail_Loop:
            currentLoop = Response_Fail_Loop
            # abbreviate parameter names if possible (e.g. rgb = thisResponse_Fail_Loop.rgb)
            if thisResponse_Fail_Loop != None:
                for paramName in thisResponse_Fail_Loop:
                    exec('{} = thisResponse_Fail_Loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Response_Fail" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            Response_FailComponents = [Fail_Too_Text, Fail_Slow_Text]
            for thisComponent in Response_FailComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Response_Fail" ---
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fail_Too_Text* updates
                if Fail_Too_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fail_Too_Text.frameNStart = frameN  # exact frame index
                    Fail_Too_Text.tStart = t  # local t and not account for scr refresh
                    Fail_Too_Text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fail_Too_Text, 'tStartRefresh')  # time at next scr refresh
                    Fail_Too_Text.setAutoDraw(True)
                if Fail_Too_Text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fail_Too_Text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Fail_Too_Text.tStop = t  # not accounting for scr refresh
                        Fail_Too_Text.frameNStop = frameN  # exact frame index
                        Fail_Too_Text.setAutoDraw(False)
                
                # *Fail_Slow_Text* updates
                if Fail_Slow_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fail_Slow_Text.frameNStart = frameN  # exact frame index
                    Fail_Slow_Text.tStart = t  # local t and not account for scr refresh
                    Fail_Slow_Text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fail_Slow_Text, 'tStartRefresh')  # time at next scr refresh
                    Fail_Slow_Text.setAutoDraw(True)
                if Fail_Slow_Text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fail_Slow_Text.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Fail_Slow_Text.tStop = t  # not accounting for scr refresh
                        Fail_Slow_Text.frameNStop = frameN  # exact frame index
                        Fail_Slow_Text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Response_FailComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Response_Fail" ---
            for thisComponent in Response_FailComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
        # completed Resp_Fail repeats of 'Response_Fail_Loop'
        
        
        # set up handler to look after randomisation of conditions etc
        FB_Loop = data.TrialHandler(nReps=FB, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='FB_Loop')
        thisExp.addLoop(FB_Loop)  # add the loop to the experiment
        thisFB_Loop = FB_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFB_Loop.rgb)
        if thisFB_Loop != None:
            for paramName in thisFB_Loop:
                exec('{} = thisFB_Loop[paramName]'.format(paramName))
        
        for thisFB_Loop in FB_Loop:
            currentLoop = FB_Loop
            # abbreviate parameter names if possible (e.g. rgb = thisFB_Loop.rgb)
            if thisFB_Loop != None:
                for paramName in thisFB_Loop:
                    exec('{} = thisFB_Loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Border_code
            if Encoding_Resp.keys:
                if Encoding_Resp.keys[-1] == 'q':
                    L_Sq_FB_Stim.lineColor=[1.0000, -1.0000, -1.0000]
                    R_Scene_FB_Stim.opacity=0
                    R_Point_Mask.opacity=1
                    R_Sq_FB_Stim.opacity=0
                elif Encoding_Resp.keys[-1]  == 'p':
                    R_Sq_FB_Stim.lineColor=[1.0000, -1.0000, -1.0000]
                    L_Scene_FB_Stim.opacity=0
                    L_Point_Mask.opacity=1
                    L_Sq_FB_Stim.opacity=0
            R_Scene_FB_Stim.setImage(R_Scene)
            L_Scene_FB_Stim.setImage(L_Scene)
            L_Point_FB_Stim.setText(Points_L)
            R_Point_FB_Stim.setText(Points_R)
            # keep track of which components have finished
            FeedbackComponents = [R_Sq_FB_Stim, L_Sq_FB_Stim, R_Scene_FB_Stim, L_Scene_FB_Stim, L_Point_FB_Stim, R_Point_FB_Stim, L_Point_Mask, R_Point_Mask]
            for thisComponent in FeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Feedback" ---
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *R_Sq_FB_Stim* updates
                if R_Sq_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    R_Sq_FB_Stim.frameNStart = frameN  # exact frame index
                    R_Sq_FB_Stim.tStart = t  # local t and not account for scr refresh
                    R_Sq_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(R_Sq_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    R_Sq_FB_Stim.setAutoDraw(True)
                if R_Sq_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > R_Sq_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        R_Sq_FB_Stim.tStop = t  # not accounting for scr refresh
                        R_Sq_FB_Stim.frameNStop = frameN  # exact frame index
                        R_Sq_FB_Stim.setAutoDraw(False)
                
                # *L_Sq_FB_Stim* updates
                if L_Sq_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    L_Sq_FB_Stim.frameNStart = frameN  # exact frame index
                    L_Sq_FB_Stim.tStart = t  # local t and not account for scr refresh
                    L_Sq_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(L_Sq_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    L_Sq_FB_Stim.setAutoDraw(True)
                if L_Sq_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > L_Sq_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        L_Sq_FB_Stim.tStop = t  # not accounting for scr refresh
                        L_Sq_FB_Stim.frameNStop = frameN  # exact frame index
                        L_Sq_FB_Stim.setAutoDraw(False)
                
                # *R_Scene_FB_Stim* updates
                if R_Scene_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    R_Scene_FB_Stim.frameNStart = frameN  # exact frame index
                    R_Scene_FB_Stim.tStart = t  # local t and not account for scr refresh
                    R_Scene_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(R_Scene_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    R_Scene_FB_Stim.setAutoDraw(True)
                if R_Scene_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > R_Scene_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        R_Scene_FB_Stim.tStop = t  # not accounting for scr refresh
                        R_Scene_FB_Stim.frameNStop = frameN  # exact frame index
                        R_Scene_FB_Stim.setAutoDraw(False)
                
                # *L_Scene_FB_Stim* updates
                if L_Scene_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    L_Scene_FB_Stim.frameNStart = frameN  # exact frame index
                    L_Scene_FB_Stim.tStart = t  # local t and not account for scr refresh
                    L_Scene_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(L_Scene_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    L_Scene_FB_Stim.setAutoDraw(True)
                if L_Scene_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > L_Scene_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        L_Scene_FB_Stim.tStop = t  # not accounting for scr refresh
                        L_Scene_FB_Stim.frameNStop = frameN  # exact frame index
                        L_Scene_FB_Stim.setAutoDraw(False)
                
                # *L_Point_FB_Stim* updates
                if L_Point_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    L_Point_FB_Stim.frameNStart = frameN  # exact frame index
                    L_Point_FB_Stim.tStart = t  # local t and not account for scr refresh
                    L_Point_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(L_Point_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    L_Point_FB_Stim.setAutoDraw(True)
                if L_Point_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > L_Point_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        L_Point_FB_Stim.tStop = t  # not accounting for scr refresh
                        L_Point_FB_Stim.frameNStop = frameN  # exact frame index
                        L_Point_FB_Stim.setAutoDraw(False)
                
                # *R_Point_FB_Stim* updates
                if R_Point_FB_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    R_Point_FB_Stim.frameNStart = frameN  # exact frame index
                    R_Point_FB_Stim.tStart = t  # local t and not account for scr refresh
                    R_Point_FB_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(R_Point_FB_Stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'R_Point_FB_Stim.started')
                    R_Point_FB_Stim.setAutoDraw(True)
                if R_Point_FB_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > R_Point_FB_Stim.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        R_Point_FB_Stim.tStop = t  # not accounting for scr refresh
                        R_Point_FB_Stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'R_Point_FB_Stim.stopped')
                        R_Point_FB_Stim.setAutoDraw(False)
                
                # *L_Point_Mask* updates
                if L_Point_Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    L_Point_Mask.frameNStart = frameN  # exact frame index
                    L_Point_Mask.tStart = t  # local t and not account for scr refresh
                    L_Point_Mask.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(L_Point_Mask, 'tStartRefresh')  # time at next scr refresh
                    L_Point_Mask.setAutoDraw(True)
                if L_Point_Mask.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > L_Point_Mask.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        L_Point_Mask.tStop = t  # not accounting for scr refresh
                        L_Point_Mask.frameNStop = frameN  # exact frame index
                        L_Point_Mask.setAutoDraw(False)
                
                # *R_Point_Mask* updates
                if R_Point_Mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    R_Point_Mask.frameNStart = frameN  # exact frame index
                    R_Point_Mask.tStart = t  # local t and not account for scr refresh
                    R_Point_Mask.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(R_Point_Mask, 'tStartRefresh')  # time at next scr refresh
                    R_Point_Mask.setAutoDraw(True)
                if R_Point_Mask.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > R_Point_Mask.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        R_Point_Mask.tStop = t  # not accounting for scr refresh
                        R_Point_Mask.frameNStop = frameN  # exact frame index
                        R_Point_Mask.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Feedback" ---
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from Border_code
            R_Scene_FB_Stim.opacity=1.0
            R_Point_Mask.opacity=0
            L_Scene_FB_Stim.opacity=1.0
            L_Point_Mask.opacity=0
            L_Sq_FB_Stim.opacity=1
            R_Sq_FB_Stim.opacity=1
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
        # completed FB repeats of 'FB_Loop'
        
        
        # set up handler to look after randomisation of conditions etc
        Attention_Loop = data.TrialHandler(nReps=Attn, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Attention_Loop')
        thisExp.addLoop(Attention_Loop)  # add the loop to the experiment
        thisAttention_Loop = Attention_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAttention_Loop.rgb)
        if thisAttention_Loop != None:
            for paramName in thisAttention_Loop:
                exec('{} = thisAttention_Loop[paramName]'.format(paramName))
        
        for thisAttention_Loop in Attention_Loop:
            currentLoop = Attention_Loop
            # abbreviate parameter names if possible (e.g. rgb = thisAttention_Loop.rgb)
            if thisAttention_Loop != None:
                for paramName in thisAttention_Loop:
                    exec('{} = thisAttention_Loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Attention" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Attn_Stim.setImage('AttnSlide.png')
            Attn_resp.keys = []
            Attn_resp.rt = []
            _Attn_resp_allKeys = []
            # keep track of which components have finished
            AttentionComponents = [Attn_Stim, Attn_resp]
            for thisComponent in AttentionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Attention" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Attn_Stim* updates
                if Attn_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Attn_Stim.frameNStart = frameN  # exact frame index
                    Attn_Stim.tStart = t  # local t and not account for scr refresh
                    Attn_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Attn_Stim, 'tStartRefresh')  # time at next scr refresh
                    Attn_Stim.setAutoDraw(True)
                
                # *Attn_resp* updates
                waitOnFlip = False
                if Attn_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Attn_resp.frameNStart = frameN  # exact frame index
                    Attn_resp.tStart = t  # local t and not account for scr refresh
                    Attn_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Attn_resp, 'tStartRefresh')  # time at next scr refresh
                    Attn_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Attn_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Attn_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Attn_resp.status == STARTED and not waitOnFlip:
                    theseKeys = Attn_resp.getKeys(keyList=['0', '1', '2', '3', '4', '5'], waitRelease=False)
                    _Attn_resp_allKeys.extend(theseKeys)
                    if len(_Attn_resp_allKeys):
                        Attn_resp.keys = _Attn_resp_allKeys[-1].name  # just the last key pressed
                        Attn_resp.rt = _Attn_resp_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AttentionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Attention" ---
            for thisComponent in AttentionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if Attn_resp.keys in ['', [], None]:  # No response was made
                Attn_resp.keys = None
            Attention_Loop.addData('Attn_resp.keys',Attn_resp.keys)
            if Attn_resp.keys != None:  # we had a response
                Attention_Loop.addData('Attn_resp.rt', Attn_resp.rt)
            # the Routine "Attention" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Attn repeats of 'Attention_Loop'
        
        
        # set up handler to look after randomisation of conditions etc
        EncBrk_Loop = data.TrialHandler(nReps=Brk_Enc, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='EncBrk_Loop')
        thisExp.addLoop(EncBrk_Loop)  # add the loop to the experiment
        thisEncBrk_Loop = EncBrk_Loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEncBrk_Loop.rgb)
        if thisEncBrk_Loop != None:
            for paramName in thisEncBrk_Loop:
                exec('{} = thisEncBrk_Loop[paramName]'.format(paramName))
        
        for thisEncBrk_Loop in EncBrk_Loop:
            currentLoop = EncBrk_Loop
            # abbreviate parameter names if possible (e.g. rgb = thisEncBrk_Loop.rgb)
            if thisEncBrk_Loop != None:
                for paramName in thisEncBrk_Loop:
                    exec('{} = thisEncBrk_Loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            ITIComponents = [ITI_Stim]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ITI_Stim* updates
                if ITI_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_Stim.frameNStart = frameN  # exact frame index
                    ITI_Stim.tStart = t  # local t and not account for scr refresh
                    ITI_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
                    ITI_Stim.setAutoDraw(True)
                if ITI_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI_Stim.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI_Stim.tStop = t  # not accounting for scr refresh
                        ITI_Stim.frameNStop = frameN  # exact frame index
                        ITI_Stim.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "Coins" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            Coin_Animation.setOpacity(1.0)
            Coin_Animation.setContrast(None)
            Coin_Animation.setMovie('coin.mp4')
            # keep track of which components have finished
            CoinsComponents = [Coin_Animation]
            for thisComponent in CoinsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Coins" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Coin_Animation* updates
                if Coin_Animation.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    Coin_Animation.frameNStart = frameN  # exact frame index
                    Coin_Animation.tStart = t  # local t and not account for scr refresh
                    Coin_Animation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Coin_Animation, 'tStartRefresh')  # time at next scr refresh
                    Coin_Animation.setAutoDraw(True)
                    Coin_Animation.play()
                if Coin_Animation.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in CoinsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Coins" ---
            for thisComponent in CoinsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Coin_Animation.stop()
            # the Routine "Coins" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Encoding_Break" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            EncBrk_Resp.keys = []
            EncBrk_Resp.rt = []
            _EncBrk_Resp_allKeys = []
            Point_Report_Stim.setText(PtTotal)
            Progress_Tracker.setImage(ProTracker)
            # keep track of which components have finished
            Encoding_BreakComponents = [EncBrk_Prompt, Cont_Enc_Stim, EncBrk_Warning_Prompt, Cont_EncBrk_Prompt, EncBrk_Resp, Point_Report_Prompt, Point_Report_Stim, Progress_Tracker, Perc_stim]
            for thisComponent in Encoding_BreakComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Encoding_Break" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *EncBrk_Prompt* updates
                if EncBrk_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    EncBrk_Prompt.frameNStart = frameN  # exact frame index
                    EncBrk_Prompt.tStart = t  # local t and not account for scr refresh
                    EncBrk_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EncBrk_Prompt, 'tStartRefresh')  # time at next scr refresh
                    EncBrk_Prompt.setAutoDraw(True)
                if EncBrk_Prompt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > EncBrk_Prompt.tStartRefresh + 20-frameTolerance:
                        # keep track of stop time/frame for later
                        EncBrk_Prompt.tStop = t  # not accounting for scr refresh
                        EncBrk_Prompt.frameNStop = frameN  # exact frame index
                        EncBrk_Prompt.setAutoDraw(False)
                
                # *Cont_Enc_Stim* updates
                if Cont_Enc_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Cont_Enc_Stim.frameNStart = frameN  # exact frame index
                    Cont_Enc_Stim.tStart = t  # local t and not account for scr refresh
                    Cont_Enc_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cont_Enc_Stim, 'tStartRefresh')  # time at next scr refresh
                    Cont_Enc_Stim.setAutoDraw(True)
                
                # *EncBrk_Warning_Prompt* updates
                if EncBrk_Warning_Prompt.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
                    # keep track of start time/frame for later
                    EncBrk_Warning_Prompt.frameNStart = frameN  # exact frame index
                    EncBrk_Warning_Prompt.tStart = t  # local t and not account for scr refresh
                    EncBrk_Warning_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EncBrk_Warning_Prompt, 'tStartRefresh')  # time at next scr refresh
                    EncBrk_Warning_Prompt.setAutoDraw(True)
                if EncBrk_Warning_Prompt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > EncBrk_Warning_Prompt.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        EncBrk_Warning_Prompt.tStop = t  # not accounting for scr refresh
                        EncBrk_Warning_Prompt.frameNStop = frameN  # exact frame index
                        EncBrk_Warning_Prompt.setAutoDraw(False)
                
                # *Cont_EncBrk_Prompt* updates
                if Cont_EncBrk_Prompt.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
                    # keep track of start time/frame for later
                    Cont_EncBrk_Prompt.frameNStart = frameN  # exact frame index
                    Cont_EncBrk_Prompt.tStart = t  # local t and not account for scr refresh
                    Cont_EncBrk_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cont_EncBrk_Prompt, 'tStartRefresh')  # time at next scr refresh
                    Cont_EncBrk_Prompt.setAutoDraw(True)
                
                # *EncBrk_Resp* updates
                waitOnFlip = False
                if EncBrk_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    EncBrk_Resp.frameNStart = frameN  # exact frame index
                    EncBrk_Resp.tStart = t  # local t and not account for scr refresh
                    EncBrk_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EncBrk_Resp, 'tStartRefresh')  # time at next scr refresh
                    EncBrk_Resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(EncBrk_Resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(EncBrk_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if EncBrk_Resp.status == STARTED and not waitOnFlip:
                    theseKeys = EncBrk_Resp.getKeys(keyList=['space'], waitRelease=False)
                    _EncBrk_Resp_allKeys.extend(theseKeys)
                    if len(_EncBrk_Resp_allKeys):
                        EncBrk_Resp.keys = _EncBrk_Resp_allKeys[-1].name  # just the last key pressed
                        EncBrk_Resp.rt = _EncBrk_Resp_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *Point_Report_Prompt* updates
                if Point_Report_Prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Point_Report_Prompt.frameNStart = frameN  # exact frame index
                    Point_Report_Prompt.tStart = t  # local t and not account for scr refresh
                    Point_Report_Prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Point_Report_Prompt, 'tStartRefresh')  # time at next scr refresh
                    Point_Report_Prompt.setAutoDraw(True)
                if Point_Report_Prompt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Point_Report_Prompt.tStartRefresh + 20-frameTolerance:
                        # keep track of stop time/frame for later
                        Point_Report_Prompt.tStop = t  # not accounting for scr refresh
                        Point_Report_Prompt.frameNStop = frameN  # exact frame index
                        Point_Report_Prompt.setAutoDraw(False)
                
                # *Point_Report_Stim* updates
                if Point_Report_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Point_Report_Stim.frameNStart = frameN  # exact frame index
                    Point_Report_Stim.tStart = t  # local t and not account for scr refresh
                    Point_Report_Stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Point_Report_Stim, 'tStartRefresh')  # time at next scr refresh
                    Point_Report_Stim.setAutoDraw(True)
                if Point_Report_Stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Point_Report_Stim.tStartRefresh + 20-frameTolerance:
                        # keep track of stop time/frame for later
                        Point_Report_Stim.tStop = t  # not accounting for scr refresh
                        Point_Report_Stim.frameNStop = frameN  # exact frame index
                        Point_Report_Stim.setAutoDraw(False)
                
                # *Progress_Tracker* updates
                if Progress_Tracker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Progress_Tracker.frameNStart = frameN  # exact frame index
                    Progress_Tracker.tStart = t  # local t and not account for scr refresh
                    Progress_Tracker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Progress_Tracker, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Progress_Tracker.started')
                    Progress_Tracker.setAutoDraw(True)
                
                # *Perc_stim* updates
                if Perc_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Perc_stim.frameNStart = frameN  # exact frame index
                    Perc_stim.tStart = t  # local t and not account for scr refresh
                    Perc_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Perc_stim, 'tStartRefresh')  # time at next scr refresh
                    Perc_stim.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Encoding_BreakComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Encoding_Break" ---
            for thisComponent in Encoding_BreakComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if EncBrk_Resp.keys in ['', [], None]:  # No response was made
                EncBrk_Resp.keys = None
            EncBrk_Loop.addData('EncBrk_Resp.keys',EncBrk_Resp.keys)
            if EncBrk_Resp.keys != None:  # we had a response
                EncBrk_Loop.addData('EncBrk_Resp.rt', EncBrk_Resp.rt)
            # the Routine "Encoding_Break" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Brk_Enc repeats of 'EncBrk_Loop'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'EncStim_Loop'
    
# completed 1.0 repeats of 'Encoding_Loop'


# --- Prepare to start Routine "Reward_Reveal" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Reward_RevealComponents = [Reward_Stim, Bonus_Cash]
for thisComponent in Reward_RevealComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Reward_Reveal" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Reward_Stim* updates
    if Reward_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Reward_Stim.frameNStart = frameN  # exact frame index
        Reward_Stim.tStart = t  # local t and not account for scr refresh
        Reward_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Reward_Stim, 'tStartRefresh')  # time at next scr refresh
        Reward_Stim.setAutoDraw(True)
    if Reward_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Reward_Stim.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Reward_Stim.tStop = t  # not accounting for scr refresh
            Reward_Stim.frameNStop = frameN  # exact frame index
            Reward_Stim.setAutoDraw(False)
    
    # *Bonus_Cash* updates
    if Bonus_Cash.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Bonus_Cash.frameNStart = frameN  # exact frame index
        Bonus_Cash.tStart = t  # local t and not account for scr refresh
        Bonus_Cash.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Bonus_Cash, 'tStartRefresh')  # time at next scr refresh
        Bonus_Cash.setAutoDraw(True)
    if Bonus_Cash.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Bonus_Cash.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Bonus_Cash.tStop = t  # not accounting for scr refresh
            Bonus_Cash.frameNStop = frameN  # exact frame index
            Bonus_Cash.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Reward_RevealComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Reward_Reveal" ---
for thisComponent in Reward_RevealComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Experiment_End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Experiment_EndComponents = [Experiment_End_Stim]
for thisComponent in Experiment_EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Experiment_End" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Experiment_End_Stim* updates
    if Experiment_End_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Experiment_End_Stim.frameNStart = frameN  # exact frame index
        Experiment_End_Stim.tStart = t  # local t and not account for scr refresh
        Experiment_End_Stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Experiment_End_Stim, 'tStartRefresh')  # time at next scr refresh
        Experiment_End_Stim.setAutoDraw(True)
    if Experiment_End_Stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Experiment_End_Stim.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Experiment_End_Stim.tStop = t  # not accounting for scr refresh
            Experiment_End_Stim.frameNStop = frameN  # exact frame index
            Experiment_End_Stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Experiment_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Experiment_End" ---
for thisComponent in Experiment_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
