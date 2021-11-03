#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue 02 Nov 2021 07:38:47 PM CDT
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
expInfo = {'participant': '1000', 'session': '001', 'condition': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'../data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

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
    units='deg')
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

# Initialize components for Routine "Initialize"
InitializeClock = core.Clock()
import random
import itertools
import sys
import time

# determine experiment settings from participant condition
conditionStr = expInfo['condition']
condition = int(conditionStr)
numBlocks = 4
numTrialsPerBlock = 48
numTrialsUntimed = 12
numTrialsTimed = 24

# set up instrcution and experiment image stimuli based on condition
untimedInstruction01   = 'instructions/cond-%02d-untimed-01.png' % (condition)
untimedInstruction02   = 'instructions/cond-%02d-untimed-02.png' % (condition)
untimedInstruction03   = 'instructions/cond-%02d-untimed-03.png' % (condition)
untimedInstruction04   = 'instructions/cond-%02d-untimed-04.png' % (condition)
untimedInstruction05   = 'instructions/cond-%02d-untimed-05.png' % (condition)
untimedInstruction06   = 'instructions/cond-%02d-untimed-06.png' % (condition)
untimedInstruction07   = 'instructions/cond-%02d-untimed-07.png' % (condition)
untimedInstruction08   = 'instructions/cond-%02d-untimed-08.png' % (condition)
timedInstruction01     = 'instructions/cond-%02d-timed-01.png' % (condition)
timedInstruction02     = 'instructions/cond-%02d-timed-02.png' % (condition)
expInstruction01       = 'instructions/cond-%02d-experiment-01.png' % (condition)
errorInstructionDashed = 'instructions/cond-%02d-error-dashed.png' % (condition)
errorInstructionSolid  = 'instructions/cond-%02d-error-solid.png' % (condition)

# experiment trial variable enumerated types
cue_types = ['dashed', 'solid']
shape_types = ['square', 'triangle']
shape_colors = ['blue', 'yellow']

# mapping of subject condition number to counter balanced experiment settings for
# cues and expected correct responses
# NOTE: should we try and move these two tables/dicts into an external csv file and
# load it instead of having it hardcoded in the psycopy code?
counter_balancing = {
    #    posture     cueSolid cueDashed colorLeft colorRight shapeLeft  shapeRight
     1: ['standing', 'color', 'shape', 'blue',   'yellow', 'triangle', 'square'],
     2: ['standing', 'color', 'shape', 'blue',   'yellow', 'square',   'triangle'],
     3: ['standing', 'color', 'shape', 'yellow', 'blue',   'triangle', 'square'],
     4: ['standing', 'color', 'shape', 'yellow', 'blue',   'square',   'triangle'],

     5: ['standing', 'shape', 'color', 'blue',   'yellow', 'triangle', 'square'],
     6: ['standing', 'shape', 'color', 'blue',   'yellow', 'square',   'triangle'],
     7: ['standing', 'shape', 'color', 'yellow', 'blue',   'triangle', 'square'],
     8: ['standing', 'shape', 'color', 'yellow', 'blue',   'square',   'triangle'],

     9: ['sitting',  'color', 'shape', 'blue',   'yellow', 'triangle', 'square'],
    10: ['sitting',  'color', 'shape', 'blue',   'yellow', 'square',   'triangle'],
    11: ['sitting',  'color', 'shape', 'yellow', 'blue',   'triangle', 'square'],
    12: ['sitting',  'color', 'shape', 'yellow', 'blue',   'square',   'triangle'],

    13: ['sitting',  'shape', 'color', 'blue',   'yellow', 'triangle', 'square'],
    14: ['sitting',  'shape', 'color', 'blue',   'yellow', 'square',   'triangle'],
    15: ['sitting',  'shape', 'color', 'yellow', 'blue',   'triangle', 'square'],
    16: ['sitting',  'shape', 'color', 'yellow', 'blue',   'square',   'triangle'],
}

# given selected subject condition, determine experiment variables and settings being
# used
posture, cueSolid, cueDashed, colorLeft, colorRight, shapeLeft, shapeRight = counter_balancing[condition]

# mapping of subject counter balanced conditions to expected correct button
# press, 1 for left and 2 for right.  Used explicitly when creating randomized
# trials to correctly set all trial variables for current subject condition
subject_condition_responses = {
    # condition 1, dashed=shape, solid=color
    (1, 'dashed', 'yellow', 'triangle'): 1,
    (1, 'dashed', 'yellow', 'square'): 2,
    (1, 'dashed', 'blue',   'triangle'): 1,
    (1, 'dashed', 'blue',   'square'): 2,
    (1, 'solid',  'yellow', 'triangle'): 2,
    (1, 'solid',  'yellow', 'square'): 2,
    (1, 'solid',  'blue',   'triangle'): 1,
    (1, 'solid',  'blue',   'square'): 1,

    # condition 2, dashed=shape, solid=color
    (2, 'dashed', 'yellow', 'triangle'): 2,
    (2, 'dashed', 'yellow', 'square'): 1,
    (2, 'dashed', 'blue',   'triangle'): 2,
    (2, 'dashed', 'blue',   'square'): 1,
    (2, 'solid',  'yellow', 'triangle'): 2,
    (2, 'solid',  'yellow', 'square'): 2,
    (2, 'solid',  'blue',   'triangle'): 1,
    (2, 'solid',  'blue',   'square'): 1,

    # condition 3, dashed=shape, solid=color
    (3, 'dashed', 'yellow', 'triangle'): 1,
    (3, 'dashed', 'yellow', 'square'): 2,
    (3, 'dashed', 'blue',   'triangle'): 1,
    (3, 'dashed', 'blue',   'square'): 2,
    (3, 'solid',  'yellow', 'triangle'): 1,
    (3, 'solid',  'yellow', 'square'): 1,
    (3, 'solid',  'blue',   'triangle'): 2,
    (3, 'solid',  'blue',   'square'): 2,

    # condition 4, dashed=shape, solid=color
    (4, 'dashed', 'yellow', 'triangle'): 2,
    (4, 'dashed', 'yellow', 'square'): 1,
    (4, 'dashed', 'blue',   'triangle'): 2,
    (4, 'dashed', 'blue',   'square'): 1,
    (4, 'solid',  'yellow', 'triangle'): 1,
    (4, 'solid',  'yellow', 'square'): 1,
    (4, 'solid',  'blue',   'triangle'): 2,
    (4, 'solid',  'blue',   'square'): 2,

    # condition 5, dashed=color, solid=shape
    (5, 'dashed', 'yellow', 'triangle'): 2,
    (5, 'dashed', 'yellow', 'square'): 2,
    (5, 'dashed', 'blue',   'triangle'): 1,
    (5, 'dashed', 'blue',   'square'): 1,
    (5, 'solid',  'yellow', 'triangle'): 1,
    (5, 'solid',  'yellow', 'square'): 2,
    (5, 'solid',  'blue',   'triangle'): 1,
    (5, 'solid',  'blue',   'square'): 2,

    # condition 6, dashed=color, solid=shape
    (6, 'dashed', 'yellow', 'triangle'): 2,
    (6, 'dashed', 'yellow', 'square'): 2,
    (6, 'dashed', 'blue',   'triangle'): 1,
    (6, 'dashed', 'blue',   'square'): 1,
    (6, 'solid',  'yellow', 'triangle'): 2,
    (6, 'solid',  'yellow', 'square'): 1,
    (6, 'solid',  'blue',   'triangle'): 2,
    (6, 'solid',  'blue',   'square'): 1,

    # condition 7, dashed=color, solid=shape
    (7, 'dashed', 'yellow', 'triangle'): 1,
    (7, 'dashed', 'yellow', 'square'): 1,
    (7, 'dashed', 'blue',   'triangle'): 2,
    (7, 'dashed', 'blue',   'square'): 2,
    (7, 'solid',  'yellow', 'triangle'): 1,
    (7, 'solid',  'yellow', 'square'): 2,
    (7, 'solid',  'blue',   'triangle'): 1,
    (7, 'solid',  'blue',   'square'): 2,

    # condition 8, dashed=color, solid=shape
    (8, 'dashed', 'yellow', 'triangle'): 1,
    (8, 'dashed', 'yellow', 'square'): 1,
    (8, 'dashed', 'blue',   'triangle'): 2,
    (8, 'dashed', 'blue',   'square'): 2,
    (8, 'solid',  'yellow', 'triangle'): 2,
    (8, 'solid',  'yellow', 'square'): 1,
    (8, 'solid',  'blue',   'triangle'): 2,
    (8, 'solid',  'blue',   'square'): 1,

    # condition 9, dashed=shape, solid=color
    (9, 'dashed', 'yellow', 'triangle'): 1,
    (9, 'dashed', 'yellow', 'square'): 2,
    (9, 'dashed', 'blue',   'triangle'): 1,
    (9, 'dashed', 'blue',   'square'): 2,
    (9, 'solid',  'yellow', 'triangle'): 2,
    (9, 'solid',  'yellow', 'square'): 2,
    (9, 'solid',  'blue',   'triangle'): 1,
    (9, 'solid',  'blue',   'square'): 1,

    # condition 10, dashed=shape, solid=color
    (10, 'dashed', 'yellow', 'triangle'): 2,
    (10, 'dashed', 'yellow', 'square'): 1,
    (10, 'dashed', 'blue',   'triangle'): 2,
    (10, 'dashed', 'blue',   'square'): 1,
    (10, 'solid',  'yellow', 'triangle'): 2,
    (10, 'solid',  'yellow', 'square'): 2,
    (10, 'solid',  'blue',   'triangle'): 1,
    (10, 'solid',  'blue',   'square'): 1,

    # condition 11, dashed=shape, solid=color
    (11, 'dashed', 'yellow', 'triangle'): 1,
    (11, 'dashed', 'yellow', 'square'): 2,
    (11, 'dashed', 'blue',   'triangle'): 1,
    (11, 'dashed', 'blue',   'square'): 2,
    (11, 'solid',  'yellow', 'triangle'): 1,
    (11, 'solid',  'yellow', 'square'): 1,
    (11, 'solid',  'blue',   'triangle'): 2,
    (11, 'solid',  'blue',   'square'): 2,

    # condition 12, dashed=shape, solid=color
    (12, 'dashed', 'yellow', 'triangle'): 2,
    (12, 'dashed', 'yellow', 'square'): 1,
    (12, 'dashed', 'blue',   'triangle'): 2,
    (12, 'dashed', 'blue',   'square'): 1,
    (12, 'solid',  'yellow', 'triangle'): 1,
    (12, 'solid',  'yellow', 'square'): 1,
    (12, 'solid',  'blue',   'triangle'): 2,
    (12, 'solid',  'blue',   'square'): 2,

    # condition 13, dashed=color, solid=shape
    (13, 'dashed', 'yellow', 'triangle'): 2,
    (13, 'dashed', 'yellow', 'square'): 2,
    (13, 'dashed', 'blue',   'triangle'): 1,
    (13, 'dashed', 'blue',   'square'): 1,
    (13, 'solid',  'yellow', 'triangle'): 1,
    (13, 'solid',  'yellow', 'square'): 2,
    (13, 'solid',  'blue',   'triangle'): 1,
    (13, 'solid',  'blue',   'square'): 2,

    # condition 14, dashed=color, solid=shape
    (14, 'dashed', 'yellow', 'triangle'): 2,
    (14, 'dashed', 'yellow', 'square'): 2,
    (14, 'dashed', 'blue',   'triangle'): 1,
    (14, 'dashed', 'blue',   'square'): 1,
    (14, 'solid',  'yellow', 'triangle'): 2,
    (14, 'solid',  'yellow', 'square'): 1,
    (14, 'solid',  'blue',   'triangle'): 2,
    (14, 'solid',  'blue',   'square'): 1,

    # condition 15, dashed=color, solid=shape
    (15, 'dashed', 'yellow', 'triangle'): 1,
    (15, 'dashed', 'yellow', 'square'): 1,
    (15, 'dashed', 'blue',   'triangle'): 2,
    (15, 'dashed', 'blue',   'square'): 2,
    (15, 'solid',  'yellow', 'triangle'): 1,
    (15, 'solid',  'yellow', 'square'): 2,
    (15, 'solid',  'blue',   'triangle'): 1,
    (15, 'solid',  'blue',   'square'): 2,

    # condition 16, dashed=color, solid=shape
    (16, 'dashed', 'yellow', 'triangle'): 1,
    (16, 'dashed', 'yellow', 'square'): 1,
    (16, 'dashed', 'blue',   'triangle'): 2,
    (16, 'dashed', 'blue',   'square'): 2,
    (16, 'solid',  'yellow', 'triangle'): 2,
    (16, 'solid',  'yellow', 'square'): 1,
    (16, 'solid',  'blue',   'triangle'): 2,
    (16, 'solid',  'blue',   'square'): 1,
}

def determine_expected_response(condition, trial):
    """
    Given subject condition and the trial variables (cue, shape and color), determine
    correct response.  We basically use a lookup table / dictionary
    to map from these to expected correct response.  The lookup table could (should?)
    be moved to a file that is read in on experiment startup.
    """
    response = 0
    cue_type, shape_type, shape_color = trial
    response = subject_condition_responses[(condition, cue_type, shape_color, shape_type)]

    # it is an error if response is still 0, should probably
    # stop or throw an exception to be defensive
    return response


def is_balanced(trials):
    """
    Return true if both switch/noswitch and congruant/incongruant
    are balanced, false otherwise.

    NOTE: this method always assumes there is a first buffer
    trial which is ignored when determining balance
    """
    return is_switch_balanced(trials) and is_congruant_balanced(trials)


def is_switch_balanced(trials):
    """
    Return true if switch/noswitch are balanced, false if not.
    """
    switch_count = 0
    for _, _, _, _, _, switch_type, *_ in trials:
        if switch_type == 'switch':
            switch_count += 1

    num_trials = len(trials) - 1
    half_trials = num_trials // 2
    
    #print('is_switch_balanced %d switched out of %d trials' % (switch_count, num_trials))
    return switch_count == half_trials

        
def is_congruant_balanced(trials):
    """
    Return true if congruant/incongruant are balanced, false if not.
    """
    congruant_count = 0
    for _, _, _, _, _, _, congruant_type, *_ in trials:
        if congruant_type == 'congruant':
            congruant_count += 1

    num_trials = len(trials) - 1
    half_trials = num_trials // 2
    
    #print('is_congruant_balanced %d congruant out of %d trials' % (congruant_count, num_trials))
    return congruant_count == half_trials


def random_trials(block_num, trial_type, condition, posture, num_trials, add_buffer_trial=False):
    """
    Create the indicated number of trials and shuffle them
    randomly.  Return result as a list of the trial variables.

    The add_buffer_trial flag determines if a random initial trial is
    added to the beginning of the trial sequence.  Normally we systematically
    use the trial variable combinations, repeating all possible combinations
    as many times as needed.  But when we are explicitly enforcing that
    trial blocks have equal switch/noswitch and congruant/incongruant, we need
    an initial buffer trial where switch and congruant are NA, this is not
    defined except in relation to a previous trial, so the initial trial is always
    NA with respect to switch/noswitch and congruant/incongruant
    """
    
    # create list of 8 basic trial variable combinations
    vars = [cue_types, shape_types, shape_colors]
    base_trials = list(itertools.product(*vars))
    num_base_trials = len(base_trials)

    # Repeat basic trial combinations whole number of times
    # that we can, then select some more combinations at random
    # to get exactly the asked for num_trials
    num_base_repeats = num_trials // num_base_trials
    num_remaining = num_trials % num_base_trials
    trial_list = base_trials * num_base_repeats
    trial_list += random.sample(base_trials, num_remaining)

    # now shuffle the trial_list randomly
    random.shuffle(trial_list)

    # if we are to add a buffer trial, choose one at random and prepend
    # it to the trial list
    if add_buffer_trial:
        trial = random.choice(base_trials)
        trial_list = [trial] + trial_list
        num_trials += 1
        
    # collect trial variables as a list of trials to return
    trials = []

    # rest of trials, determine switch and congruant from previous
    for trial_num in range(0, num_trials):
        cue_type, shape_type, shape_color = trial_list[trial_num]
        current_response = determine_expected_response(condition, trial_list[trial_num])

        # first trial is a buffer
        # if no previous, then switch and congrunt are not applicable to this trial
        if trial_num == 0:
            switch_type = 'buffer'
            congruant_type = 'buffer'
        # otherwise determine switch and congruant for this trial based on previous trial
        else:
            prev_cue_type, prev_shape_type, prev_shape_color = trial_list[trial_num - 1]

            # determine if switch or noswitch
            if cue_type == prev_cue_type:
                switch_type = 'noswitch'
            else:
                switch_type = 'switch'

            # determine if congruant or not congruant, this is more complicated, it depends
            # on the expected response of previous trial and the response of current trial
            if current_response == prev_response:
                congruant_type = 'congruant'
            else:
                congruant_type = 'incongruant'

        # remember the previous response for next iteration to determine congruant / incongruant
        prev_response = current_response
        
        trials.append( (block_num, trial_num + 1, trial_type, condition, posture, switch_type, congruant_type, cue_type, shape_type, shape_color, current_response) )

    # return the resulting constructed and randomly shuffled list of trials
    return trials


def counter_balanced_trials(block_num, trial_type, condition, posture, num_trials):
    """
    We brute force solution here.  Generate random trials
    with a buffer trial before the requested num_trials, then
    test to see if resulting random shuffle of trials is balanced
    or not.  Usually should take no more than 100 random generations
    to find a trial that is both balanced by switch/noswitch and
    congruant/incongruant
    """
    # get an initial set of random trials
    MAX_ATTEMPTS = 1000
    trials = random_trials(block_num, trial_type, condition, posture, num_trials, True)

    # keep generating random trials of the requested size until
    # we find a balanced one, or until we reach some maximum
    # attempts, in which case something may be wrong
    num_attempts = 1
    while not is_balanced(trials) and num_attempts <= MAX_ATTEMPTS:
        trials = random_trials(block_num, trial_type, condition, posture, num_trials, True)
        num_attempts += 1

    # sanity check, make sure we found a balanced trial
    if not is_balanced(trials):
        print("<counter_balanced_trials> Error: could not achieve block balance in %d attempts, aborting" % (MAX_ATTEMPTS))
        sys.exit(1)
        
    # at this point we should have found a balanced trial
    return trials
                    

def trials_to_csv(filename, trials):
    """
    Given a list of trials (which constitutes a single block of trials usually
    for the experiment), save the block trial list to a comma seperated values (csv)
    file.  This file can be loaded by Psychopy for an experiment block of trials.
    """
    f = open(filename, 'w')
    
    # file header
    f.write("blockNum,trialNum,trialType,condition,posture,switchTrialType,congruantTrialType,cueType,shapeType,shapeColor,cueFileName,stimuliFileName,correctAnswer\n")

    # loop to generate trial settings/variables
    for block_num, trial_num, trial_type, condition, posture, switch_type, congruant_type, cue_type, shape_type, shape_color, correct_response in trials:
        # file names for cue/stimuli to use for this trial
        cue_filename = 'stimuli/%s-rectangle.png' % (cue_type)
        stimuli_filename = 'stimuli/%s-%s.png' % (shape_color, shape_type)

        # output this trial
        f.write('%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d\n' %
              (block_num, trial_num, trial_type, condition, posture, switch_type, congruant_type, cue_type, shape_type, shape_color, cue_filename, stimuli_filename, correct_response))

    f.close()


def trials_to_triallist(trials):
    """
    Return a list of dictionaries, where keys are the trial feature/variable names.  Can be used
    directly in Psychopy code instead of saving to a csv file then loading the file for a
    block of trials.
    """
    trial_list = []
    
    # loop to generate trial settings/variables
    for block_num, trial_num, trial_type, condition, posture, switch_type, congruant_type, cue_type, shape_type, shape_color, correct_response in trials:
        # file names for cue/stimuli to use for this trial
        cue_filename = 'stimuli/%s-rectangle.png' % (cue_type)
        stimuli_filename = 'stimuli/%s-%s.png' % (shape_color, shape_type)

        trial_dict = {
            'blockNum': block_num,
            'trialNum': trial_num,
            'trialType': trial_type,
            'condition': condition,
            'posture': posture,
            'switchTrialType': switch_type,
            'congruantTrialType': congruant_type,
            'cueType': cue_type,
            'shapeType': shape_type,
            'shapeColor': shape_color,
            'cueFileName': cue_filename,
            'stimuliFileName': stimuli_filename,
            'correctAnswer': correct_response,
        }

        trial_list.append(trial_dict)

    return trial_list




# Initialize components for Routine "PostureInstruction"
PostureInstructionClock = core.Clock()
postureTrial = 0

numCorrectTrials = 0
totalTrialsAttempted = 0
reactionTimeSum = 0.0
totalTrialsReactedSuccessfully = 0
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction01"
UntimedInstruction01Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image=untimedInstruction01, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction02"
UntimedInstruction02Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image=untimedInstruction02, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction03"
UntimedInstruction03Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image=untimedInstruction03, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction04"
UntimedInstruction04Clock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image=untimedInstruction04, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction05"
UntimedInstruction05Clock = core.Clock()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image=untimedInstruction05, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction06"
UntimedInstruction06Clock = core.Clock()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image=untimedInstruction06, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction07"
UntimedInstruction07Clock = core.Clock()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image=untimedInstruction07, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "UntimedInstruction08"
UntimedInstruction08Clock = core.Clock()
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image=untimedInstruction08, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "InitializeUntimed"
InitializeUntimedClock = core.Clock()

# Initialize components for Routine "UntimedTrial"
UntimedTrialClock = core.Clock()
cue_untimed_image = visual.ImageStim(
    win=win,
    name='cue_untimed_image', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(30.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimuli_untimed_image = visual.ImageStim(
    win=win,
    name='stimuli_untimed_image', units='cm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(15.0, 15.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
untimed_resp = keyboard.Keyboard()

# Initialize components for Routine "DetermineUntimedFeedback"
DetermineUntimedFeedbackClock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "SolidFeedback"
SolidFeedbackClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image=errorInstructionSolid, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "DashedFeedback"
DashedFeedbackClock = core.Clock()
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image=errorInstructionDashed, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Delay"
DelayClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TimedInstruction01"
TimedInstruction01Clock = core.Clock()
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image=timedInstruction01, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "TimedInstruction02"
TimedInstruction02Clock = core.Clock()
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image=timedInstruction02, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "InitializeTimed"
InitializeTimedClock = core.Clock()

# Initialize components for Routine "TimedTrial"
TimedTrialClock = core.Clock()
cue_timed_image = visual.ImageStim(
    win=win,
    name='cue_timed_image', units='deg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(25.0, 25.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimuli_timed_image = visual.ImageStim(
    win=win,
    name='stimuli_timed_image', units='deg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(12.0, 12.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
timed_resp = keyboard.Keyboard()

# Initialize components for Routine "DetermineTimedFeedback"
DetermineTimedFeedbackClock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "SolidFeedback"
SolidFeedbackClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image=errorInstructionSolid, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "DashedFeedback"
DashedFeedbackClock = core.Clock()
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image=errorInstructionDashed, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Delay"
DelayClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PostureInstruction"
PostureInstructionClock = core.Clock()
postureTrial = 0

numCorrectTrials = 0
totalTrialsAttempted = 0
reactionTimeSum = 0.0
totalTrialsReactedSuccessfully = 0
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ExpInstruction01"
ExpInstruction01Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image=expInstruction01, mask=None,
    ori=0.0, pos=(0, 0), size=(53.0, 30.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_response = keyboard.Keyboard()

# Initialize components for Routine "ExpInstructionBlock"
ExpInstructionBlockClock = core.Clock()
blockNumber = 0
blockText = ""
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "InitializeBlock"
InitializeBlockClock = core.Clock()

# Initialize components for Routine "ExpTrial"
ExpTrialClock = core.Clock()
cue_image = visual.ImageStim(
    win=win,
    name='cue_image', units='deg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(25.0, 25.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stimuli_image = visual.ImageStim(
    win=win,
    name='stimuli_image', units='deg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(12.0, 12.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
exp_resp = keyboard.Keyboard()

# Initialize components for Routine "DetermineExpFeedback"
DetermineExpFeedbackClock = core.Clock()
selectCorrect = 0
selectIncorrectSolid = 0
selectIncorrectDashed= 0

# Initialize components for Routine "SolidFeedback"
SolidFeedbackClock = core.Clock()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image=errorInstructionSolid, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "DashedFeedback"
DashedFeedbackClock = core.Clock()
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image=errorInstructionDashed, mask=None,
    ori=0.0, pos=(0, 0), size=(53, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Delay"
DelayClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Results"
ResultsClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initialize"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InitializeComponents = []
for thisComponent in InitializeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitializeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Initialize"-------
while continueRoutine:
    # get current time
    t = InitializeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitializeClock)
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
    for thisComponent in InitializeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initialize"-------
for thisComponent in InitializeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Initialize" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PostureInstruction"-------
continueRoutine = True
# update component parameters for each repeat
# move to next posture if needed,
# this will switch the posture after each
# set of numBlocks is completed.
if postureTrial >= 2:
    blockNumber = 0
    if posture == 'standing':
        posture = 'sitting'
    elif posture == 'sitting':
        posture = 'standing'

# set up instructions for this posture
postureInstructions = """
You will be performing this experiment in
two separate postures.

At this time you should be in the
`%s` posture

Please have the experimenter help you
get yourself into position for this
portion of the experiment. 

Press any button when you are ready to continue.
""" % (posture)

# set up for next posture iteration
postureTrial += 1
text_3.setText(postureInstructions)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
PostureInstructionComponents = [text_3, key_resp_2]
for thisComponent in PostureInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PostureInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PostureInstruction"-------
while continueRoutine:
    # get current time
    t = PostureInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PostureInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PostureInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PostureInstruction"-------
for thisComponent in PostureInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "PostureInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction01"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
UntimedInstruction01Components = [image_4, key_resp_4]
for thisComponent in UntimedInstruction01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction01"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction01"-------
for thisComponent in UntimedInstruction01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction02"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
UntimedInstruction02Components = [image_5, key_resp_5]
for thisComponent in UntimedInstruction02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction02"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['1'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction02"-------
for thisComponent in UntimedInstruction02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction03"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
UntimedInstruction03Components = [image_6, key_resp_6]
for thisComponent in UntimedInstruction03Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction03Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction03"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction03Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction03Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['2'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction03"-------
for thisComponent in UntimedInstruction03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction04"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
UntimedInstruction04Components = [image_7, key_resp_7]
for thisComponent in UntimedInstruction04Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction04Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction04"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction04Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction04Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction04Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction04"-------
for thisComponent in UntimedInstruction04Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction04" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction05"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
UntimedInstruction05Components = [image_8, key_resp_8]
for thisComponent in UntimedInstruction05Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction05Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction05"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction05Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction05Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['1'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction05Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction05"-------
for thisComponent in UntimedInstruction05Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction05" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction06"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
UntimedInstruction06Components = [image_9, key_resp_9]
for thisComponent in UntimedInstruction06Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction06Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction06"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction06Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction06Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['2'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction06Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction06"-------
for thisComponent in UntimedInstruction06Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction06" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction07"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
UntimedInstruction07Components = [image_10, key_resp_10]
for thisComponent in UntimedInstruction07Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction07Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction07"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction07Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction07Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction07Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction07"-------
for thisComponent in UntimedInstruction07Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction07" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UntimedInstruction08"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
UntimedInstruction08Components = [image_11, key_resp_11]
for thisComponent in UntimedInstruction08Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UntimedInstruction08Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UntimedInstruction08"-------
while continueRoutine:
    # get current time
    t = UntimedInstruction08Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UntimedInstruction08Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UntimedInstruction08Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UntimedInstruction08"-------
for thisComponent in UntimedInstruction08Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
# the Routine "UntimedInstruction08" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InitializeUntimed"-------
continueRoutine = True
# update component parameters for each repeat
untimedNum = 1
blockNum = 1
trialType = 'untimed'
thisUntimedTrials = random_trials(blockNum, trialType, condition, posture, numTrialsUntimed)
thisUntimedFileName = '../data/%s_%s_%s-untimed-%02d-trials.csv' % (expInfo['participant'], expName, expInfo['date'], untimedNum)
trials_to_csv(thisUntimedFileName, thisUntimedTrials)
# keep track of which components have finished
InitializeUntimedComponents = []
for thisComponent in InitializeUntimedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitializeUntimedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InitializeUntimed"-------
while continueRoutine:
    # get current time
    t = InitializeUntimedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitializeUntimedClock)
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
    for thisComponent in InitializeUntimedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InitializeUntimed"-------
for thisComponent in InitializeUntimedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "InitializeUntimed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
untimedTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(thisUntimedFileName),
    seed=None, name='untimedTrials')
thisExp.addLoop(untimedTrials)  # add the loop to the experiment
thisUntimedTrial = untimedTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisUntimedTrial.rgb)
if thisUntimedTrial != None:
    for paramName in thisUntimedTrial:
        exec('{} = thisUntimedTrial[paramName]'.format(paramName))

for thisUntimedTrial in untimedTrials:
    currentLoop = untimedTrials
    # abbreviate parameter names if possible (e.g. rgb = thisUntimedTrial.rgb)
    if thisUntimedTrial != None:
        for paramName in thisUntimedTrial:
            exec('{} = thisUntimedTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "UntimedTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_untimed_image.setImage(cueFileName)
    stimuli_untimed_image.setImage(stimuliFileName)
    untimed_resp.keys = []
    untimed_resp.rt = []
    _untimed_resp_allKeys = []
    # keep track of which components have finished
    UntimedTrialComponents = [cue_untimed_image, stimuli_untimed_image, untimed_resp]
    for thisComponent in UntimedTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    UntimedTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "UntimedTrial"-------
    while continueRoutine:
        # get current time
        t = UntimedTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=UntimedTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_untimed_image* updates
        if cue_untimed_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_untimed_image.frameNStart = frameN  # exact frame index
            cue_untimed_image.tStart = t  # local t and not account for scr refresh
            cue_untimed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_untimed_image, 'tStartRefresh')  # time at next scr refresh
            cue_untimed_image.setAutoDraw(True)
        
        # *stimuli_untimed_image* updates
        if stimuli_untimed_image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_untimed_image.frameNStart = frameN  # exact frame index
            stimuli_untimed_image.tStart = t  # local t and not account for scr refresh
            stimuli_untimed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_untimed_image, 'tStartRefresh')  # time at next scr refresh
            stimuli_untimed_image.setAutoDraw(True)
        
        # *untimed_resp* updates
        waitOnFlip = False
        if untimed_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            untimed_resp.frameNStart = frameN  # exact frame index
            untimed_resp.tStart = t  # local t and not account for scr refresh
            untimed_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(untimed_resp, 'tStartRefresh')  # time at next scr refresh
            untimed_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(untimed_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(untimed_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if untimed_resp.status == STARTED and not waitOnFlip:
            theseKeys = untimed_resp.getKeys(keyList=['1', '2'], waitRelease=False)
            _untimed_resp_allKeys.extend(theseKeys)
            if len(_untimed_resp_allKeys):
                untimed_resp.keys = _untimed_resp_allKeys[-1].name  # just the last key pressed
                untimed_resp.rt = _untimed_resp_allKeys[-1].rt
                # was this correct?
                if (untimed_resp.keys == str(correctAnswer)) or (untimed_resp.keys == correctAnswer):
                    untimed_resp.corr = 1
                else:
                    untimed_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        if True:
            untimedTrials.addData("utcTime", time.time())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in UntimedTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "UntimedTrial"-------
    for thisComponent in UntimedTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    untimedTrials.addData('cue_untimed_image.started', cue_untimed_image.tStartRefresh)
    untimedTrials.addData('cue_untimed_image.stopped', cue_untimed_image.tStopRefresh)
    untimedTrials.addData('stimuli_untimed_image.started', stimuli_untimed_image.tStartRefresh)
    untimedTrials.addData('stimuli_untimed_image.stopped', stimuli_untimed_image.tStopRefresh)
    # check responses
    if untimed_resp.keys in ['', [], None]:  # No response was made
        untimed_resp.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           untimed_resp.corr = 1;  # correct non-response
        else:
           untimed_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for untimedTrials (TrialHandler)
    untimedTrials.addData('untimed_resp.keys',untimed_resp.keys)
    untimedTrials.addData('untimed_resp.corr', untimed_resp.corr)
    if untimed_resp.keys != None:  # we had a response
        untimedTrials.addData('untimed_resp.rt', untimed_resp.rt)
    untimedTrials.addData('untimed_resp.started', untimed_resp.tStartRefresh)
    untimedTrials.addData('untimed_resp.stopped', untimed_resp.tStopRefresh)
    # the Routine "UntimedTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "DetermineUntimedFeedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if untimed_resp.corr == 1:
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
    DetermineUntimedFeedbackComponents = []
    for thisComponent in DetermineUntimedFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DetermineUntimedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DetermineUntimedFeedback"-------
    while continueRoutine:
        # get current time
        t = DetermineUntimedFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DetermineUntimedFeedbackClock)
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
        for thisComponent in DetermineUntimedFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DetermineUntimedFeedback"-------
    for thisComponent in DetermineUntimedFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "DetermineUntimedFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    selectSolid1 = data.TrialHandler(nReps=selectIncorrectSolid, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='selectSolid1')
    thisExp.addLoop(selectSolid1)  # add the loop to the experiment
    thisSelectSolid1 = selectSolid1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid1.rgb)
    if thisSelectSolid1 != None:
        for paramName in thisSelectSolid1:
            exec('{} = thisSelectSolid1[paramName]'.format(paramName))
    
    for thisSelectSolid1 in selectSolid1:
        currentLoop = selectSolid1
        # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid1.rgb)
        if thisSelectSolid1 != None:
            for paramName in thisSelectSolid1:
                exec('{} = thisSelectSolid1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SolidFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_1.setSound('A', secs=1.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        SolidFeedbackComponents = [sound_1, image_2]
        for thisComponent in SolidFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SolidFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SolidFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SolidFeedbackClock)
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
                if tThisFlipGlobal > image_2.tStartRefresh + 5.0-frameTolerance:
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
            for thisComponent in SolidFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SolidFeedback"-------
        for thisComponent in SolidFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        selectSolid1.addData('sound_1.started', sound_1.tStartRefresh)
        selectSolid1.addData('sound_1.stopped', sound_1.tStopRefresh)
        selectSolid1.addData('image_2.started', image_2.tStartRefresh)
        selectSolid1.addData('image_2.stopped', image_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectSolid repeats of 'selectSolid1'
    
    
    # set up handler to look after randomisation of conditions etc
    selectDashed1 = data.TrialHandler(nReps=selectIncorrectDashed, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='selectDashed1')
    thisExp.addLoop(selectDashed1)  # add the loop to the experiment
    thisSelectDashed1 = selectDashed1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed1.rgb)
    if thisSelectDashed1 != None:
        for paramName in thisSelectDashed1:
            exec('{} = thisSelectDashed1[paramName]'.format(paramName))
    
    for thisSelectDashed1 in selectDashed1:
        currentLoop = selectDashed1
        # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed1.rgb)
        if thisSelectDashed1 != None:
            for paramName in thisSelectDashed1:
                exec('{} = thisSelectDashed1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "DashedFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_2.setSound('A', secs=1.0, hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        DashedFeedbackComponents = [sound_2, image_3]
        for thisComponent in DashedFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        DashedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "DashedFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = DashedFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=DashedFeedbackClock)
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
                if tThisFlipGlobal > image_3.tStartRefresh + 5.0-frameTolerance:
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
            for thisComponent in DashedFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "DashedFeedback"-------
        for thisComponent in DashedFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_2.stop()  # ensure sound has stopped at end of routine
        selectDashed1.addData('sound_2.started', sound_2.tStartRefresh)
        selectDashed1.addData('sound_2.stopped', sound_2.tStopRefresh)
        selectDashed1.addData('image_3.started', image_3.tStartRefresh)
        selectDashed1.addData('image_3.stopped', image_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectDashed repeats of 'selectDashed1'
    
    
    # ------Prepare to start Routine "Delay"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DelayComponents = [text_2]
    for thisComponent in DelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Delay"-------
    for thisComponent in DelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    untimedTrials.addData('text_2.started', text_2.tStartRefresh)
    untimedTrials.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'untimedTrials'


# ------Prepare to start Routine "TimedInstruction01"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
TimedInstruction01Components = [image_12, key_resp_12]
for thisComponent in TimedInstruction01Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TimedInstruction01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TimedInstruction01"-------
while continueRoutine:
    # get current time
    t = TimedInstruction01Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TimedInstruction01Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TimedInstruction01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TimedInstruction01"-------
for thisComponent in TimedInstruction01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_12.started', image_12.tStartRefresh)
thisExp.addData('image_12.stopped', image_12.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "TimedInstruction01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TimedInstruction02"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
TimedInstruction02Components = [image_13, key_resp_13]
for thisComponent in TimedInstruction02Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TimedInstruction02Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TimedInstruction02"-------
while continueRoutine:
    # get current time
    t = TimedInstruction02Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TimedInstruction02Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_13* updates
    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        image_13.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TimedInstruction02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TimedInstruction02"-------
for thisComponent in TimedInstruction02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_13.started', image_13.tStartRefresh)
thisExp.addData('image_13.stopped', image_13.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "TimedInstruction02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InitializeTimed"-------
continueRoutine = True
# update component parameters for each repeat
timedNum = 1
blockNum = 1
trialType = 'timed'
thisTimedTrials = random_trials(blockNum, trialType, condition, posture, numTrialsTimed)
thisTimedFileName = '../data/%s_%s_%s-timed-%02d-trials.csv' % (expInfo['participant'], expName, expInfo['date'], timedNum)
trials_to_csv(thisTimedFileName, thisTimedTrials)
# keep track of which components have finished
InitializeTimedComponents = []
for thisComponent in InitializeTimedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InitializeTimedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InitializeTimed"-------
while continueRoutine:
    # get current time
    t = InitializeTimedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InitializeTimedClock)
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
    for thisComponent in InitializeTimedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InitializeTimed"-------
for thisComponent in InitializeTimedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "InitializeTimed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
timedTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(thisTimedFileName),
    seed=None, name='timedTrials')
thisExp.addLoop(timedTrials)  # add the loop to the experiment
thisTimedTrial = timedTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTimedTrial.rgb)
if thisTimedTrial != None:
    for paramName in thisTimedTrial:
        exec('{} = thisTimedTrial[paramName]'.format(paramName))

for thisTimedTrial in timedTrials:
    currentLoop = timedTrials
    # abbreviate parameter names if possible (e.g. rgb = thisTimedTrial.rgb)
    if thisTimedTrial != None:
        for paramName in thisTimedTrial:
            exec('{} = thisTimedTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TimedTrial"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    cue_timed_image.setImage(cueFileName)
    stimuli_timed_image.setImage(stimuliFileName)
    timed_resp.keys = []
    timed_resp.rt = []
    _timed_resp_allKeys = []
    # keep track of which components have finished
    TimedTrialComponents = [cue_timed_image, stimuli_timed_image, timed_resp]
    for thisComponent in TimedTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TimedTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TimedTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TimedTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TimedTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_timed_image* updates
        if cue_timed_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_timed_image.frameNStart = frameN  # exact frame index
            cue_timed_image.tStart = t  # local t and not account for scr refresh
            cue_timed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_timed_image, 'tStartRefresh')  # time at next scr refresh
            cue_timed_image.setAutoDraw(True)
        if cue_timed_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_timed_image.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_timed_image.tStop = t  # not accounting for scr refresh
                cue_timed_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_timed_image, 'tStopRefresh')  # time at next scr refresh
                cue_timed_image.setAutoDraw(False)
        
        # *stimuli_timed_image* updates
        if stimuli_timed_image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_timed_image.frameNStart = frameN  # exact frame index
            stimuli_timed_image.tStart = t  # local t and not account for scr refresh
            stimuli_timed_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_timed_image, 'tStartRefresh')  # time at next scr refresh
            stimuli_timed_image.setAutoDraw(True)
        if stimuli_timed_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_timed_image.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_timed_image.tStop = t  # not accounting for scr refresh
                stimuli_timed_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_timed_image, 'tStopRefresh')  # time at next scr refresh
                stimuli_timed_image.setAutoDraw(False)
        
        # *timed_resp* updates
        waitOnFlip = False
        if timed_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            timed_resp.frameNStart = frameN  # exact frame index
            timed_resp.tStart = t  # local t and not account for scr refresh
            timed_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timed_resp, 'tStartRefresh')  # time at next scr refresh
            timed_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(timed_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(timed_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if timed_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timed_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                timed_resp.tStop = t  # not accounting for scr refresh
                timed_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timed_resp, 'tStopRefresh')  # time at next scr refresh
                timed_resp.status = FINISHED
        if timed_resp.status == STARTED and not waitOnFlip:
            theseKeys = timed_resp.getKeys(keyList=['1', '2'], waitRelease=False)
            _timed_resp_allKeys.extend(theseKeys)
            if len(_timed_resp_allKeys):
                timed_resp.keys = _timed_resp_allKeys[-1].name  # just the last key pressed
                timed_resp.rt = _timed_resp_allKeys[-1].rt
                # was this correct?
                if (timed_resp.keys == str(correctAnswer)) or (timed_resp.keys == correctAnswer):
                    timed_resp.corr = 1
                else:
                    timed_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        if True:
            timedTrials.addData("utcTime", time.time())
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TimedTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TimedTrial"-------
    for thisComponent in TimedTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    timedTrials.addData('cue_timed_image.started', cue_timed_image.tStartRefresh)
    timedTrials.addData('cue_timed_image.stopped', cue_timed_image.tStopRefresh)
    timedTrials.addData('stimuli_timed_image.started', stimuli_timed_image.tStartRefresh)
    timedTrials.addData('stimuli_timed_image.stopped', stimuli_timed_image.tStopRefresh)
    # check responses
    if timed_resp.keys in ['', [], None]:  # No response was made
        timed_resp.keys = None
        # was no response the correct answer?!
        if str(correctAnswer).lower() == 'none':
           timed_resp.corr = 1;  # correct non-response
        else:
           timed_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for timedTrials (TrialHandler)
    timedTrials.addData('timed_resp.keys',timed_resp.keys)
    timedTrials.addData('timed_resp.corr', timed_resp.corr)
    if timed_resp.keys != None:  # we had a response
        timedTrials.addData('timed_resp.rt', timed_resp.rt)
    timedTrials.addData('timed_resp.started', timed_resp.tStartRefresh)
    timedTrials.addData('timed_resp.stopped', timed_resp.tStopRefresh)
    
    # ------Prepare to start Routine "DetermineTimedFeedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if timed_resp.corr == 1:
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
    DetermineTimedFeedbackComponents = []
    for thisComponent in DetermineTimedFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DetermineTimedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "DetermineTimedFeedback"-------
    while continueRoutine:
        # get current time
        t = DetermineTimedFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DetermineTimedFeedbackClock)
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
        for thisComponent in DetermineTimedFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DetermineTimedFeedback"-------
    for thisComponent in DetermineTimedFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "DetermineTimedFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    selectSolid2 = data.TrialHandler(nReps=selectIncorrectSolid, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='selectSolid2')
    thisExp.addLoop(selectSolid2)  # add the loop to the experiment
    thisSelectSolid2 = selectSolid2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid2.rgb)
    if thisSelectSolid2 != None:
        for paramName in thisSelectSolid2:
            exec('{} = thisSelectSolid2[paramName]'.format(paramName))
    
    for thisSelectSolid2 in selectSolid2:
        currentLoop = selectSolid2
        # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid2.rgb)
        if thisSelectSolid2 != None:
            for paramName in thisSelectSolid2:
                exec('{} = thisSelectSolid2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SolidFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_1.setSound('A', secs=1.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        SolidFeedbackComponents = [sound_1, image_2]
        for thisComponent in SolidFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SolidFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SolidFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SolidFeedbackClock)
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
                if tThisFlipGlobal > image_2.tStartRefresh + 5.0-frameTolerance:
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
            for thisComponent in SolidFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SolidFeedback"-------
        for thisComponent in SolidFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        selectSolid2.addData('sound_1.started', sound_1.tStartRefresh)
        selectSolid2.addData('sound_1.stopped', sound_1.tStopRefresh)
        selectSolid2.addData('image_2.started', image_2.tStartRefresh)
        selectSolid2.addData('image_2.stopped', image_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectSolid repeats of 'selectSolid2'
    
    
    # set up handler to look after randomisation of conditions etc
    selectDashed2 = data.TrialHandler(nReps=selectIncorrectDashed, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='selectDashed2')
    thisExp.addLoop(selectDashed2)  # add the loop to the experiment
    thisSelectDashed2 = selectDashed2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed2.rgb)
    if thisSelectDashed2 != None:
        for paramName in thisSelectDashed2:
            exec('{} = thisSelectDashed2[paramName]'.format(paramName))
    
    for thisSelectDashed2 in selectDashed2:
        currentLoop = selectDashed2
        # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed2.rgb)
        if thisSelectDashed2 != None:
            for paramName in thisSelectDashed2:
                exec('{} = thisSelectDashed2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "DashedFeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        sound_2.setSound('A', secs=1.0, hamming=True)
        sound_2.setVolume(1.0, log=False)
        # keep track of which components have finished
        DashedFeedbackComponents = [sound_2, image_3]
        for thisComponent in DashedFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        DashedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "DashedFeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = DashedFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=DashedFeedbackClock)
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
                if tThisFlipGlobal > image_3.tStartRefresh + 5.0-frameTolerance:
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
            for thisComponent in DashedFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "DashedFeedback"-------
        for thisComponent in DashedFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_2.stop()  # ensure sound has stopped at end of routine
        selectDashed2.addData('sound_2.started', sound_2.tStartRefresh)
        selectDashed2.addData('sound_2.stopped', sound_2.tStopRefresh)
        selectDashed2.addData('image_3.started', image_3.tStartRefresh)
        selectDashed2.addData('image_3.stopped', image_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed selectIncorrectDashed repeats of 'selectDashed2'
    
    
    # ------Prepare to start Routine "Delay"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DelayComponents = [text_2]
    for thisComponent in DelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Delay"-------
    for thisComponent in DelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    timedTrials.addData('text_2.started', text_2.tStartRefresh)
    timedTrials.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'timedTrials'


# set up handler to look after randomisation of conditions etc
postures = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='postures')
thisExp.addLoop(postures)  # add the loop to the experiment
thisPosture = postures.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPosture.rgb)
if thisPosture != None:
    for paramName in thisPosture:
        exec('{} = thisPosture[paramName]'.format(paramName))

for thisPosture in postures:
    currentLoop = postures
    # abbreviate parameter names if possible (e.g. rgb = thisPosture.rgb)
    if thisPosture != None:
        for paramName in thisPosture:
            exec('{} = thisPosture[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PostureInstruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    # move to next posture if needed,
    # this will switch the posture after each
    # set of numBlocks is completed.
    if postureTrial >= 2:
        blockNumber = 0
        if posture == 'standing':
            posture = 'sitting'
        elif posture == 'sitting':
            posture = 'standing'
    
    # set up instructions for this posture
    postureInstructions = """
    You will be performing this experiment in
    two separate postures.
    
    At this time you should be in the
    `%s` posture
    
    Please have the experimenter help you
    get yourself into position for this
    portion of the experiment. 
    
    Press any button when you are ready to continue.
    """ % (posture)
    
    # set up for next posture iteration
    postureTrial += 1
    text_3.setText(postureInstructions)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    PostureInstructionComponents = [text_3, key_resp_2]
    for thisComponent in PostureInstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PostureInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PostureInstruction"-------
    while continueRoutine:
        # get current time
        t = PostureInstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PostureInstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1', '2'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PostureInstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PostureInstruction"-------
    for thisComponent in PostureInstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    postures.addData('text_3.started', text_3.tStartRefresh)
    postures.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    postures.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        postures.addData('key_resp_2.rt', key_resp_2.rt)
    postures.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    postures.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "PostureInstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=numBlocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ExpInstruction01"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_response.keys = []
        key_response.rt = []
        _key_response_allKeys = []
        # keep track of which components have finished
        ExpInstruction01Components = [image, key_response]
        for thisComponent in ExpInstruction01Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ExpInstruction01Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ExpInstruction01"-------
        while continueRoutine:
            # get current time
            t = ExpInstruction01Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ExpInstruction01Clock)
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
            
            # *key_response* updates
            waitOnFlip = False
            if key_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response.frameNStart = frameN  # exact frame index
                key_response.tStart = t  # local t and not account for scr refresh
                key_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
                key_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_response.status == STARTED and not waitOnFlip:
                theseKeys = key_response.getKeys(keyList=['1', '2'], waitRelease=False)
                _key_response_allKeys.extend(theseKeys)
                if len(_key_response_allKeys):
                    key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                    key_response.rt = _key_response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ExpInstruction01Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ExpInstruction01"-------
        for thisComponent in ExpInstruction01Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('image.started', image.tStartRefresh)
        blocks.addData('image.stopped', image.tStopRefresh)
        # check responses
        if key_response.keys in ['', [], None]:  # No response was made
            key_response.keys = None
        blocks.addData('key_response.keys',key_response.keys)
        if key_response.keys != None:  # we had a response
            blocks.addData('key_response.rt', key_response.rt)
        blocks.addData('key_response.started', key_response.tStartRefresh)
        blocks.addData('key_response.stopped', key_response.tStopRefresh)
        # the Routine "ExpInstruction01" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ExpInstructionBlock"-------
        continueRoutine = True
        # update component parameters for each repeat
        blockNumber += 1
        
        blockText = """
        Please check your posture and ensure you
        are still in the correct position.
        
        You should be in the '%s' posture for this
        block of the experiment.
        
        This is block %d of %d blocks
        
        
        
        Press any button to start the challenge""" % (posture, blockNumber, numBlocks)
        
        text.setText(blockText)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        ExpInstructionBlockComponents = [text, key_resp]
        for thisComponent in ExpInstructionBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ExpInstructionBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ExpInstructionBlock"-------
        while continueRoutine:
            # get current time
            t = ExpInstructionBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ExpInstructionBlockClock)
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
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1', '2'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ExpInstructionBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ExpInstructionBlock"-------
        for thisComponent in ExpInstructionBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('text.started', text.tStartRefresh)
        blocks.addData('text.stopped', text.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        blocks.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            blocks.addData('key_resp.rt', key_resp.rt)
        blocks.addData('key_resp.started', key_resp.tStartRefresh)
        blocks.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "ExpInstructionBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "InitializeBlock"-------
        continueRoutine = True
        # update component parameters for each repeat
        #blockNum = 1
        trialType = 'experiment'
        thisBlockTrials = counter_balanced_trials(blockNumber, trialType, condition, posture, numTrialsPerBlock)
        thisBlockFileName = '../data/%s_%s_%s-posture-%s-block-%02d-trials.csv' % (expInfo['participant'], expName, expInfo['date'], posture, blockNumber)
        trials_to_csv(thisBlockFileName, thisBlockTrials)
        # keep track of which components have finished
        InitializeBlockComponents = []
        for thisComponent in InitializeBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InitializeBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "InitializeBlock"-------
        while continueRoutine:
            # get current time
            t = InitializeBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InitializeBlockClock)
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
            for thisComponent in InitializeBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "InitializeBlock"-------
        for thisComponent in InitializeBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "InitializeBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(thisBlockFileName),
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
            
            # ------Prepare to start Routine "ExpTrial"-------
            continueRoutine = True
            routineTimer.add(2.500000)
            # update component parameters for each repeat
            cue_image.setImage(cueFileName)
            stimuli_image.setImage(stimuliFileName)
            exp_resp.keys = []
            exp_resp.rt = []
            _exp_resp_allKeys = []
            # keep track of which components have finished
            ExpTrialComponents = [cue_image, stimuli_image, exp_resp]
            for thisComponent in ExpTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ExpTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ExpTrial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ExpTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ExpTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cue_image* updates
                if cue_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cue_image.frameNStart = frameN  # exact frame index
                    cue_image.tStart = t  # local t and not account for scr refresh
                    cue_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_image, 'tStartRefresh')  # time at next scr refresh
                    cue_image.setAutoDraw(True)
                if cue_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cue_image.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        cue_image.tStop = t  # not accounting for scr refresh
                        cue_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(cue_image, 'tStopRefresh')  # time at next scr refresh
                        cue_image.setAutoDraw(False)
                
                # *stimuli_image* updates
                if stimuli_image.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimuli_image.frameNStart = frameN  # exact frame index
                    stimuli_image.tStart = t  # local t and not account for scr refresh
                    stimuli_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimuli_image, 'tStartRefresh')  # time at next scr refresh
                    stimuli_image.setAutoDraw(True)
                if stimuli_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimuli_image.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimuli_image.tStop = t  # not accounting for scr refresh
                        stimuli_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stimuli_image, 'tStopRefresh')  # time at next scr refresh
                        stimuli_image.setAutoDraw(False)
                
                # *exp_resp* updates
                waitOnFlip = False
                if exp_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    exp_resp.frameNStart = frameN  # exact frame index
                    exp_resp.tStart = t  # local t and not account for scr refresh
                    exp_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exp_resp, 'tStartRefresh')  # time at next scr refresh
                    exp_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(exp_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(exp_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if exp_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > exp_resp.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        exp_resp.tStop = t  # not accounting for scr refresh
                        exp_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(exp_resp, 'tStopRefresh')  # time at next scr refresh
                        exp_resp.status = FINISHED
                if exp_resp.status == STARTED and not waitOnFlip:
                    theseKeys = exp_resp.getKeys(keyList=['1', '2'], waitRelease=False)
                    _exp_resp_allKeys.extend(theseKeys)
                    if len(_exp_resp_allKeys):
                        exp_resp.keys = _exp_resp_allKeys[-1].name  # just the last key pressed
                        exp_resp.rt = _exp_resp_allKeys[-1].rt
                        # was this correct?
                        if (exp_resp.keys == str(correctAnswer)) or (exp_resp.keys == correctAnswer):
                            exp_resp.corr = 1
                        else:
                            exp_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                if True:
                    trials.addData("utcTime", time.time())
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ExpTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ExpTrial"-------
            for thisComponent in ExpTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('cue_image.started', cue_image.tStartRefresh)
            trials.addData('cue_image.stopped', cue_image.tStopRefresh)
            trials.addData('stimuli_image.started', stimuli_image.tStartRefresh)
            trials.addData('stimuli_image.stopped', stimuli_image.tStopRefresh)
            # check responses
            if exp_resp.keys in ['', [], None]:  # No response was made
                exp_resp.keys = None
                # was no response the correct answer?!
                if str(correctAnswer).lower() == 'none':
                   exp_resp.corr = 1;  # correct non-response
                else:
                   exp_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('exp_resp.keys',exp_resp.keys)
            trials.addData('exp_resp.corr', exp_resp.corr)
            if exp_resp.keys != None:  # we had a response
                trials.addData('exp_resp.rt', exp_resp.rt)
            trials.addData('exp_resp.started', exp_resp.tStartRefresh)
            trials.addData('exp_resp.stopped', exp_resp.tStopRefresh)
            
            # ------Prepare to start Routine "DetermineExpFeedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            totalTrialsAttempted += 1
            
            if type(exp_resp.rt) == float:
                reactionTimeSum += exp_resp.rt
                totalTrialsReactedSuccessfully += 1
                #print('rt:  %f, sum: %f, totalTrials: %d' % (exp_resp.rt, reactionTimeSum, totalTrialsReactedSuccessfully))
                
            if exp_resp.corr == 1:
                selectCorrect = 1
                selectIncorrectSolid = 0
                selectIncorrectDashed = 0
                numCorrectTrials += 1
            else:
                selectCorrect = 0
                if cueType == 'solid':
                    selectIncorrectSolid = 1
                    selectIncorrectDashed = 0
                else:
                    selectIncorrectSolid = 0
                    selectIncorrectDashed = 1
            # keep track of which components have finished
            DetermineExpFeedbackComponents = []
            for thisComponent in DetermineExpFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            DetermineExpFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "DetermineExpFeedback"-------
            while continueRoutine:
                # get current time
                t = DetermineExpFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=DetermineExpFeedbackClock)
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
                for thisComponent in DetermineExpFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "DetermineExpFeedback"-------
            for thisComponent in DetermineExpFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "DetermineExpFeedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            selectSolid = data.TrialHandler(nReps=selectIncorrectSolid, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='selectSolid')
            thisExp.addLoop(selectSolid)  # add the loop to the experiment
            thisSelectSolid = selectSolid.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid.rgb)
            if thisSelectSolid != None:
                for paramName in thisSelectSolid:
                    exec('{} = thisSelectSolid[paramName]'.format(paramName))
            
            for thisSelectSolid in selectSolid:
                currentLoop = selectSolid
                # abbreviate parameter names if possible (e.g. rgb = thisSelectSolid.rgb)
                if thisSelectSolid != None:
                    for paramName in thisSelectSolid:
                        exec('{} = thisSelectSolid[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "SolidFeedback"-------
                continueRoutine = True
                routineTimer.add(5.000000)
                # update component parameters for each repeat
                sound_1.setSound('A', secs=1.0, hamming=True)
                sound_1.setVolume(1.0, log=False)
                # keep track of which components have finished
                SolidFeedbackComponents = [sound_1, image_2]
                for thisComponent in SolidFeedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                SolidFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "SolidFeedback"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = SolidFeedbackClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=SolidFeedbackClock)
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
                        if tThisFlipGlobal > image_2.tStartRefresh + 5.0-frameTolerance:
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
                    for thisComponent in SolidFeedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "SolidFeedback"-------
                for thisComponent in SolidFeedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                sound_1.stop()  # ensure sound has stopped at end of routine
                selectSolid.addData('sound_1.started', sound_1.tStartRefresh)
                selectSolid.addData('sound_1.stopped', sound_1.tStopRefresh)
                selectSolid.addData('image_2.started', image_2.tStartRefresh)
                selectSolid.addData('image_2.stopped', image_2.tStopRefresh)
                thisExp.nextEntry()
                
            # completed selectIncorrectSolid repeats of 'selectSolid'
            
            
            # set up handler to look after randomisation of conditions etc
            selectDashed = data.TrialHandler(nReps=selectIncorrectDashed, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='selectDashed')
            thisExp.addLoop(selectDashed)  # add the loop to the experiment
            thisSelectDashed = selectDashed.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed.rgb)
            if thisSelectDashed != None:
                for paramName in thisSelectDashed:
                    exec('{} = thisSelectDashed[paramName]'.format(paramName))
            
            for thisSelectDashed in selectDashed:
                currentLoop = selectDashed
                # abbreviate parameter names if possible (e.g. rgb = thisSelectDashed.rgb)
                if thisSelectDashed != None:
                    for paramName in thisSelectDashed:
                        exec('{} = thisSelectDashed[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "DashedFeedback"-------
                continueRoutine = True
                routineTimer.add(5.000000)
                # update component parameters for each repeat
                sound_2.setSound('A', secs=1.0, hamming=True)
                sound_2.setVolume(1.0, log=False)
                # keep track of which components have finished
                DashedFeedbackComponents = [sound_2, image_3]
                for thisComponent in DashedFeedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                DashedFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "DashedFeedback"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = DashedFeedbackClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=DashedFeedbackClock)
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
                        if tThisFlipGlobal > image_3.tStartRefresh + 5.0-frameTolerance:
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
                    for thisComponent in DashedFeedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "DashedFeedback"-------
                for thisComponent in DashedFeedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                sound_2.stop()  # ensure sound has stopped at end of routine
                selectDashed.addData('sound_2.started', sound_2.tStartRefresh)
                selectDashed.addData('sound_2.stopped', sound_2.tStopRefresh)
                selectDashed.addData('image_3.started', image_3.tStartRefresh)
                selectDashed.addData('image_3.stopped', image_3.tStopRefresh)
                thisExp.nextEntry()
                
            # completed selectIncorrectDashed repeats of 'selectDashed'
            
            
            # ------Prepare to start Routine "Delay"-------
            continueRoutine = True
            routineTimer.add(0.200000)
            # update component parameters for each repeat
            # keep track of which components have finished
            DelayComponents = [text_2]
            for thisComponent in DelayComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            DelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Delay"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = DelayClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=DelayClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    text_2.setAutoDraw(True)
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in DelayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Delay"-------
            for thisComponent in DelayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('text_2.started', text_2.tStartRefresh)
            trials.addData('text_2.stopped', text_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed numBlocks repeats of 'blocks'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'postures'


# ------Prepare to start Routine "Results"-------
continueRoutine = True
# update component parameters for each repeat
accuracy = float(numCorrectTrials) / float(totalTrialsAttempted)
avgReactionTime = reactionTimeSum / float(totalTrialsReactedSuccessfully)

experimentResultsText = """
Thank you for participating in our experiment.
Your participantion is greatly appreciated.

You had an accuracy rate of 

%d / %d = %0.1f %% correct

For comparison, in a previous study, participants
achieved an accuracy of 92.5%%

Your average reaction time on the trials
that you responded in time was

%0.4f sec

For comparison, in a previous study, participants
achieved an average reaction time of 0.5404 sec

Press any key when you are ready to finish the experiment.
""" % (numCorrectTrials, totalTrialsAttempted, accuracy * 100.0, avgReactionTime)

text_4.setText(experimentResultsText)
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
ResultsComponents = [text_4, key_resp_3]
for thisComponent in ResultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ResultsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Results"-------
while continueRoutine:
    # get current time
    t = ResultsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ResultsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ResultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Results"-------
for thisComponent in ResultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Results" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
