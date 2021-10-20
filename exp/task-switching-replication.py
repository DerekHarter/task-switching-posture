#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed 20 Oct 2021 02:14:33 PM CDT
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'task-switching-replication'  # from the Builder filename that created this script
expInfo = {'participant': '1000', 'session': '001', 'condition': '7'}
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
    originPath='/home/dash/cognitive-control-posture/exp/task-switching-replication.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='degFlatPos')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions01"
practiceUntimedInstructions01Clock = core.Clock()
# set up instruction and experiment image file names for loading
condition = expInfo['condition']
untimed01InstructionImage = 'instructions/cond-%02d-untimed-01.png' % (int(condition))
untimed02InstructionImage = 'instructions/cond-%02d-untimed-02.png' % (int(condition))
untimed03InstructionImage = 'instructions/cond-%02d-untimed-03.png' % (int(condition))
untimed04InstructionImage = 'instructions/cond-%02d-untimed-04.png' % (int(condition))
untimed05InstructionImage = 'instructions/cond-%02d-untimed-05.png' % (int(condition))
untimed06InstructionImage = 'instructions/cond-%02d-untimed-06.png' % (int(condition))
untimed07InstructionImage = 'instructions/cond-%02d-untimed-07.png' % (int(condition))
untimed08InstructionImage = 'instructions/cond-%02d-untimed-08.png' % (int(condition))

timed01InstructionImage = 'instructions/cond-%02d-timed-01.png' % (int(condition))
timed02InstructionImage = 'instructions/cond-%02d-timed-02.png' % (int(condition))

experiment01InstructionImage = 'instructions/cond-%02d-experiment-01.png' % (int(condition))

errorDashedImage = 'instructions/cond-%02d-error-dashed.png' % (int(condition))
errorSolidImage = 'instructions/cond-%02d-error-solid.png' % (int(condition))

# experimental condition variables
posture = 'standing'
cueSolid = 'shape'
cueDashed = 'color'
colorLeft = 'yellow'
colorRight = 'blue'
shapeLeft = 'triangle'
shapeRight = 'square'
practiceUntimedInstruction01Text = visual.ImageStim(
    win=win,
    name='practiceUntimedInstruction01Text', 
    image=untimed01InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
practiceUntimedInstructions01KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions02"
practiceUntimedInstructions02Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image=untimed02InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimed02KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions03"
practiceUntimedInstructions03Clock = core.Clock()
practiceUntimedInstructions03Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions03Image', 
    image=untimed03InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions03KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions04"
practiceUntimedInstructions04Clock = core.Clock()
practiceUntimedInstructions04Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions04Image', 
    image=untimed04InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions04KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions05"
practiceUntimedInstructions05Clock = core.Clock()
practiceUntimedInstructions05Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions05Image', 
    image=untimed05InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions05KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions06"
practiceUntimedInstructions06Clock = core.Clock()
practiceUntimedInstructions06Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions06Image', 
    image=untimed06InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions06KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions07"
practiceUntimedInstructions07Clock = core.Clock()
practiceUntimedInstructions07Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions07Image', 
    image=untimed07InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions07KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedInstructions08"
practiceUntimedInstructions08Clock = core.Clock()
practiceUntimedInstructions08Image = visual.ImageStim(
    win=win,
    name='practiceUntimedInstructions08Image', 
    image=untimed08InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedInstructions08KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedTrial"
practiceUntimedTrialClock = core.Clock()
practiceUntimedTaskCueImage = visual.ImageStim(
    win=win,
    name='practiceUntimedTaskCueImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(10.0, 10.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceUntimedTaskTargetImage = visual.ImageStim(
    win=win,
    name='practiceUntimedTaskTargetImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(5.0, 5.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
practiceUntimedTaskResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceUntimedFeedbackSelect_2"
practiceUntimedFeedbackSelect_2Clock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "practiceCorrectFeedback"
practiceCorrectFeedbackClock = core.Clock()
practiceTimedFeedbackMessageCorrect = visual.TextStim(win=win, name='practiceTimedFeedbackMessageCorrect',
    text='That was correct!',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceIncorrectSolidFeedback"
practiceIncorrectSolidFeedbackClock = core.Clock()
feedbackSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='feedbackSound')
feedbackSound.setVolume(1.0)
feedbackSolidIncorrectImage = visual.ImageStim(
    win=win,
    name='feedbackSolidIncorrectImage', 
    image=errorSolidImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceIncorrectDashFeedback"
practiceIncorrectDashFeedbackClock = core.Clock()
practiceIncorrectDashedSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='practiceIncorrectDashedSound')
practiceIncorrectDashedSound.setVolume(1.0)
practiceIncorrectDashedFeedbackImage = visual.ImageStim(
    win=win,
    name='practiceIncorrectDashedFeedbackImage', 
    image=errorDashedImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceDelay"
practiceDelayClock = core.Clock()
delayText = visual.TextStim(win=win, name='delayText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceTimedInstructions01"
practiceTimedInstructions01Clock = core.Clock()
practiceTimedInstructions01Image = visual.ImageStim(
    win=win,
    name='practiceTimedInstructions01Image', 
    image=timed01InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceTimedInstructions01KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceTimedInstructions02"
practiceTimedInstructions02Clock = core.Clock()
practiceTimedInstructions02Image = visual.ImageStim(
    win=win,
    name='practiceTimedInstructions02Image', 
    image=timed02InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceTimedInstructions02KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceTimedTrial"
practiceTimedTrialClock = core.Clock()
practiceTimedTaskCueImage = visual.ImageStim(
    win=win,
    name='practiceTimedTaskCueImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(10.0, 10.0),
    color=None, colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practiceTimedTaskTargetImage = visual.ImageStim(
    win=win,
    name='practiceTimedTaskTargetImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(5.0, 5.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
practiceTimedTaskResponse = keyboard.Keyboard()

# Initialize components for Routine "practiceTimedFeedbackSelect"
practiceTimedFeedbackSelectClock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "practiceCorrectFeedback"
practiceCorrectFeedbackClock = core.Clock()
practiceTimedFeedbackMessageCorrect = visual.TextStim(win=win, name='practiceTimedFeedbackMessageCorrect',
    text='That was correct!',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceIncorrectSolidFeedback"
practiceIncorrectSolidFeedbackClock = core.Clock()
feedbackSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='feedbackSound')
feedbackSound.setVolume(1.0)
feedbackSolidIncorrectImage = visual.ImageStim(
    win=win,
    name='feedbackSolidIncorrectImage', 
    image=errorSolidImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceIncorrectDashFeedback"
practiceIncorrectDashFeedbackClock = core.Clock()
practiceIncorrectDashedSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='practiceIncorrectDashedSound')
practiceIncorrectDashedSound.setVolume(1.0)
practiceIncorrectDashedFeedbackImage = visual.ImageStim(
    win=win,
    name='practiceIncorrectDashedFeedbackImage', 
    image=errorDashedImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "practiceDelay"
practiceDelayClock = core.Clock()
delayText = visual.TextStim(win=win, name='delayText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "experimentInstructions01"
experimentInstructions01Clock = core.Clock()
experimentInstructions01Image = visual.ImageStim(
    win=win,
    name='experimentInstructions01Image', 
    image=experiment01InstructionImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
experimentInstructions01KeyResponse = keyboard.Keyboard()

# Initialize components for Routine "experimentTimedTrial"
experimentTimedTrialClock = core.Clock()
expCueImage = visual.ImageStim(
    win=win,
    name='expCueImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(10.0, 10.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
expTargetImage = visual.ImageStim(
    win=win,
    name='expTargetImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(5.0, 5.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
expResponse = keyboard.Keyboard()

# Initialize components for Routine "experimentFeedbackSelect"
experimentFeedbackSelectClock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "experimentIncorrectSolidFeedback"
experimentIncorrectSolidFeedbackClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image=errorSolidImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "experimentIncorrectDashedFeedback"
experimentIncorrectDashedFeedbackClock = core.Clock()
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image=errorDashedImage, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "experimentDelay"
experimentDelayClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practiceUntimedInstructions01"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions01KeyResponse.keys = []
practiceUntimedInstructions01KeyResponse.rt = []
_practiceUntimedInstructions01KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions01Components = [practiceUntimedInstruction01Text, practiceUntimedInstructions01KeyResponse]
for thisComponent in practiceUntimedInstructions01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions01"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstruction01Text* updates
    if practiceUntimedInstruction01Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstruction01Text.frameNStart = frameN  # exact frame index
        practiceUntimedInstruction01Text.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstruction01Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstruction01Text, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstruction01Text.setAutoDraw(True)
    
    # *practiceUntimedInstructions01KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions01KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions01KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions01KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions01KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions01KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions01KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions01KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions01KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions01KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions01KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceUntimedInstructions01KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions01KeyResponse_allKeys):
            practiceUntimedInstructions01KeyResponse.keys = _practiceUntimedInstructions01KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions01KeyResponse.rt = _practiceUntimedInstructions01KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions01"-------
for thisComponent in practiceUntimedInstructions01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstruction01Text.started', practiceUntimedInstruction01Text.tStartRefresh)
thisExp.addData('practiceUntimedInstruction01Text.stopped', practiceUntimedInstruction01Text.tStopRefresh)
# check responses
if practiceUntimedInstructions01KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions01KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions01KeyResponse.keys',practiceUntimedInstructions01KeyResponse.keys)
if practiceUntimedInstructions01KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions01KeyResponse.rt', practiceUntimedInstructions01KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions01KeyResponse.started', practiceUntimedInstructions01KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions01KeyResponse.stopped', practiceUntimedInstructions01KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions02"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimed02KeyResponse.keys = []
practiceUntimed02KeyResponse.rt = []
_practiceUntimed02KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions02Components = [image, practiceUntimed02KeyResponse]
for thisComponent in practiceUntimedInstructions02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions02"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *practiceUntimed02KeyResponse* updates
    waitOnFlip = False
    if practiceUntimed02KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimed02KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimed02KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimed02KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimed02KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimed02KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimed02KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimed02KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimed02KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimed02KeyResponse.getKeys(keyList=['1'], waitRelease=False)
        _practiceUntimed02KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimed02KeyResponse_allKeys):
            practiceUntimed02KeyResponse.keys = _practiceUntimed02KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimed02KeyResponse.rt = _practiceUntimed02KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions02"-------
for thisComponent in practiceUntimedInstructions02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if practiceUntimed02KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimed02KeyResponse.keys = None
thisExp.addData('practiceUntimed02KeyResponse.keys',practiceUntimed02KeyResponse.keys)
if practiceUntimed02KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimed02KeyResponse.rt', practiceUntimed02KeyResponse.rt)
thisExp.addData('practiceUntimed02KeyResponse.started', practiceUntimed02KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimed02KeyResponse.stopped', practiceUntimed02KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions03"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions03KeyResponse.keys = []
practiceUntimedInstructions03KeyResponse.rt = []
_practiceUntimedInstructions03KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions03Components = [practiceUntimedInstructions03Image, practiceUntimedInstructions03KeyResponse]
for thisComponent in practiceUntimedInstructions03Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions03Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions03"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions03Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions03Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions03Image* updates
    if practiceUntimedInstructions03Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions03Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions03Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions03Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions03Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions03Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions03KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions03KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions03KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions03KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions03KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions03KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions03KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions03KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions03KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions03KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions03KeyResponse.getKeys(keyList=['2'], waitRelease=False)
        _practiceUntimedInstructions03KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions03KeyResponse_allKeys):
            practiceUntimedInstructions03KeyResponse.keys = _practiceUntimedInstructions03KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions03KeyResponse.rt = _practiceUntimedInstructions03KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions03"-------
for thisComponent in practiceUntimedInstructions03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions03Image.started', practiceUntimedInstructions03Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions03Image.stopped', practiceUntimedInstructions03Image.tStopRefresh)
# check responses
if practiceUntimedInstructions03KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions03KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions03KeyResponse.keys',practiceUntimedInstructions03KeyResponse.keys)
if practiceUntimedInstructions03KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions03KeyResponse.rt', practiceUntimedInstructions03KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions03KeyResponse.started', practiceUntimedInstructions03KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions03KeyResponse.stopped', practiceUntimedInstructions03KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions04"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions04KeyResponse.keys = []
practiceUntimedInstructions04KeyResponse.rt = []
_practiceUntimedInstructions04KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions04Components = [practiceUntimedInstructions04Image, practiceUntimedInstructions04KeyResponse]
for thisComponent in practiceUntimedInstructions04Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions04Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions04"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions04Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions04Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions04Image* updates
    if practiceUntimedInstructions04Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions04Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions04Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions04Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions04Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions04Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions04KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions04KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions04KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions04KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions04KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions04KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions04KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions04KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions04KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions04KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions04KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceUntimedInstructions04KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions04KeyResponse_allKeys):
            practiceUntimedInstructions04KeyResponse.keys = _practiceUntimedInstructions04KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions04KeyResponse.rt = _practiceUntimedInstructions04KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions04Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions04"-------
for thisComponent in practiceUntimedInstructions04Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions04Image.started', practiceUntimedInstructions04Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions04Image.stopped', practiceUntimedInstructions04Image.tStopRefresh)
# check responses
if practiceUntimedInstructions04KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions04KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions04KeyResponse.keys',practiceUntimedInstructions04KeyResponse.keys)
if practiceUntimedInstructions04KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions04KeyResponse.rt', practiceUntimedInstructions04KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions04KeyResponse.started', practiceUntimedInstructions04KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions04KeyResponse.stopped', practiceUntimedInstructions04KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions04" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions05"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions05KeyResponse.keys = []
practiceUntimedInstructions05KeyResponse.rt = []
_practiceUntimedInstructions05KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions05Components = [practiceUntimedInstructions05Image, practiceUntimedInstructions05KeyResponse]
for thisComponent in practiceUntimedInstructions05Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions05Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions05"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions05Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions05Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions05Image* updates
    if practiceUntimedInstructions05Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions05Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions05Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions05Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions05Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions05Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions05KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions05KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions05KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions05KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions05KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions05KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions05KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions05KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions05KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions05KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions05KeyResponse.getKeys(keyList=['1'], waitRelease=False)
        _practiceUntimedInstructions05KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions05KeyResponse_allKeys):
            practiceUntimedInstructions05KeyResponse.keys = _practiceUntimedInstructions05KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions05KeyResponse.rt = _practiceUntimedInstructions05KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions05Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions05"-------
for thisComponent in practiceUntimedInstructions05Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions05Image.started', practiceUntimedInstructions05Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions05Image.stopped', practiceUntimedInstructions05Image.tStopRefresh)
# check responses
if practiceUntimedInstructions05KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions05KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions05KeyResponse.keys',practiceUntimedInstructions05KeyResponse.keys)
if practiceUntimedInstructions05KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions05KeyResponse.rt', practiceUntimedInstructions05KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions05KeyResponse.started', practiceUntimedInstructions05KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions05KeyResponse.stopped', practiceUntimedInstructions05KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions05" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions06"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions06KeyResponse.keys = []
practiceUntimedInstructions06KeyResponse.rt = []
_practiceUntimedInstructions06KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions06Components = [practiceUntimedInstructions06Image, practiceUntimedInstructions06KeyResponse]
for thisComponent in practiceUntimedInstructions06Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions06Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions06"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions06Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions06Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions06Image* updates
    if practiceUntimedInstructions06Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions06Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions06Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions06Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions06Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions06Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions06KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions06KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions06KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions06KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions06KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions06KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions06KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions06KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions06KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions06KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions06KeyResponse.getKeys(keyList=['2'], waitRelease=False)
        _practiceUntimedInstructions06KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions06KeyResponse_allKeys):
            practiceUntimedInstructions06KeyResponse.keys = _practiceUntimedInstructions06KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions06KeyResponse.rt = _practiceUntimedInstructions06KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions06Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions06"-------
for thisComponent in practiceUntimedInstructions06Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions06Image.started', practiceUntimedInstructions06Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions06Image.stopped', practiceUntimedInstructions06Image.tStopRefresh)
# check responses
if practiceUntimedInstructions06KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions06KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions06KeyResponse.keys',practiceUntimedInstructions06KeyResponse.keys)
if practiceUntimedInstructions06KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions06KeyResponse.rt', practiceUntimedInstructions06KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions06KeyResponse.started', practiceUntimedInstructions06KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions06KeyResponse.stopped', practiceUntimedInstructions06KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions06" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions07"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions07KeyResponse.keys = []
practiceUntimedInstructions07KeyResponse.rt = []
_practiceUntimedInstructions07KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions07Components = [practiceUntimedInstructions07Image, practiceUntimedInstructions07KeyResponse]
for thisComponent in practiceUntimedInstructions07Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions07Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions07"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions07Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions07Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions07Image* updates
    if practiceUntimedInstructions07Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions07Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions07Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions07Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions07Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions07Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions07KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions07KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions07KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions07KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions07KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions07KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions07KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions07KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions07KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions07KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions07KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceUntimedInstructions07KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions07KeyResponse_allKeys):
            practiceUntimedInstructions07KeyResponse.keys = _practiceUntimedInstructions07KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions07KeyResponse.rt = _practiceUntimedInstructions07KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions07Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions07"-------
for thisComponent in practiceUntimedInstructions07Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions07Image.started', practiceUntimedInstructions07Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions07Image.stopped', practiceUntimedInstructions07Image.tStopRefresh)
# check responses
if practiceUntimedInstructions07KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions07KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions07KeyResponse.keys',practiceUntimedInstructions07KeyResponse.keys)
if practiceUntimedInstructions07KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions07KeyResponse.rt', practiceUntimedInstructions07KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions07KeyResponse.started', practiceUntimedInstructions07KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions07KeyResponse.stopped', practiceUntimedInstructions07KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions07" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceUntimedInstructions08"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedInstructions08KeyResponse.keys = []
practiceUntimedInstructions08KeyResponse.rt = []
_practiceUntimedInstructions08KeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructions08Components = [practiceUntimedInstructions08Image, practiceUntimedInstructions08KeyResponse]
for thisComponent in practiceUntimedInstructions08Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructions08Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions08"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructions08Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructions08Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructions08Image* updates
    if practiceUntimedInstructions08Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions08Image.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions08Image.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions08Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions08Image, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions08Image.setAutoDraw(True)
    
    # *practiceUntimedInstructions08KeyResponse* updates
    waitOnFlip = False
    if practiceUntimedInstructions08KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructions08KeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedInstructions08KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructions08KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructions08KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructions08KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedInstructions08KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedInstructions08KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedInstructions08KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedInstructions08KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceUntimedInstructions08KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedInstructions08KeyResponse_allKeys):
            practiceUntimedInstructions08KeyResponse.keys = _practiceUntimedInstructions08KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedInstructions08KeyResponse.rt = _practiceUntimedInstructions08KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructions08Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions08"-------
for thisComponent in practiceUntimedInstructions08Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructions08Image.started', practiceUntimedInstructions08Image.tStartRefresh)
thisExp.addData('practiceUntimedInstructions08Image.stopped', practiceUntimedInstructions08Image.tStopRefresh)
# check responses
if practiceUntimedInstructions08KeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedInstructions08KeyResponse.keys = None
thisExp.addData('practiceUntimedInstructions08KeyResponse.keys',practiceUntimedInstructions08KeyResponse.keys)
if practiceUntimedInstructions08KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedInstructions08KeyResponse.rt', practiceUntimedInstructions08KeyResponse.rt)
thisExp.addData('practiceUntimedInstructions08KeyResponse.started', practiceUntimedInstructions08KeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedInstructions08KeyResponse.stopped', practiceUntimedInstructions08KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions08" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceUntimedTrials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task-switching-replication-trialtypes.xlsx'),
    seed=None, name='practiceUntimedTrials')
thisExp.addLoop(practiceUntimedTrials)  # add the loop to the experiment
thisPracticeUntimedTrial = practiceUntimedTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeUntimedTrial.rgb)
if thisPracticeUntimedTrial != None:
    for paramName in thisPracticeUntimedTrial:
        exec('{} = thisPracticeUntimedTrial[paramName]'.format(paramName))

for thisPracticeUntimedTrial in practiceUntimedTrials:
    currentLoop = practiceUntimedTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeUntimedTrial.rgb)
    if thisPracticeUntimedTrial != None:
        for paramName in thisPracticeUntimedTrial:
            exec('{} = thisPracticeUntimedTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceUntimedTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    practiceUntimedTaskCueImage.setImage(cueFileName)
    practiceUntimedTaskTargetImage.setImage(targetFileName)
    practiceUntimedTaskResponse.keys = []
    practiceUntimedTaskResponse.rt = []
    _practiceUntimedTaskResponse_allKeys = []
    # keep track of which components have finished
    practiceUntimedTrialComponents = [practiceUntimedTaskCueImage, practiceUntimedTaskTargetImage, practiceUntimedTaskResponse]
    for thisComponent in practiceUntimedTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceUntimedTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceUntimedTrial"-------
    while continueRoutine:
        # get current time
        t = practiceUntimedTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceUntimedTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceUntimedTaskCueImage* updates
        if practiceUntimedTaskCueImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practiceUntimedTaskCueImage.frameNStart = frameN  # exact frame index
            practiceUntimedTaskCueImage.tStart = t  # local t and not account for scr refresh
            practiceUntimedTaskCueImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceUntimedTaskCueImage, 'tStartRefresh')  # time at next scr refresh
            practiceUntimedTaskCueImage.setAutoDraw(True)
        
        # *practiceUntimedTaskTargetImage* updates
        if practiceUntimedTaskTargetImage.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            practiceUntimedTaskTargetImage.frameNStart = frameN  # exact frame index
            practiceUntimedTaskTargetImage.tStart = t  # local t and not account for scr refresh
            practiceUntimedTaskTargetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceUntimedTaskTargetImage, 'tStartRefresh')  # time at next scr refresh
            practiceUntimedTaskTargetImage.setAutoDraw(True)
        
        # *practiceUntimedTaskResponse* updates
        waitOnFlip = False
        if practiceUntimedTaskResponse.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            practiceUntimedTaskResponse.frameNStart = frameN  # exact frame index
            practiceUntimedTaskResponse.tStart = t  # local t and not account for scr refresh
            practiceUntimedTaskResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceUntimedTaskResponse, 'tStartRefresh')  # time at next scr refresh
            practiceUntimedTaskResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practiceUntimedTaskResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practiceUntimedTaskResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practiceUntimedTaskResponse.status == STARTED and not waitOnFlip:
            theseKeys = practiceUntimedTaskResponse.getKeys(keyList=['1', '2'], waitRelease=False)
            _practiceUntimedTaskResponse_allKeys.extend(theseKeys)
            if len(_practiceUntimedTaskResponse_allKeys):
                practiceUntimedTaskResponse.keys = _practiceUntimedTaskResponse_allKeys[-1].name  # just the last key pressed
                practiceUntimedTaskResponse.rt = _practiceUntimedTaskResponse_allKeys[-1].rt
                # was this correct?
                if (practiceUntimedTaskResponse.keys == str(correctAnswer)) or (practiceUntimedTaskResponse.keys == correctAnswer):
                    practiceUntimedTaskResponse.corr = 1
                else:
                    practiceUntimedTaskResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceUntimedTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceUntimedTrial"-------
    for thisComponent in practiceUntimedTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceUntimedTrials.addData('practiceUntimedTaskCueImage.started', practiceUntimedTaskCueImage.tStartRefresh)
    practiceUntimedTrials.addData('practiceUntimedTaskCueImage.stopped', practiceUntimedTaskCueImage.tStopRefresh)
    practiceUntimedTrials.addData('practiceUntimedTaskTargetImage.started', practiceUntimedTaskTargetImage.tStartRefresh)
    practiceUntimedTrials.addData('practiceUntimedTaskTargetImage.stopped', practiceUntimedTaskTargetImage.tStopRefresh)
    # check responses
    if practiceUntimedTaskResponse.keys in ['', [], None]:  # No response was made
        practiceUntimedTaskResponse.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           practiceUntimedTaskResponse.corr = 1;  # correct non-response
        else:
           practiceUntimedTaskResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceUntimedTrials (TrialHandler)
    practiceUntimedTrials.addData('practiceUntimedTaskResponse.keys',practiceUntimedTaskResponse.keys)
    practiceUntimedTrials.addData('practiceUntimedTaskResponse.corr', practiceUntimedTaskResponse.corr)
    if practiceUntimedTaskResponse.keys != None:  # we had a response
        practiceUntimedTrials.addData('practiceUntimedTaskResponse.rt', practiceUntimedTaskResponse.rt)
    practiceUntimedTrials.addData('practiceUntimedTaskResponse.started', practiceUntimedTaskResponse.tStartRefresh)
    practiceUntimedTrials.addData('practiceUntimedTaskResponse.stopped', practiceUntimedTaskResponse.tStopRefresh)
    # the Routine "practiceUntimedTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practiceUntimedFeedbackSelect_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practiceUntimedTaskResponse.corr == 1:
        selectCorrect = 1
        selectIncorrectSolid = 0
        selectIncorrectDashed = 0
    else:
        selectCorrect = 0
        if cueType == 'solid':
            selectIncorrectSolid = 1
            selectIncorrectDashed = 0
        else:
            selectIncorrectSolid = 0
            selectIncorrectDashed = 1
     
    # keep track of which components have finished
    practiceUntimedFeedbackSelect_2Components = []
    for thisComponent in practiceUntimedFeedbackSelect_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceUntimedFeedbackSelect_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceUntimedFeedbackSelect_2"-------
    while continueRoutine:
        # get current time
        t = practiceUntimedFeedbackSelect_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceUntimedFeedbackSelect_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceUntimedFeedbackSelect_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceUntimedFeedbackSelect_2"-------
    for thisComponent in practiceUntimedFeedbackSelect_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceUntimedFeedbackSelect_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceCorrectConditionSelect = data.TrialHandler(nReps=selectCorrect, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceCorrectConditionSelect')
    thisExp.addLoop(practiceCorrectConditionSelect)  # add the loop to the experiment
    thisPracticeCorrectConditionSelect = practiceCorrectConditionSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeCorrectConditionSelect.rgb)
    if thisPracticeCorrectConditionSelect != None:
        for paramName in thisPracticeCorrectConditionSelect:
            exec('{} = thisPracticeCorrectConditionSelect[paramName]'.format(paramName))
    
    for thisPracticeCorrectConditionSelect in practiceCorrectConditionSelect:
        currentLoop = practiceCorrectConditionSelect
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeCorrectConditionSelect.rgb)
        if thisPracticeCorrectConditionSelect != None:
            for paramName in thisPracticeCorrectConditionSelect:
                exec('{} = thisPracticeCorrectConditionSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceCorrectFeedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        practiceCorrectFeedbackComponents = [practiceTimedFeedbackMessageCorrect]
        for thisComponent in practiceCorrectFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceCorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceCorrectFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceCorrectFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceCorrectFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceTimedFeedbackMessageCorrect* updates
            if practiceTimedFeedbackMessageCorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceTimedFeedbackMessageCorrect.frameNStart = frameN  # exact frame index
                practiceTimedFeedbackMessageCorrect.tStart = t  # local t and not account for scr refresh
                practiceTimedFeedbackMessageCorrect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceTimedFeedbackMessageCorrect, 'tStartRefresh')  # time at next scr refresh
                practiceTimedFeedbackMessageCorrect.setAutoDraw(True)
            if practiceTimedFeedbackMessageCorrect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceTimedFeedbackMessageCorrect.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceTimedFeedbackMessageCorrect.tStop = t  # not accounting for scr refresh
                    practiceTimedFeedbackMessageCorrect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceTimedFeedbackMessageCorrect, 'tStopRefresh')  # time at next scr refresh
                    practiceTimedFeedbackMessageCorrect.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceCorrectFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceCorrectFeedback"-------
        for thisComponent in practiceCorrectFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceCorrectConditionSelect.addData('practiceTimedFeedbackMessageCorrect.started', practiceTimedFeedbackMessageCorrect.tStartRefresh)
        practiceCorrectConditionSelect.addData('practiceTimedFeedbackMessageCorrect.stopped', practiceTimedFeedbackMessageCorrect.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectCorrect repeats of 'practiceCorrectConditionSelect'
    
    
    # set up handler to look after randomisation of conditions etc
    practiceIncorrectSolidConditionSelect = data.TrialHandler(nReps=selectIncorrectSolid, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectSolidConditionSelect')
    thisExp.addLoop(practiceIncorrectSolidConditionSelect)  # add the loop to the experiment
    thisPracticeIncorrectSolidConditionSelect = practiceIncorrectSolidConditionSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectSolidConditionSelect.rgb)
    if thisPracticeIncorrectSolidConditionSelect != None:
        for paramName in thisPracticeIncorrectSolidConditionSelect:
            exec('{} = thisPracticeIncorrectSolidConditionSelect[paramName]'.format(paramName))
    
    for thisPracticeIncorrectSolidConditionSelect in practiceIncorrectSolidConditionSelect:
        currentLoop = practiceIncorrectSolidConditionSelect
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectSolidConditionSelect.rgb)
        if thisPracticeIncorrectSolidConditionSelect != None:
            for paramName in thisPracticeIncorrectSolidConditionSelect:
                exec('{} = thisPracticeIncorrectSolidConditionSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectSolidFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        feedbackSound.setSound('A', secs=1.0, hamming=True)
        feedbackSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectSolidFeedbackComponents = [feedbackSound, feedbackSolidIncorrectImage]
        for thisComponent in practiceIncorrectSolidFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectSolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectSolidFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectSolidFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectSolidFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop feedbackSound
            if feedbackSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSound.frameNStart = frameN  # exact frame index
                feedbackSound.tStart = t  # local t and not account for scr refresh
                feedbackSound.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackSound.play(when=win)  # sync with win flip
            if feedbackSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSound.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSound.tStop = t  # not accounting for scr refresh
                    feedbackSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSound, 'tStopRefresh')  # time at next scr refresh
                    feedbackSound.stop()
            
            # *feedbackSolidIncorrectImage* updates
            if feedbackSolidIncorrectImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSolidIncorrectImage.frameNStart = frameN  # exact frame index
                feedbackSolidIncorrectImage.tStart = t  # local t and not account for scr refresh
                feedbackSolidIncorrectImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackSolidIncorrectImage, 'tStartRefresh')  # time at next scr refresh
                feedbackSolidIncorrectImage.setAutoDraw(True)
            if feedbackSolidIncorrectImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSolidIncorrectImage.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSolidIncorrectImage.tStop = t  # not accounting for scr refresh
                    feedbackSolidIncorrectImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSolidIncorrectImage, 'tStopRefresh')  # time at next scr refresh
                    feedbackSolidIncorrectImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectSolidFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectSolidFeedback"-------
        for thisComponent in practiceIncorrectSolidFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedbackSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectSolidConditionSelect.addData('feedbackSound.started', feedbackSound.tStartRefresh)
        practiceIncorrectSolidConditionSelect.addData('feedbackSound.stopped', feedbackSound.tStopRefresh)
        practiceIncorrectSolidConditionSelect.addData('feedbackSolidIncorrectImage.started', feedbackSolidIncorrectImage.tStartRefresh)
        practiceIncorrectSolidConditionSelect.addData('feedbackSolidIncorrectImage.stopped', feedbackSolidIncorrectImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectSolid repeats of 'practiceIncorrectSolidConditionSelect'
    
    
    # set up handler to look after randomisation of conditions etc
    practiceIncorrectDashedConditionSelect = data.TrialHandler(nReps=selectIncorrectDashed, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectDashedConditionSelect')
    thisExp.addLoop(practiceIncorrectDashedConditionSelect)  # add the loop to the experiment
    thisPracticeIncorrectDashedConditionSelect = practiceIncorrectDashedConditionSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectDashedConditionSelect.rgb)
    if thisPracticeIncorrectDashedConditionSelect != None:
        for paramName in thisPracticeIncorrectDashedConditionSelect:
            exec('{} = thisPracticeIncorrectDashedConditionSelect[paramName]'.format(paramName))
    
    for thisPracticeIncorrectDashedConditionSelect in practiceIncorrectDashedConditionSelect:
        currentLoop = practiceIncorrectDashedConditionSelect
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectDashedConditionSelect.rgb)
        if thisPracticeIncorrectDashedConditionSelect != None:
            for paramName in thisPracticeIncorrectDashedConditionSelect:
                exec('{} = thisPracticeIncorrectDashedConditionSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectDashFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        practiceIncorrectDashedSound.setSound('A', secs=1.0, hamming=True)
        practiceIncorrectDashedSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectDashFeedbackComponents = [practiceIncorrectDashedSound, practiceIncorrectDashedFeedbackImage]
        for thisComponent in practiceIncorrectDashFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectDashFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectDashFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectDashFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectDashFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop practiceIncorrectDashedSound
            if practiceIncorrectDashedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceIncorrectDashedSound.frameNStart = frameN  # exact frame index
                practiceIncorrectDashedSound.tStart = t  # local t and not account for scr refresh
                practiceIncorrectDashedSound.tStartRefresh = tThisFlipGlobal  # on global time
                practiceIncorrectDashedSound.play(when=win)  # sync with win flip
            if practiceIncorrectDashedSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceIncorrectDashedSound.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceIncorrectDashedSound.tStop = t  # not accounting for scr refresh
                    practiceIncorrectDashedSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceIncorrectDashedSound, 'tStopRefresh')  # time at next scr refresh
                    practiceIncorrectDashedSound.stop()
            
            # *practiceIncorrectDashedFeedbackImage* updates
            if practiceIncorrectDashedFeedbackImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceIncorrectDashedFeedbackImage.frameNStart = frameN  # exact frame index
                practiceIncorrectDashedFeedbackImage.tStart = t  # local t and not account for scr refresh
                practiceIncorrectDashedFeedbackImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceIncorrectDashedFeedbackImage, 'tStartRefresh')  # time at next scr refresh
                practiceIncorrectDashedFeedbackImage.setAutoDraw(True)
            if practiceIncorrectDashedFeedbackImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceIncorrectDashedFeedbackImage.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceIncorrectDashedFeedbackImage.tStop = t  # not accounting for scr refresh
                    practiceIncorrectDashedFeedbackImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceIncorrectDashedFeedbackImage, 'tStopRefresh')  # time at next scr refresh
                    practiceIncorrectDashedFeedbackImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectDashFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectDashFeedback"-------
        for thisComponent in practiceIncorrectDashFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceIncorrectDashedSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectDashedConditionSelect.addData('practiceIncorrectDashedSound.started', practiceIncorrectDashedSound.tStartRefresh)
        practiceIncorrectDashedConditionSelect.addData('practiceIncorrectDashedSound.stopped', practiceIncorrectDashedSound.tStopRefresh)
        practiceIncorrectDashedConditionSelect.addData('practiceIncorrectDashedFeedbackImage.started', practiceIncorrectDashedFeedbackImage.tStartRefresh)
        practiceIncorrectDashedConditionSelect.addData('practiceIncorrectDashedFeedbackImage.stopped', practiceIncorrectDashedFeedbackImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectDashed repeats of 'practiceIncorrectDashedConditionSelect'
    
    
    # ------Prepare to start Routine "practiceDelay"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    practiceDelayComponents = [delayText]
    for thisComponent in practiceDelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceDelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceDelay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceDelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceDelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *delayText* updates
        if delayText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            delayText.frameNStart = frameN  # exact frame index
            delayText.tStart = t  # local t and not account for scr refresh
            delayText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayText, 'tStartRefresh')  # time at next scr refresh
            delayText.setAutoDraw(True)
        if delayText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > delayText.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                delayText.tStop = t  # not accounting for scr refresh
                delayText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(delayText, 'tStopRefresh')  # time at next scr refresh
                delayText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceDelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceDelay"-------
    for thisComponent in practiceDelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceUntimedTrials.addData('delayText.started', delayText.tStartRefresh)
    practiceUntimedTrials.addData('delayText.stopped', delayText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'practiceUntimedTrials'


# ------Prepare to start Routine "practiceTimedInstructions01"-------
continueRoutine = True
# update component parameters for each repeat
practiceTimedInstructions01KeyResponse.keys = []
practiceTimedInstructions01KeyResponse.rt = []
_practiceTimedInstructions01KeyResponse_allKeys = []
# keep track of which components have finished
practiceTimedInstructions01Components = [practiceTimedInstructions01Image, practiceTimedInstructions01KeyResponse]
for thisComponent in practiceTimedInstructions01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceTimedInstructions01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceTimedInstructions01"-------
while continueRoutine:
    # get current time
    t = practiceTimedInstructions01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceTimedInstructions01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceTimedInstructions01Image* updates
    if practiceTimedInstructions01Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedInstructions01Image.frameNStart = frameN  # exact frame index
        practiceTimedInstructions01Image.tStart = t  # local t and not account for scr refresh
        practiceTimedInstructions01Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedInstructions01Image, 'tStartRefresh')  # time at next scr refresh
        practiceTimedInstructions01Image.setAutoDraw(True)
    
    # *practiceTimedInstructions01KeyResponse* updates
    waitOnFlip = False
    if practiceTimedInstructions01KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedInstructions01KeyResponse.frameNStart = frameN  # exact frame index
        practiceTimedInstructions01KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceTimedInstructions01KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedInstructions01KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceTimedInstructions01KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceTimedInstructions01KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceTimedInstructions01KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceTimedInstructions01KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceTimedInstructions01KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceTimedInstructions01KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceTimedInstructions01KeyResponse_allKeys):
            practiceTimedInstructions01KeyResponse.keys = _practiceTimedInstructions01KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceTimedInstructions01KeyResponse.rt = _practiceTimedInstructions01KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceTimedInstructions01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceTimedInstructions01"-------
for thisComponent in practiceTimedInstructions01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceTimedInstructions01Image.started', practiceTimedInstructions01Image.tStartRefresh)
thisExp.addData('practiceTimedInstructions01Image.stopped', practiceTimedInstructions01Image.tStopRefresh)
# check responses
if practiceTimedInstructions01KeyResponse.keys in ['', [], None]:  # No response was made
    practiceTimedInstructions01KeyResponse.keys = None
thisExp.addData('practiceTimedInstructions01KeyResponse.keys',practiceTimedInstructions01KeyResponse.keys)
if practiceTimedInstructions01KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceTimedInstructions01KeyResponse.rt', practiceTimedInstructions01KeyResponse.rt)
thisExp.addData('practiceTimedInstructions01KeyResponse.started', practiceTimedInstructions01KeyResponse.tStartRefresh)
thisExp.addData('practiceTimedInstructions01KeyResponse.stopped', practiceTimedInstructions01KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceTimedInstructions01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceTimedInstructions02"-------
continueRoutine = True
# update component parameters for each repeat
practiceTimedInstructions02KeyResponse.keys = []
practiceTimedInstructions02KeyResponse.rt = []
_practiceTimedInstructions02KeyResponse_allKeys = []
# keep track of which components have finished
practiceTimedInstructions02Components = [practiceTimedInstructions02Image, practiceTimedInstructions02KeyResponse]
for thisComponent in practiceTimedInstructions02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceTimedInstructions02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceTimedInstructions02"-------
while continueRoutine:
    # get current time
    t = practiceTimedInstructions02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceTimedInstructions02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceTimedInstructions02Image* updates
    if practiceTimedInstructions02Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedInstructions02Image.frameNStart = frameN  # exact frame index
        practiceTimedInstructions02Image.tStart = t  # local t and not account for scr refresh
        practiceTimedInstructions02Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedInstructions02Image, 'tStartRefresh')  # time at next scr refresh
        practiceTimedInstructions02Image.setAutoDraw(True)
    
    # *practiceTimedInstructions02KeyResponse* updates
    waitOnFlip = False
    if practiceTimedInstructions02KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedInstructions02KeyResponse.frameNStart = frameN  # exact frame index
        practiceTimedInstructions02KeyResponse.tStart = t  # local t and not account for scr refresh
        practiceTimedInstructions02KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedInstructions02KeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceTimedInstructions02KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceTimedInstructions02KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceTimedInstructions02KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceTimedInstructions02KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceTimedInstructions02KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _practiceTimedInstructions02KeyResponse_allKeys.extend(theseKeys)
        if len(_practiceTimedInstructions02KeyResponse_allKeys):
            practiceTimedInstructions02KeyResponse.keys = _practiceTimedInstructions02KeyResponse_allKeys[-1].name  # just the last key pressed
            practiceTimedInstructions02KeyResponse.rt = _practiceTimedInstructions02KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceTimedInstructions02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceTimedInstructions02"-------
for thisComponent in practiceTimedInstructions02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceTimedInstructions02Image.started', practiceTimedInstructions02Image.tStartRefresh)
thisExp.addData('practiceTimedInstructions02Image.stopped', practiceTimedInstructions02Image.tStopRefresh)
# check responses
if practiceTimedInstructions02KeyResponse.keys in ['', [], None]:  # No response was made
    practiceTimedInstructions02KeyResponse.keys = None
thisExp.addData('practiceTimedInstructions02KeyResponse.keys',practiceTimedInstructions02KeyResponse.keys)
if practiceTimedInstructions02KeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceTimedInstructions02KeyResponse.rt', practiceTimedInstructions02KeyResponse.rt)
thisExp.addData('practiceTimedInstructions02KeyResponse.started', practiceTimedInstructions02KeyResponse.tStartRefresh)
thisExp.addData('practiceTimedInstructions02KeyResponse.stopped', practiceTimedInstructions02KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceTimedInstructions02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTimedTrials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task-switching-replication-trialtypes.xlsx'),
    seed=None, name='practiceTimedTrials')
thisExp.addLoop(practiceTimedTrials)  # add the loop to the experiment
thisPracticeTimedTrial = practiceTimedTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTimedTrial.rgb)
if thisPracticeTimedTrial != None:
    for paramName in thisPracticeTimedTrial:
        exec('{} = thisPracticeTimedTrial[paramName]'.format(paramName))

for thisPracticeTimedTrial in practiceTimedTrials:
    currentLoop = practiceTimedTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTimedTrial.rgb)
    if thisPracticeTimedTrial != None:
        for paramName in thisPracticeTimedTrial:
            exec('{} = thisPracticeTimedTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceTimedTrial"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    practiceTimedTaskCueImage.setImage(cueFileName)
    practiceTimedTaskTargetImage.setImage(targetFileName)
    practiceTimedTaskResponse.keys = []
    practiceTimedTaskResponse.rt = []
    _practiceTimedTaskResponse_allKeys = []
    # keep track of which components have finished
    practiceTimedTrialComponents = [practiceTimedTaskCueImage, practiceTimedTaskTargetImage, practiceTimedTaskResponse]
    for thisComponent in practiceTimedTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceTimedTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceTimedTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceTimedTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceTimedTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceTimedTaskCueImage* updates
        if practiceTimedTaskCueImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practiceTimedTaskCueImage.frameNStart = frameN  # exact frame index
            practiceTimedTaskCueImage.tStart = t  # local t and not account for scr refresh
            practiceTimedTaskCueImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceTimedTaskCueImage, 'tStartRefresh')  # time at next scr refresh
            practiceTimedTaskCueImage.setAutoDraw(True)
        if practiceTimedTaskCueImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceTimedTaskCueImage.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                practiceTimedTaskCueImage.tStop = t  # not accounting for scr refresh
                practiceTimedTaskCueImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceTimedTaskCueImage, 'tStopRefresh')  # time at next scr refresh
                practiceTimedTaskCueImage.setAutoDraw(False)
        
        # *practiceTimedTaskTargetImage* updates
        if practiceTimedTaskTargetImage.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            practiceTimedTaskTargetImage.frameNStart = frameN  # exact frame index
            practiceTimedTaskTargetImage.tStart = t  # local t and not account for scr refresh
            practiceTimedTaskTargetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceTimedTaskTargetImage, 'tStartRefresh')  # time at next scr refresh
            practiceTimedTaskTargetImage.setAutoDraw(True)
        if practiceTimedTaskTargetImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceTimedTaskTargetImage.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                practiceTimedTaskTargetImage.tStop = t  # not accounting for scr refresh
                practiceTimedTaskTargetImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceTimedTaskTargetImage, 'tStopRefresh')  # time at next scr refresh
                practiceTimedTaskTargetImage.setAutoDraw(False)
        
        # *practiceTimedTaskResponse* updates
        waitOnFlip = False
        if practiceTimedTaskResponse.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            practiceTimedTaskResponse.frameNStart = frameN  # exact frame index
            practiceTimedTaskResponse.tStart = t  # local t and not account for scr refresh
            practiceTimedTaskResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceTimedTaskResponse, 'tStartRefresh')  # time at next scr refresh
            practiceTimedTaskResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practiceTimedTaskResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practiceTimedTaskResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practiceTimedTaskResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceTimedTaskResponse.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                practiceTimedTaskResponse.tStop = t  # not accounting for scr refresh
                practiceTimedTaskResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceTimedTaskResponse, 'tStopRefresh')  # time at next scr refresh
                practiceTimedTaskResponse.status = FINISHED
        if practiceTimedTaskResponse.status == STARTED and not waitOnFlip:
            theseKeys = practiceTimedTaskResponse.getKeys(keyList=['1', '2'], waitRelease=False)
            _practiceTimedTaskResponse_allKeys.extend(theseKeys)
            if len(_practiceTimedTaskResponse_allKeys):
                practiceTimedTaskResponse.keys = _practiceTimedTaskResponse_allKeys[-1].name  # just the last key pressed
                practiceTimedTaskResponse.rt = _practiceTimedTaskResponse_allKeys[-1].rt
                # was this correct?
                if (practiceTimedTaskResponse.keys == str(correctAnswer)) or (practiceTimedTaskResponse.keys == correctAnswer):
                    practiceTimedTaskResponse.corr = 1
                else:
                    practiceTimedTaskResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTimedTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceTimedTrial"-------
    for thisComponent in practiceTimedTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTimedTrials.addData('practiceTimedTaskCueImage.started', practiceTimedTaskCueImage.tStartRefresh)
    practiceTimedTrials.addData('practiceTimedTaskCueImage.stopped', practiceTimedTaskCueImage.tStopRefresh)
    practiceTimedTrials.addData('practiceTimedTaskTargetImage.started', practiceTimedTaskTargetImage.tStartRefresh)
    practiceTimedTrials.addData('practiceTimedTaskTargetImage.stopped', practiceTimedTaskTargetImage.tStopRefresh)
    # check responses
    if practiceTimedTaskResponse.keys in ['', [], None]:  # No response was made
        practiceTimedTaskResponse.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           practiceTimedTaskResponse.corr = 1;  # correct non-response
        else:
           practiceTimedTaskResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceTimedTrials (TrialHandler)
    practiceTimedTrials.addData('practiceTimedTaskResponse.keys',practiceTimedTaskResponse.keys)
    practiceTimedTrials.addData('practiceTimedTaskResponse.corr', practiceTimedTaskResponse.corr)
    if practiceTimedTaskResponse.keys != None:  # we had a response
        practiceTimedTrials.addData('practiceTimedTaskResponse.rt', practiceTimedTaskResponse.rt)
    practiceTimedTrials.addData('practiceTimedTaskResponse.started', practiceTimedTaskResponse.tStartRefresh)
    practiceTimedTrials.addData('practiceTimedTaskResponse.stopped', practiceTimedTaskResponse.tStopRefresh)
    
    # ------Prepare to start Routine "practiceTimedFeedbackSelect"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practiceTimedTaskResponse.corr == 1:
        selectCorrect = 1
        selectIncorrectSolid = 0
        selectIncorrectDashed = 0
    else:
        selectCorrect = 0
        if cueType == 'solid':
            selectIncorrectSolid = 1
            selectIncorrectDashed = 0
        else:
            selectIncorrectSolid = 0
            selectIncorrectDashed = 1
    # keep track of which components have finished
    practiceTimedFeedbackSelectComponents = []
    for thisComponent in practiceTimedFeedbackSelectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceTimedFeedbackSelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceTimedFeedbackSelect"-------
    while continueRoutine:
        # get current time
        t = practiceTimedFeedbackSelectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceTimedFeedbackSelectClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTimedFeedbackSelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceTimedFeedbackSelect"-------
    for thisComponent in practiceTimedFeedbackSelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceTimedFeedbackSelect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceCorrectConditionSelection = data.TrialHandler(nReps=selectCorrect, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceCorrectConditionSelection')
    thisExp.addLoop(practiceCorrectConditionSelection)  # add the loop to the experiment
    thisPracticeCorrectConditionSelection = practiceCorrectConditionSelection.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeCorrectConditionSelection.rgb)
    if thisPracticeCorrectConditionSelection != None:
        for paramName in thisPracticeCorrectConditionSelection:
            exec('{} = thisPracticeCorrectConditionSelection[paramName]'.format(paramName))
    
    for thisPracticeCorrectConditionSelection in practiceCorrectConditionSelection:
        currentLoop = practiceCorrectConditionSelection
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeCorrectConditionSelection.rgb)
        if thisPracticeCorrectConditionSelection != None:
            for paramName in thisPracticeCorrectConditionSelection:
                exec('{} = thisPracticeCorrectConditionSelection[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceCorrectFeedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        practiceCorrectFeedbackComponents = [practiceTimedFeedbackMessageCorrect]
        for thisComponent in practiceCorrectFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceCorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceCorrectFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceCorrectFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceCorrectFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceTimedFeedbackMessageCorrect* updates
            if practiceTimedFeedbackMessageCorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceTimedFeedbackMessageCorrect.frameNStart = frameN  # exact frame index
                practiceTimedFeedbackMessageCorrect.tStart = t  # local t and not account for scr refresh
                practiceTimedFeedbackMessageCorrect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceTimedFeedbackMessageCorrect, 'tStartRefresh')  # time at next scr refresh
                practiceTimedFeedbackMessageCorrect.setAutoDraw(True)
            if practiceTimedFeedbackMessageCorrect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceTimedFeedbackMessageCorrect.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceTimedFeedbackMessageCorrect.tStop = t  # not accounting for scr refresh
                    practiceTimedFeedbackMessageCorrect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceTimedFeedbackMessageCorrect, 'tStopRefresh')  # time at next scr refresh
                    practiceTimedFeedbackMessageCorrect.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceCorrectFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceCorrectFeedback"-------
        for thisComponent in practiceCorrectFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceCorrectConditionSelection.addData('practiceTimedFeedbackMessageCorrect.started', practiceTimedFeedbackMessageCorrect.tStartRefresh)
        practiceCorrectConditionSelection.addData('practiceTimedFeedbackMessageCorrect.stopped', practiceTimedFeedbackMessageCorrect.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectCorrect repeats of 'practiceCorrectConditionSelection'
    
    
    # set up handler to look after randomisation of conditions etc
    practiceIncorrectSolidConditionSelection = data.TrialHandler(nReps=selectIncorrectSolid, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectSolidConditionSelection')
    thisExp.addLoop(practiceIncorrectSolidConditionSelection)  # add the loop to the experiment
    thisPracticeIncorrectSolidConditionSelection = practiceIncorrectSolidConditionSelection.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectSolidConditionSelection.rgb)
    if thisPracticeIncorrectSolidConditionSelection != None:
        for paramName in thisPracticeIncorrectSolidConditionSelection:
            exec('{} = thisPracticeIncorrectSolidConditionSelection[paramName]'.format(paramName))
    
    for thisPracticeIncorrectSolidConditionSelection in practiceIncorrectSolidConditionSelection:
        currentLoop = practiceIncorrectSolidConditionSelection
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectSolidConditionSelection.rgb)
        if thisPracticeIncorrectSolidConditionSelection != None:
            for paramName in thisPracticeIncorrectSolidConditionSelection:
                exec('{} = thisPracticeIncorrectSolidConditionSelection[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectSolidFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        feedbackSound.setSound('A', secs=1.0, hamming=True)
        feedbackSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectSolidFeedbackComponents = [feedbackSound, feedbackSolidIncorrectImage]
        for thisComponent in practiceIncorrectSolidFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectSolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectSolidFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectSolidFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectSolidFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop feedbackSound
            if feedbackSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSound.frameNStart = frameN  # exact frame index
                feedbackSound.tStart = t  # local t and not account for scr refresh
                feedbackSound.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackSound.play(when=win)  # sync with win flip
            if feedbackSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSound.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSound.tStop = t  # not accounting for scr refresh
                    feedbackSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSound, 'tStopRefresh')  # time at next scr refresh
                    feedbackSound.stop()
            
            # *feedbackSolidIncorrectImage* updates
            if feedbackSolidIncorrectImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSolidIncorrectImage.frameNStart = frameN  # exact frame index
                feedbackSolidIncorrectImage.tStart = t  # local t and not account for scr refresh
                feedbackSolidIncorrectImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackSolidIncorrectImage, 'tStartRefresh')  # time at next scr refresh
                feedbackSolidIncorrectImage.setAutoDraw(True)
            if feedbackSolidIncorrectImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSolidIncorrectImage.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSolidIncorrectImage.tStop = t  # not accounting for scr refresh
                    feedbackSolidIncorrectImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSolidIncorrectImage, 'tStopRefresh')  # time at next scr refresh
                    feedbackSolidIncorrectImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectSolidFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectSolidFeedback"-------
        for thisComponent in practiceIncorrectSolidFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedbackSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectSolidConditionSelection.addData('feedbackSound.started', feedbackSound.tStartRefresh)
        practiceIncorrectSolidConditionSelection.addData('feedbackSound.stopped', feedbackSound.tStopRefresh)
        practiceIncorrectSolidConditionSelection.addData('feedbackSolidIncorrectImage.started', feedbackSolidIncorrectImage.tStartRefresh)
        practiceIncorrectSolidConditionSelection.addData('feedbackSolidIncorrectImage.stopped', feedbackSolidIncorrectImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectSolid repeats of 'practiceIncorrectSolidConditionSelection'
    
    
    # set up handler to look after randomisation of conditions etc
    practiceIncorrectDashedConditionSelect2 = data.TrialHandler(nReps=selectIncorrectDashed, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectDashedConditionSelect2')
    thisExp.addLoop(practiceIncorrectDashedConditionSelect2)  # add the loop to the experiment
    thisPracticeIncorrectDashedConditionSelect2 = practiceIncorrectDashedConditionSelect2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectDashedConditionSelect2.rgb)
    if thisPracticeIncorrectDashedConditionSelect2 != None:
        for paramName in thisPracticeIncorrectDashedConditionSelect2:
            exec('{} = thisPracticeIncorrectDashedConditionSelect2[paramName]'.format(paramName))
    
    for thisPracticeIncorrectDashedConditionSelect2 in practiceIncorrectDashedConditionSelect2:
        currentLoop = practiceIncorrectDashedConditionSelect2
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectDashedConditionSelect2.rgb)
        if thisPracticeIncorrectDashedConditionSelect2 != None:
            for paramName in thisPracticeIncorrectDashedConditionSelect2:
                exec('{} = thisPracticeIncorrectDashedConditionSelect2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectDashFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        practiceIncorrectDashedSound.setSound('A', secs=1.0, hamming=True)
        practiceIncorrectDashedSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectDashFeedbackComponents = [practiceIncorrectDashedSound, practiceIncorrectDashedFeedbackImage]
        for thisComponent in practiceIncorrectDashFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectDashFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectDashFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectDashFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectDashFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop practiceIncorrectDashedSound
            if practiceIncorrectDashedSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceIncorrectDashedSound.frameNStart = frameN  # exact frame index
                practiceIncorrectDashedSound.tStart = t  # local t and not account for scr refresh
                practiceIncorrectDashedSound.tStartRefresh = tThisFlipGlobal  # on global time
                practiceIncorrectDashedSound.play(when=win)  # sync with win flip
            if practiceIncorrectDashedSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceIncorrectDashedSound.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceIncorrectDashedSound.tStop = t  # not accounting for scr refresh
                    practiceIncorrectDashedSound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceIncorrectDashedSound, 'tStopRefresh')  # time at next scr refresh
                    practiceIncorrectDashedSound.stop()
            
            # *practiceIncorrectDashedFeedbackImage* updates
            if practiceIncorrectDashedFeedbackImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practiceIncorrectDashedFeedbackImage.frameNStart = frameN  # exact frame index
                practiceIncorrectDashedFeedbackImage.tStart = t  # local t and not account for scr refresh
                practiceIncorrectDashedFeedbackImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practiceIncorrectDashedFeedbackImage, 'tStartRefresh')  # time at next scr refresh
                practiceIncorrectDashedFeedbackImage.setAutoDraw(True)
            if practiceIncorrectDashedFeedbackImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practiceIncorrectDashedFeedbackImage.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practiceIncorrectDashedFeedbackImage.tStop = t  # not accounting for scr refresh
                    practiceIncorrectDashedFeedbackImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practiceIncorrectDashedFeedbackImage, 'tStopRefresh')  # time at next scr refresh
                    practiceIncorrectDashedFeedbackImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectDashFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectDashFeedback"-------
        for thisComponent in practiceIncorrectDashFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceIncorrectDashedSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectDashedConditionSelect2.addData('practiceIncorrectDashedSound.started', practiceIncorrectDashedSound.tStartRefresh)
        practiceIncorrectDashedConditionSelect2.addData('practiceIncorrectDashedSound.stopped', practiceIncorrectDashedSound.tStopRefresh)
        practiceIncorrectDashedConditionSelect2.addData('practiceIncorrectDashedFeedbackImage.started', practiceIncorrectDashedFeedbackImage.tStartRefresh)
        practiceIncorrectDashedConditionSelect2.addData('practiceIncorrectDashedFeedbackImage.stopped', practiceIncorrectDashedFeedbackImage.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectDashed repeats of 'practiceIncorrectDashedConditionSelect2'
    
    
    # ------Prepare to start Routine "practiceDelay"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    practiceDelayComponents = [delayText]
    for thisComponent in practiceDelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceDelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceDelay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceDelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceDelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *delayText* updates
        if delayText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            delayText.frameNStart = frameN  # exact frame index
            delayText.tStart = t  # local t and not account for scr refresh
            delayText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayText, 'tStartRefresh')  # time at next scr refresh
            delayText.setAutoDraw(True)
        if delayText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > delayText.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                delayText.tStop = t  # not accounting for scr refresh
                delayText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(delayText, 'tStopRefresh')  # time at next scr refresh
                delayText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceDelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceDelay"-------
    for thisComponent in practiceDelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTimedTrials.addData('delayText.started', delayText.tStartRefresh)
    practiceTimedTrials.addData('delayText.stopped', delayText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'practiceTimedTrials'


# ------Prepare to start Routine "experimentInstructions01"-------
continueRoutine = True
# update component parameters for each repeat
experimentInstructions01KeyResponse.keys = []
experimentInstructions01KeyResponse.rt = []
_experimentInstructions01KeyResponse_allKeys = []
# keep track of which components have finished
experimentInstructions01Components = [experimentInstructions01Image, experimentInstructions01KeyResponse]
for thisComponent in experimentInstructions01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
experimentInstructions01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experimentInstructions01"-------
while continueRoutine:
    # get current time
    t = experimentInstructions01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experimentInstructions01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *experimentInstructions01Image* updates
    if experimentInstructions01Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experimentInstructions01Image.frameNStart = frameN  # exact frame index
        experimentInstructions01Image.tStart = t  # local t and not account for scr refresh
        experimentInstructions01Image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experimentInstructions01Image, 'tStartRefresh')  # time at next scr refresh
        experimentInstructions01Image.setAutoDraw(True)
    
    # *experimentInstructions01KeyResponse* updates
    waitOnFlip = False
    if experimentInstructions01KeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experimentInstructions01KeyResponse.frameNStart = frameN  # exact frame index
        experimentInstructions01KeyResponse.tStart = t  # local t and not account for scr refresh
        experimentInstructions01KeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experimentInstructions01KeyResponse, 'tStartRefresh')  # time at next scr refresh
        experimentInstructions01KeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experimentInstructions01KeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experimentInstructions01KeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experimentInstructions01KeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = experimentInstructions01KeyResponse.getKeys(keyList=['1', '2'], waitRelease=False)
        _experimentInstructions01KeyResponse_allKeys.extend(theseKeys)
        if len(_experimentInstructions01KeyResponse_allKeys):
            experimentInstructions01KeyResponse.keys = _experimentInstructions01KeyResponse_allKeys[-1].name  # just the last key pressed
            experimentInstructions01KeyResponse.rt = _experimentInstructions01KeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experimentInstructions01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experimentInstructions01"-------
for thisComponent in experimentInstructions01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('experimentInstructions01Image.started', experimentInstructions01Image.tStartRefresh)
thisExp.addData('experimentInstructions01Image.stopped', experimentInstructions01Image.tStopRefresh)
# check responses
if experimentInstructions01KeyResponse.keys in ['', [], None]:  # No response was made
    experimentInstructions01KeyResponse.keys = None
thisExp.addData('experimentInstructions01KeyResponse.keys',experimentInstructions01KeyResponse.keys)
if experimentInstructions01KeyResponse.keys != None:  # we had a response
    thisExp.addData('experimentInstructions01KeyResponse.rt', experimentInstructions01KeyResponse.rt)
thisExp.addData('experimentInstructions01KeyResponse.started', experimentInstructions01KeyResponse.tStartRefresh)
thisExp.addData('experimentInstructions01KeyResponse.stopped', experimentInstructions01KeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "experimentInstructions01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task-switching-replication-trialtypes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "experimentTimedTrial"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    expCueImage.setImage(cueFileName)
    expTargetImage.setImage(targetFileName)
    expResponse.keys = []
    expResponse.rt = []
    _expResponse_allKeys = []
    # keep track of which components have finished
    experimentTimedTrialComponents = [expCueImage, expTargetImage, expResponse]
    for thisComponent in experimentTimedTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentTimedTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experimentTimedTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = experimentTimedTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentTimedTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *expCueImage* updates
        if expCueImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            expCueImage.frameNStart = frameN  # exact frame index
            expCueImage.tStart = t  # local t and not account for scr refresh
            expCueImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(expCueImage, 'tStartRefresh')  # time at next scr refresh
            expCueImage.setAutoDraw(True)
        if expCueImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > expCueImage.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                expCueImage.tStop = t  # not accounting for scr refresh
                expCueImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(expCueImage, 'tStopRefresh')  # time at next scr refresh
                expCueImage.setAutoDraw(False)
        
        # *expTargetImage* updates
        if expTargetImage.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            expTargetImage.frameNStart = frameN  # exact frame index
            expTargetImage.tStart = t  # local t and not account for scr refresh
            expTargetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(expTargetImage, 'tStartRefresh')  # time at next scr refresh
            expTargetImage.setAutoDraw(True)
        if expTargetImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > expTargetImage.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                expTargetImage.tStop = t  # not accounting for scr refresh
                expTargetImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(expTargetImage, 'tStopRefresh')  # time at next scr refresh
                expTargetImage.setAutoDraw(False)
        
        # *expResponse* updates
        waitOnFlip = False
        if expResponse.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            expResponse.frameNStart = frameN  # exact frame index
            expResponse.tStart = t  # local t and not account for scr refresh
            expResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(expResponse, 'tStartRefresh')  # time at next scr refresh
            expResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(expResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(expResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if expResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > expResponse.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                expResponse.tStop = t  # not accounting for scr refresh
                expResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(expResponse, 'tStopRefresh')  # time at next scr refresh
                expResponse.status = FINISHED
        if expResponse.status == STARTED and not waitOnFlip:
            theseKeys = expResponse.getKeys(keyList=['1', '2'], waitRelease=False)
            _expResponse_allKeys.extend(theseKeys)
            if len(_expResponse_allKeys):
                expResponse.keys = _expResponse_allKeys[-1].name  # just the last key pressed
                expResponse.rt = _expResponse_allKeys[-1].rt
                # was this correct?
                if (expResponse.keys == str(correctAnswer)) or (expResponse.keys == correctAnswer):
                    expResponse.corr = 1
                else:
                    expResponse.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentTimedTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experimentTimedTrial"-------
    for thisComponent in experimentTimedTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('expCueImage.started', expCueImage.tStartRefresh)
    trials.addData('expCueImage.stopped', expCueImage.tStopRefresh)
    trials.addData('expTargetImage.started', expTargetImage.tStartRefresh)
    trials.addData('expTargetImage.stopped', expTargetImage.tStopRefresh)
    # check responses
    if expResponse.keys in ['', [], None]:  # No response was made
        expResponse.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           expResponse.corr = 1;  # correct non-response
        else:
           expResponse.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('expResponse.keys',expResponse.keys)
    trials.addData('expResponse.corr', expResponse.corr)
    if expResponse.keys != None:  # we had a response
        trials.addData('expResponse.rt', expResponse.rt)
    trials.addData('expResponse.started', expResponse.tStartRefresh)
    trials.addData('expResponse.stopped', expResponse.tStopRefresh)
    
    # ------Prepare to start Routine "experimentFeedbackSelect"-------
    continueRoutine = True
    # update component parameters for each repeat
    if expResponse.corr == 1:
        selectCorrect = 1
        selectIncorrectSolid = 0
        selectIncorrectDashed = 0
    else:
        selectCorrect = 0
        if cueType == 'solid':
            selectIncorrectSolid = 1
            selectIncorrectDashed = 0
        else:
            selectIncorrectSolid = 0
            selectIncorrectDashed = 1
    # keep track of which components have finished
    experimentFeedbackSelectComponents = []
    for thisComponent in experimentFeedbackSelectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentFeedbackSelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experimentFeedbackSelect"-------
    while continueRoutine:
        # get current time
        t = experimentFeedbackSelectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentFeedbackSelectClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentFeedbackSelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experimentFeedbackSelect"-------
    for thisComponent in experimentFeedbackSelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "experimentFeedbackSelect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    experimentIncorrectSolidSelect = data.TrialHandler(nReps=selectIncorrectSolid, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='experimentIncorrectSolidSelect')
    thisExp.addLoop(experimentIncorrectSolidSelect)  # add the loop to the experiment
    thisExperimentIncorrectSolidSelect = experimentIncorrectSolidSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperimentIncorrectSolidSelect.rgb)
    if thisExperimentIncorrectSolidSelect != None:
        for paramName in thisExperimentIncorrectSolidSelect:
            exec('{} = thisExperimentIncorrectSolidSelect[paramName]'.format(paramName))
    
    for thisExperimentIncorrectSolidSelect in experimentIncorrectSolidSelect:
        currentLoop = experimentIncorrectSolidSelect
        # abbreviate parameter names if possible (e.g. rgb = thisExperimentIncorrectSolidSelect.rgb)
        if thisExperimentIncorrectSolidSelect != None:
            for paramName in thisExperimentIncorrectSolidSelect:
                exec('{} = thisExperimentIncorrectSolidSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "experimentIncorrectSolidFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_1.setSound('A', secs=1.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        experimentIncorrectSolidFeedbackComponents = [sound_1, image_2]
        for thisComponent in experimentIncorrectSolidFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        experimentIncorrectSolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "experimentIncorrectSolidFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = experimentIncorrectSolidFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=experimentIncorrectSolidFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experimentIncorrectSolidFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "experimentIncorrectSolidFeedback"-------
        for thisComponent in experimentIncorrectSolidFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        experimentIncorrectSolidSelect.addData('sound_1.started', sound_1.tStartRefresh)
        experimentIncorrectSolidSelect.addData('sound_1.stopped', sound_1.tStopRefresh)
        experimentIncorrectSolidSelect.addData('image_2.started', image_2.tStartRefresh)
        experimentIncorrectSolidSelect.addData('image_2.stopped', image_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectSolid repeats of 'experimentIncorrectSolidSelect'
    
    
    # set up handler to look after randomisation of conditions etc
    experimentIncorrectDashedSelect = data.TrialHandler(nReps=selectIncorrectDashed, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='experimentIncorrectDashedSelect')
    thisExp.addLoop(experimentIncorrectDashedSelect)  # add the loop to the experiment
    thisExperimentIncorrectDashedSelect = experimentIncorrectDashedSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExperimentIncorrectDashedSelect.rgb)
    if thisExperimentIncorrectDashedSelect != None:
        for paramName in thisExperimentIncorrectDashedSelect:
            exec('{} = thisExperimentIncorrectDashedSelect[paramName]'.format(paramName))
    
    for thisExperimentIncorrectDashedSelect in experimentIncorrectDashedSelect:
        currentLoop = experimentIncorrectDashedSelect
        # abbreviate parameter names if possible (e.g. rgb = thisExperimentIncorrectDashedSelect.rgb)
        if thisExperimentIncorrectDashedSelect != None:
            for paramName in thisExperimentIncorrectDashedSelect:
                exec('{} = thisExperimentIncorrectDashedSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "experimentIncorrectDashedFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_2.setSound('A', secs=1.0, hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        experimentIncorrectDashedFeedbackComponents = [sound_2, image_3]
        for thisComponent in experimentIncorrectDashedFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        experimentIncorrectDashedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "experimentIncorrectDashedFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = experimentIncorrectDashedFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=experimentIncorrectDashedFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_2
            if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                sound_2.play(when=win)  # sync with win flip
            if sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_2.tStop = t  # not accounting for scr refresh
                    sound_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                    sound_2.stop()
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in experimentIncorrectDashedFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "experimentIncorrectDashedFeedback"-------
        for thisComponent in experimentIncorrectDashedFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_2.stop()  # ensure sound has stopped at end of routine
        experimentIncorrectDashedSelect.addData('sound_2.started', sound_2.tStartRefresh)
        experimentIncorrectDashedSelect.addData('sound_2.stopped', sound_2.tStopRefresh)
        experimentIncorrectDashedSelect.addData('image_3.started', image_3.tStartRefresh)
        experimentIncorrectDashedSelect.addData('image_3.stopped', image_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectDashed repeats of 'experimentIncorrectDashedSelect'
    
    
    # ------Prepare to start Routine "experimentDelay"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    experimentDelayComponents = [text]
    for thisComponent in experimentDelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentDelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experimentDelay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = experimentDelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentDelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentDelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experimentDelay"-------
    for thisComponent in experimentDelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
