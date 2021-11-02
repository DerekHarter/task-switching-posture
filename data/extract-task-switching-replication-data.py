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
    'congruantTrialType': 'congruantTrialType',
    'cueType': 'cueType',
    'shapeType': 'shapeType',
    'shapeColor': 'shapeColor',
    'exp_resp.keys': 'response',
    'correctAnswer': 'correctResponse',
    'exp_resp.corr': 'correct',
    'exp_resp.rt': 'reactionTime',    
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
    task_switching_replication_df = None
    
    # find files matching raw PsychoPy subject trial/data name
    file_pattern = "[0-9][0-9][0-9][0-9]_*_*_*"
    raw_data_pattern = data_dir + "/" + file_pattern + ".csv"
    raw_data_file_list = glob.glob(raw_data_pattern)
    raw_data_file_list.sort()
    for raw_data_file in raw_data_file_list:
        # ignore csv files of trial information
        if 'trials' in raw_data_file:
            continue

        # otherwise raw psychopy data file, process it
        # read csv into a dataframe
        #print('Processing file <%s>' % raw_data_file)
        subject_df = pd.read_csv(raw_data_file)

        # for this tidy data, only keep the actual experiment trialType trials
        mask = subject_df.trialType == 'experiment'
        subject_df = subject_df[mask]

        # extract only the useful/needed features for data analysis, and
        # rename the features to better feature names for consistance of
        # data analysis
        subject_df = subject_df[final_features.keys()]
        subject_df = subject_df.rename(columns=final_features)

        # append this subject data to the final data frame
        if task_switching_replication_df == None:
            task_switching_replication_df = subject_df
        else:
            task_switching_replication_df = pd.concat([task_switching_replication_df, subject_df], ignore_index=True)

    # clean the data frame
    # blockNum and trialNum are coming out as floats, make them regular ints
    task_switching_replication_df.blockNum = task_switching_replication_df.blockNum.astype(int)
    task_switching_replication_df.trialNum = task_switching_replication_df.trialNum.astype(int)
    task_switching_replication_df.correctResponse = task_switching_replication_df.correctResponse.astype(int)
    #task_switching_replication_df.correct = task_switching_replication_df.correct.astype(int)

    # map 1/2 responses to left/right and None to timeout in our data
    task_switching_replication_df.response = task_switching_replication_df.response.map(left_right_map)
    task_switching_replication_df.correctResponse = task_switching_replication_df.correctResponse.map(left_right_map)
    task_switching_replication_df.correct = task_switching_replication_df.correct.map(correct_map)
    
    # for some reason we get duplicate results of trials (maybe a key press followed
    # real quickly by another)?  Any time that the response is blank is an indication
    # this is a duplicate row, so drop the row
    task_switching_replication_df = task_switching_replication_df.dropna(subset=['response'])

    # return the cleaned and tidy dataframe
    return task_switching_replication_df


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
