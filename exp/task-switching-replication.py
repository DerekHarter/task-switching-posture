#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue 05 Oct 2021 08:51:09 PM CDT
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
expInfo = {'participant': '', 'session': '001'}
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

# Initialize components for Routine "practiceUntimedInstructions"
practiceUntimedInstructionsClock = core.Clock()
practiceUntimedInstructionText = visual.TextStim(win=win, name='practiceUntimedInstructionText',
    text='Respond to the cue. \n\nPractice Trials. Take as much\ntime as you need to learn and\nrespond to the task.\n\n We will first  practice the task untimed\nso you can learn how to respond correctly.\n\nFor this task you will first\nsee a cue, a dashed box or a solid box.\nYou must respond to the shape or\ncolor depending on the box.\n\nFor a dashed box, respond to the color.\nleft for yellow, right for blue\n\nFor a solid box, respond to the shape.\nleft for triangle, right for square.\n\nRemember: \ndashed: left yellow right blue\nsolid: left triangle, right square\n\nPress any key to begin practicing experiment.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practiceUntimedKeyResponse = keyboard.Keyboard()

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

# Initialize components for Routine "practiceFeedbackSelect"
practiceFeedbackSelectClock = core.Clock()
selectCorrect = 0
selectIncorrect = 0

# Initialize components for Routine "practiceCorrectFeedback"
practiceCorrectFeedbackClock = core.Clock()
practiceTimedFeedbackMessageCorrect = visual.TextStim(win=win, name='practiceTimedFeedbackMessageCorrect',
    text='Correct Response\n\nRemember respond to the square\ncue as quickly as you can.\n\nDashed box, respond to color.\nleft for yellow, right for blue\n\nSolid box, respond to shape.\nleft for triangle, right for square.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceIncorrectFeedback"
practiceIncorrectFeedbackClock = core.Clock()
feedbackTextIncorrect = visual.TextStim(win=win, name='feedbackTextIncorrect',
    text='Incorrect Response\n\n\nRemember respond to the square\ncue as quickly as you can.\n\nDashed box, respond to color.\nleft for yellow, right for blue\n\nSolid box, respond to shape.\nleft for triangle, right for square.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedbackSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='feedbackSound')
feedbackSound.setVolume(1.0)

# Initialize components for Routine "practiceDelay"
practiceDelayClock = core.Clock()
delayText = visual.TextStim(win=win, name='delayText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceTimedInstructions"
practiceTimedInstructionsClock = core.Clock()
practiceTimedInstructionText = visual.TextStim(win=win, name='practiceTimedInstructionText',
    text='Respond to the cue. \n\nPractice Trials.  For these practice trials\nyou will have a time limit to respond.\nYou must respond within 1.5 seconds\nto the stimulus.\n\n We will  now practice the task\nso you can learn how to respond\nwithin the time limit correctly.\nFor this task you will first\nsee a cue, a dashed box or a solid box.\nYou must respond to the shape or\ncolor within 1.5 seconds.\n\nFor a dashed box, respond to the color.\nleft for yellow, right for blue\n\nFor a solid box, respond to the shape.\nleft for triangle, right for square.\n\nRemember: \ndashed: left yellow right blue\nsolid: left triangle, right square\n\nPress any key to begin practicing experiment.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practiceTimedKeyResponse = keyboard.Keyboard()

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

# Initialize components for Routine "practiceFeedbackSelect"
practiceFeedbackSelectClock = core.Clock()
selectCorrect = 0
selectIncorrect = 0

# Initialize components for Routine "practiceCorrectFeedback"
practiceCorrectFeedbackClock = core.Clock()
practiceTimedFeedbackMessageCorrect = visual.TextStim(win=win, name='practiceTimedFeedbackMessageCorrect',
    text='Correct Response\n\nRemember respond to the square\ncue as quickly as you can.\n\nDashed box, respond to color.\nleft for yellow, right for blue\n\nSolid box, respond to shape.\nleft for triangle, right for square.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=25.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practiceIncorrectFeedback"
practiceIncorrectFeedbackClock = core.Clock()
feedbackTextIncorrect = visual.TextStim(win=win, name='feedbackTextIncorrect',
    text='Incorrect Response\n\n\nRemember respond to the square\ncue as quickly as you can.\n\nDashed box, respond to color.\nleft for yellow, right for blue\n\nSolid box, respond to shape.\nleft for triangle, right for square.',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedbackSound = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='feedbackSound')
feedbackSound.setVolume(1.0)

# Initialize components for Routine "practiceDelay"
practiceDelayClock = core.Clock()
delayText = visual.TextStim(win=win, name='delayText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practiceUntimedInstructions"-------
continueRoutine = True
# update component parameters for each repeat
practiceUntimedKeyResponse.keys = []
practiceUntimedKeyResponse.rt = []
_practiceUntimedKeyResponse_allKeys = []
# keep track of which components have finished
practiceUntimedInstructionsComponents = [practiceUntimedInstructionText, practiceUntimedKeyResponse]
for thisComponent in practiceUntimedInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceUntimedInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceUntimedInstructions"-------
while continueRoutine:
    # get current time
    t = practiceUntimedInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceUntimedInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceUntimedInstructionText* updates
    if practiceUntimedInstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedInstructionText.frameNStart = frameN  # exact frame index
        practiceUntimedInstructionText.tStart = t  # local t and not account for scr refresh
        practiceUntimedInstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedInstructionText, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedInstructionText.setAutoDraw(True)
    
    # *practiceUntimedKeyResponse* updates
    waitOnFlip = False
    if practiceUntimedKeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceUntimedKeyResponse.frameNStart = frameN  # exact frame index
        practiceUntimedKeyResponse.tStart = t  # local t and not account for scr refresh
        practiceUntimedKeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceUntimedKeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceUntimedKeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceUntimedKeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceUntimedKeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceUntimedKeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceUntimedKeyResponse.getKeys(keyList=None, waitRelease=False)
        _practiceUntimedKeyResponse_allKeys.extend(theseKeys)
        if len(_practiceUntimedKeyResponse_allKeys):
            practiceUntimedKeyResponse.keys = _practiceUntimedKeyResponse_allKeys[-1].name  # just the last key pressed
            practiceUntimedKeyResponse.rt = _practiceUntimedKeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceUntimedInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceUntimedInstructions"-------
for thisComponent in practiceUntimedInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceUntimedInstructionText.started', practiceUntimedInstructionText.tStartRefresh)
thisExp.addData('practiceUntimedInstructionText.stopped', practiceUntimedInstructionText.tStopRefresh)
# check responses
if practiceUntimedKeyResponse.keys in ['', [], None]:  # No response was made
    practiceUntimedKeyResponse.keys = None
thisExp.addData('practiceUntimedKeyResponse.keys',practiceUntimedKeyResponse.keys)
if practiceUntimedKeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceUntimedKeyResponse.rt', practiceUntimedKeyResponse.rt)
thisExp.addData('practiceUntimedKeyResponse.started', practiceUntimedKeyResponse.tStartRefresh)
thisExp.addData('practiceUntimedKeyResponse.stopped', practiceUntimedKeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceUntimedInstructions" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "practiceFeedbackSelect"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practiceUntimedTaskResponse.corr == 1:
        selectCorrect = 1
        selectIncorrect = 0
    else:
        selectCorrect = 0
        selectIncorrect = 1
    # keep track of which components have finished
    practiceFeedbackSelectComponents = []
    for thisComponent in practiceFeedbackSelectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceFeedbackSelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceFeedbackSelect"-------
    while continueRoutine:
        # get current time
        t = practiceFeedbackSelectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceFeedbackSelectClock)
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
        for thisComponent in practiceFeedbackSelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceFeedbackSelect"-------
    for thisComponent in practiceFeedbackSelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceFeedbackSelect" was not non-slip safe, so reset the non-slip timer
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
        routineTimer.add(5.000000)
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
                if tThisFlipGlobal > practiceTimedFeedbackMessageCorrect.tStartRefresh + 5.0-frameTolerance:
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
    practiceIncorrectConditionSelect = data.TrialHandler(nReps=selectIncorrect, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectConditionSelect')
    thisExp.addLoop(practiceIncorrectConditionSelect)  # add the loop to the experiment
    thisPracticeIncorrectConditionSelect = practiceIncorrectConditionSelect.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectConditionSelect.rgb)
    if thisPracticeIncorrectConditionSelect != None:
        for paramName in thisPracticeIncorrectConditionSelect:
            exec('{} = thisPracticeIncorrectConditionSelect[paramName]'.format(paramName))
    
    for thisPracticeIncorrectConditionSelect in practiceIncorrectConditionSelect:
        currentLoop = practiceIncorrectConditionSelect
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectConditionSelect.rgb)
        if thisPracticeIncorrectConditionSelect != None:
            for paramName in thisPracticeIncorrectConditionSelect:
                exec('{} = thisPracticeIncorrectConditionSelect[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        feedbackSound.setSound('A', secs=1.0, hamming=True)
        feedbackSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectFeedbackComponents = [feedbackTextIncorrect, feedbackSound]
        for thisComponent in practiceIncorrectFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackTextIncorrect* updates
            if feedbackTextIncorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackTextIncorrect.frameNStart = frameN  # exact frame index
                feedbackTextIncorrect.tStart = t  # local t and not account for scr refresh
                feedbackTextIncorrect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackTextIncorrect, 'tStartRefresh')  # time at next scr refresh
                feedbackTextIncorrect.setAutoDraw(True)
            if feedbackTextIncorrect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackTextIncorrect.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackTextIncorrect.tStop = t  # not accounting for scr refresh
                    feedbackTextIncorrect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackTextIncorrect, 'tStopRefresh')  # time at next scr refresh
                    feedbackTextIncorrect.setAutoDraw(False)
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectFeedback"-------
        for thisComponent in practiceIncorrectFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceIncorrectConditionSelect.addData('feedbackTextIncorrect.started', feedbackTextIncorrect.tStartRefresh)
        practiceIncorrectConditionSelect.addData('feedbackTextIncorrect.stopped', feedbackTextIncorrect.tStopRefresh)
        feedbackSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectConditionSelect.addData('feedbackSound.started', feedbackSound.tStartRefresh)
        practiceIncorrectConditionSelect.addData('feedbackSound.stopped', feedbackSound.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrect repeats of 'practiceIncorrectConditionSelect'
    
    
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


# ------Prepare to start Routine "practiceTimedInstructions"-------
continueRoutine = True
# update component parameters for each repeat
practiceTimedKeyResponse.keys = []
practiceTimedKeyResponse.rt = []
_practiceTimedKeyResponse_allKeys = []
# keep track of which components have finished
practiceTimedInstructionsComponents = [practiceTimedInstructionText, practiceTimedKeyResponse]
for thisComponent in practiceTimedInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceTimedInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceTimedInstructions"-------
while continueRoutine:
    # get current time
    t = practiceTimedInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceTimedInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceTimedInstructionText* updates
    if practiceTimedInstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedInstructionText.frameNStart = frameN  # exact frame index
        practiceTimedInstructionText.tStart = t  # local t and not account for scr refresh
        practiceTimedInstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedInstructionText, 'tStartRefresh')  # time at next scr refresh
        practiceTimedInstructionText.setAutoDraw(True)
    
    # *practiceTimedKeyResponse* updates
    waitOnFlip = False
    if practiceTimedKeyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceTimedKeyResponse.frameNStart = frameN  # exact frame index
        practiceTimedKeyResponse.tStart = t  # local t and not account for scr refresh
        practiceTimedKeyResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceTimedKeyResponse, 'tStartRefresh')  # time at next scr refresh
        practiceTimedKeyResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practiceTimedKeyResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practiceTimedKeyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceTimedKeyResponse.status == STARTED and not waitOnFlip:
        theseKeys = practiceTimedKeyResponse.getKeys(keyList=None, waitRelease=False)
        _practiceTimedKeyResponse_allKeys.extend(theseKeys)
        if len(_practiceTimedKeyResponse_allKeys):
            practiceTimedKeyResponse.keys = _practiceTimedKeyResponse_allKeys[-1].name  # just the last key pressed
            practiceTimedKeyResponse.rt = _practiceTimedKeyResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceTimedInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceTimedInstructions"-------
for thisComponent in practiceTimedInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceTimedInstructionText.started', practiceTimedInstructionText.tStartRefresh)
thisExp.addData('practiceTimedInstructionText.stopped', practiceTimedInstructionText.tStopRefresh)
# check responses
if practiceTimedKeyResponse.keys in ['', [], None]:  # No response was made
    practiceTimedKeyResponse.keys = None
thisExp.addData('practiceTimedKeyResponse.keys',practiceTimedKeyResponse.keys)
if practiceTimedKeyResponse.keys != None:  # we had a response
    thisExp.addData('practiceTimedKeyResponse.rt', practiceTimedKeyResponse.rt)
thisExp.addData('practiceTimedKeyResponse.started', practiceTimedKeyResponse.tStartRefresh)
thisExp.addData('practiceTimedKeyResponse.stopped', practiceTimedKeyResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "practiceTimedInstructions" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "practiceFeedbackSelect"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practiceUntimedTaskResponse.corr == 1:
        selectCorrect = 1
        selectIncorrect = 0
    else:
        selectCorrect = 0
        selectIncorrect = 1
    # keep track of which components have finished
    practiceFeedbackSelectComponents = []
    for thisComponent in practiceFeedbackSelectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceFeedbackSelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceFeedbackSelect"-------
    while continueRoutine:
        # get current time
        t = practiceFeedbackSelectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceFeedbackSelectClock)
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
        for thisComponent in practiceFeedbackSelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceFeedbackSelect"-------
    for thisComponent in practiceFeedbackSelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practiceFeedbackSelect" was not non-slip safe, so reset the non-slip timer
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
        routineTimer.add(5.000000)
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
                if tThisFlipGlobal > practiceTimedFeedbackMessageCorrect.tStartRefresh + 5.0-frameTolerance:
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
    practiceIncorrectConditionSelection = data.TrialHandler(nReps=selectIncorrect, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceIncorrectConditionSelection')
    thisExp.addLoop(practiceIncorrectConditionSelection)  # add the loop to the experiment
    thisPracticeIncorrectConditionSelection = practiceIncorrectConditionSelection.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectConditionSelection.rgb)
    if thisPracticeIncorrectConditionSelection != None:
        for paramName in thisPracticeIncorrectConditionSelection:
            exec('{} = thisPracticeIncorrectConditionSelection[paramName]'.format(paramName))
    
    for thisPracticeIncorrectConditionSelection in practiceIncorrectConditionSelection:
        currentLoop = practiceIncorrectConditionSelection
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeIncorrectConditionSelection.rgb)
        if thisPracticeIncorrectConditionSelection != None:
            for paramName in thisPracticeIncorrectConditionSelection:
                exec('{} = thisPracticeIncorrectConditionSelection[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practiceIncorrectFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        feedbackSound.setSound('A', secs=1.0, hamming=True)
        feedbackSound.setVolume(1.0, log=False)
        # keep track of which components have finished
        practiceIncorrectFeedbackComponents = [feedbackTextIncorrect, feedbackSound]
        for thisComponent in practiceIncorrectFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceIncorrectFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practiceIncorrectFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceIncorrectFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceIncorrectFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackTextIncorrect* updates
            if feedbackTextIncorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackTextIncorrect.frameNStart = frameN  # exact frame index
                feedbackTextIncorrect.tStart = t  # local t and not account for scr refresh
                feedbackTextIncorrect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackTextIncorrect, 'tStartRefresh')  # time at next scr refresh
                feedbackTextIncorrect.setAutoDraw(True)
            if feedbackTextIncorrect.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackTextIncorrect.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackTextIncorrect.tStop = t  # not accounting for scr refresh
                    feedbackTextIncorrect.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackTextIncorrect, 'tStopRefresh')  # time at next scr refresh
                    feedbackTextIncorrect.setAutoDraw(False)
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
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceIncorrectFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceIncorrectFeedback"-------
        for thisComponent in practiceIncorrectFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practiceIncorrectConditionSelection.addData('feedbackTextIncorrect.started', feedbackTextIncorrect.tStartRefresh)
        practiceIncorrectConditionSelection.addData('feedbackTextIncorrect.stopped', feedbackTextIncorrect.tStopRefresh)
        feedbackSound.stop()  # ensure sound has stopped at end of routine
        practiceIncorrectConditionSelection.addData('feedbackSound.started', feedbackSound.tStartRefresh)
        practiceIncorrectConditionSelection.addData('feedbackSound.stopped', feedbackSound.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrect repeats of 'practiceIncorrectConditionSelection'
    
    
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
