#!/usr/bin/env python
"""Extract task switching replication data for data analysis from
raw subject trial files and raw subject trial meta-experiment
data files.

"""
import os
import sys
import argparse
import glob
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
data_dir = '.'
description = """
This script extracts all task switching replication subject trials into
a single file for data analysis.  The result is a tidy
data file, in csv format, with 1 trial per line, and normalized
feature/column names.
"""


# final features desired, and order we desire them in
final_features = {
    'participant': 'participant',
    'session': 'session',
    'condition': 'condition',
    'trialType': 'trialType',
    'posture': 'posture',
    'blockNum': 'blockNum',
    'trialNum': 'trialNum',
    'switchTrialType': 'switchTrialType',
    'congruantTrialType': 'congruentTrialType',
    'cueType': 'cueType',
    'shapeType': 'shapeType',
    'shapeColor': 'shapeColor',
    'exp_resp.keys': 'response',
    'correctAnswer': 'correctResponse',
    'exp_resp.corr': 'correct',
    'exp_resp.rt': 'reactionTime',
    'date': 'date',
    'utcTime': 'utcTime',
}

left_right_map = {
    '1': 'left',
    1: 'left',
    '2': 'right',
    2: 'right',
    'None': 'timeout',
}

correct_map = {
    0.0: 'no',
    1.0: 'yes',
}

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


def get_congruent_map(condition):
    """
    Given the subject condition, return a dictionary which is a map of
    the stimuli keys to the congruent / incongruent trial type
    """
    posture, cue_solid, cue_dashed, color_left, color_right, shape_left, shape_right = \
       counter_balancing[condition]

    congruent_dict = {
        (color_left, shape_left): "congruent",
        (color_right, shape_right): "congruent",
        (color_left, shape_right): "incongruent",
        (color_right, shape_left): "incongruent",
    }
    
    return congruent_dict


def determine_congruent_trial_type(subject_df):
    """We were not quite coding congruent/incongruent correctly in initial
    PsychoPy experiment setup.  Extract correct congruent/incongruent coding
    for the given data frame.  Congruent/incongruent is a function of them
    participants condition, and the key coding mapping for the color and shape 
    stimuli responses.

    Parameters
    ----------
    subject_df - A dataframe containing subject response information, including the
       subject condition, and the stimuli for each trial the subject received.

    Returns
    -------
    df - Returns a new pandas dataframe with a new congruentrialType feature added
       coded from the subject condition and trial stimuli.
    """
    # the condition the subject was in, each row has the condition but the condition
    # should never change, so get the first rows condition to determine this subjects
    # condition
    condition = subject_df.condition.iloc[0]

    # get the map for this condition
    congruent_map = get_congruent_map(condition)

    # apply the mapping to recode the feature correctly
    #subject_df['congruentTrialType'] = subject_df.apply(lambda row: recode_trial_congruent_mapping(row.condition, row.shapeColor, row.shapeType),  axis=1)
    subject_df['congruentTrialType'] = subject_df.apply(lambda row: congruent_map[ (row.shapeColor, row.shapeType) ],  axis=1)
    
    return subject_df


def extract_task_switching_replication_data():
    """
    Extract subject trials and create a tidy data file from raw
    trial data.  We extract data from PsychoPy subject .csv raw
    trial output files. Result is returned as a clean/tidy
    pandas dataframe.

    Returns
    -------
    df - Returns a pandas dataframe of the extracted and cleaned
         task switching replication data.
    """
    # will hold result to return
    initDf = True
    df = None
    
    # find files matching raw PsychoPy subject trial/data name
    file_pattern = "[0-9][0-9][0-9][0-9]_*_*_*"
    raw_data_pattern = data_dir + "/" + file_pattern + ".csv"
    raw_data_file_list = glob.glob(raw_data_pattern)
    raw_data_file_list.sort()
    for raw_data_file in raw_data_file_list:
        # ignore csv files of trial information
        if 'trials' in raw_data_file:
            continue

        print('processing file: ', raw_data_file)
        
        # otherwise raw psychopy data file, process it
        # read csv into a dataframe
        subject_df = pd.read_csv(raw_data_file)
        
        # for this tidy data, only keep the actual experiment trialType trials
        mask = subject_df.trialType == 'experiment'
        subject_df = subject_df[mask]

        # extract only the useful/needed features for data analysis, and
        # rename the features to better feature names for consistance of
        # data analysis
        subject_df = subject_df[final_features.keys()]
        subject_df = subject_df.rename(columns=final_features)
        subject_df = determine_congruent_trial_type(subject_df)
        
        # append this subject data to the final data frame
        if initDf:
            df = subject_df
            initDf = False
        else:
            df = pd.concat([df, subject_df], ignore_index=True)

    # clean the data frame
    # blockNum and trialNum are coming out as floats, make them regular ints
    df.blockNum = df.blockNum.astype(int)
    df.trialNum = df.trialNum.astype(int)
    df.correctResponse = df.correctResponse.astype(int)
    #df.correct = df.correct.astype(int)

    # map 1/2 responses to left/right and None to timeout in our data
    df.response = df.response.map(left_right_map)
    df.correctResponse = df.correctResponse.map(left_right_map)
    df.correct = df.correct.map(correct_map)

    # convert date string to a real date
    df.date = pd.to_datetime(df.date, format='%Y_%b_%d_%H%M')
    
    # for some reason we get duplicate results of trials (maybe a key press followed
    # real quickly by another)?  Any time that the response is blank is an indication
    # this is a duplicate row, so drop the row
    df = df.dropna(subset=['response'])

    # return the cleaned and tidy dataframe
    return df


def save_task_switching_replication_data(data_file_name, task_switching_replication_df):
    """Save extracted data fame to output file as a csv formatted
    data file.

    Parameters
    ----------
    data_file_name - Name to save extracted data file to
    task_switching_replication_df - A pandas dataframe of the data to save
    """
    task_switching_replication_df.to_csv(data_file_name, index=False)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--output', default='stroop-replication.csv',
                        help='name of output data file, defaults to stroop-replication.csv')
    args = parser.parse_args()

    # extract the trials and experiment data from the raw files
    task_switching_replication_df = extract_task_switching_replication_data()
    save_task_switching_replication_data(args.output, task_switching_replication_df)

if __name__ == "__main__":
    main()
