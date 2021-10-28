#!/usr/bin/env python3
import random
import itertools
import sys

cue_types = ['dashed', 'solid']
shape_types = ['square', 'triangle']
shape_colors = ['blue', 'yellow']

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
    Given a trial cue, shape and color, determine
    correct response.

    NOTE: TBD, the following code should be looked up from
    the participant counter balanced conditions.
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
    for _, switch_type, *_ in trials:
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
    for _, _, congruant_type, *_ in trials:
        if congruant_type == 'congruant':
            congruant_count += 1

    num_trials = len(trials) - 1
    half_trials = num_trials // 2
    
    #print('is_congruant_balanced %d congruant out of %d trials' % (congruant_count, num_trials))
    return congruant_count == half_trials


def random_trials(condition, num_trials, add_buffer_trial=False):
    """
    Create the indicated number of trials and shuffle them
    randomly.  Return result as a list of the trial variables.
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
            switch_type = 'NA'
            congruant_type = 'NA'
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
        
        trials.append( (trial_num + 1, switch_type, congruant_type, cue_type, shape_type, shape_color, current_response) )

    # return the resulting constructed and randomly shuffled list of trials
    return trials


def counter_balanced_trials(condition, num_trials):
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
    trials = random_trials(condition, num_trials, True)

    # keep generating random trials of the requested size until
    # we find a balanced one, or until we reach some maximum
    # attempts, in which case something may be wrong
    num_attempts = 1
    while not is_balanced(trials) and num_attempts <= MAX_ATTEMPTS:
        trials = random_trials(condition, num_trials, True)
        num_attempts += 1

    # sanity check, make sure we found a balanced trial
    if not is_balanced(trials):
        print("<counter_balanced_trials> Error: could not achieve block balance in %d attempts, aborting" % (MAX_ATTEMPTS))
        sys.exit(1)
        
    # at this point we should have found a balanced trial
    return trials
                    

def trials_to_csv(filename, trials):
    f = open(filename, 'w')
    
    # file header
    f.write("trialNum,switchTrialType,congruantTrialType,cueType,shapeType,shapeColor,cueFileName,stimuliFileName,correctAnswer\n")

    # loop to generate trial settings/variables
    for trial_num, switch_type, congruant_type, cue_type, shape_type, shape_color, correct_response in trials:
        # file names for cue/stimuli to use for this trial
        cue_filename = 'stimuli/%s-rectangle.png' % (cue_type)
        stimuli_filename = 'stimuli/%s-%s.png' % (shape_color, shape_type)

        # output this trial
        f.write('%d,%s,%s,%s,%s,%s,%s,%s,%d\n' %
              (trial_num, switch_type, congruant_type, cue_type, shape_type, shape_color, cue_filename, stimuli_filename, correct_response))

    f.close()


def trials_to_triallist(trials):
    """
    Return a list of dictionaries, where keys are the trial feature/variable names
    """
    trial_list = []
    
    # loop to generate trial settings/variables
    for trial_num, switch_type, congruant_type, cue_type, shape_type, shape_color, correct_response in trials:
        # file names for cue/stimuli to use for this trial
        cue_filename = 'stimuli/%s-rectangle.png' % (cue_type)
        stimuli_filename = 'stimuli/%s-%s.png' % (shape_color, shape_type)

        trial_dict = {
            'trialNum': trial_num,
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
    
if __name__ == "__main__":
    subject_condition = 7
    trials = counter_balanced_trials(subject_condition, 48)
    print(trials_to_triallist(trials))
    #trials_to_csv('tmp.csv', trials)
    for trial in trials:
        print(trial)
