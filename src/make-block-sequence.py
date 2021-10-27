#!/usr/bin/env python
import random

cueTypes = ['dashed', 'solid']
shapeTypes = ['square', 'triangle']
shapeColors = ['blue', 'yellow']

def random_trials(numTrials):

    trials = []
    for trial in range(1, numTrials + 2):
        cueType = random.choice(cueTypes)
        shapeType = random.choice(shapeTypes)
        shapeColor = random.choice(shapeColors)
        trials.append( (trial, cueType, shapeType, shapeColor) )

    return trials

def counter_balanced_trials(numTrials):
    """
    We generate numTrials + 1, first trial is randomly
    selected, then remaining trials are selected to 
    have equal numbers of congruant/incongruant and
    switch/no-switch trials.  We expect numTrials to be
    an even number divisible by 2.
    """
    trials = []

    # genenerate initial random trial
    cueType = random.choice(cueTypes)
    shapeType = random.choice(shapeTypes)
    shapeColor = random.choice(shapeColors)
    trial = (1, 'NA', 'NA', cueType, shapeType, shapeColor)

    trials.append( trial )

    # now create and randomly permute the trial types
    # we are trying to balance
    halfTrials = int(numTrials / 2)
    congruantTrialTypes = ['congruant'] * halfTrials + ['incongruant'] * halfTrials
    random.shuffle(congruantTrialTypes)
    switchTrialTypes = ['switch'] * halfTrials + ['noswitch'] * halfTrials
    random.shuffle(switchTrialTypes)
    trialNums = range(2, numTrials + 2)

    for trialNum, congruantTrialType, switchTrialType in zip(trialNums, congruantTrialTypes, switchTrialTypes):
        _, _, _, prevCueType, prevShapeType, prevShapeColor = trials[-1]

        # determine whether this is a switch or no switch on the task (choose by shape vs.
        # choose by color)
        if switchTrialType == 'noswitch':
            cueType = prevCueType
        else:
            if prevCueType == 'dashed':
                cueType = 'solid'
            else:
                cueType = 'dashed'

        # determine if response is congruant (push same button) or incongruant
        # (push the other button)
        # TODO: we currently hard code that cue solid is choose by shape and
        #   cue dashed is choose by color, but this needs to differ depending
        #   on the participant condition of what the cue means
        if congruantTrialType == 'congruant':
            if prevCueType == 'solid': # hard code solid to shape select task
                shapeType = prevShapeType
                shapeColor = random.choice(shapeColors)
            else: # hard code dashed to be color select task
                shapeColor = prevShapeColor
                shapeType = random.choice(shapeTypes)
        else:
            if prevCueType == 'solid': # hard code solid to shape select task
                if prevShapeType == 'square':
                    shapeType = 'triangle'
                else:
                    shapeType = 'square'
                shapeColor = random.choice(shapeColors)
            else: # hard code dashed to be color select task
                if prevShapeColor == 'blue':
                    shapeColor = 'yellow'
                else:
                    shapeColor = 'blue'
                shapeType = random.choice(shapeTypes)

        # save the generated trial to be returned
        trial = (trialNum, switchTrialType, congruantTrialType, cueType, shapeType, shapeColor)
        trials.append( trial )

    return trials
                    

def trialsToCsv(trials):
    # file header
    print("trialNum,switchTrialType,congruantTrialType,cueType,shapeType,shapeColor,cueFileName,stimuliFileName,correctAnswer")

    # loop to generate trial settings/variables
    for trialNum, switchTrialType, congruantTrialType, cueType, shapeType, shapeColor in trials:
        # file names for cue/stimuli to use for this trial
        cueFileName = 'stimuli/%s-rectangle.png' % (cueType)
        stimuliFileName = 'stimuli/%s-%s.png' % (shapeColor, shapeType)

        # correct answer for this trial.
        # TODO: we are hard codeing condition 07 at the moment as correct answer here
        correctAnswer = 1
        if cueType == 'dashed': # select by color
            if shapeColor == 'yellow':
                correctAnswer = 1
            else:
                correctAnswer = 2
        else: # select by shape
            if shapeType == 'triangle':
                correctAnswer = 1
            else:
                correctAnswer = 2

        # output this trial
        print('%d,%s,%s,%s,%s,%s,%s,%s,%d' %
              (trialNum, switchTrialType, congruantTrialType, cueType, shapeType, shapeColor, cueFileName, stimuliFileName, correctAnswer))
              
if __name__ == "__main__":
    #trials = random_trials(48)
    trials = counter_balanced_trials(48)
    trialsToCsv(trials)
