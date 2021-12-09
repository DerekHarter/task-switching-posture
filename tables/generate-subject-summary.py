#!/usr/bin/env python
"""Generate a LaTeX table summarizing all participants
run so far, with information about the date and condition
when run, and average accuracy and reaction time
"""
import argparse
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
table_dir = '.'
description = """
This script will generate a table summarizing all participants
run so far, with information about the date and condition
when run, and average accuracy and reaction time.
"""

correct_map = {
    'no': 0.0,
    'yes': 1.0,
}

def generate_subject_summary_df(data_file):
    """Generate summary dataframe of experimental subjects

    Parameters
    ----------
    data_file - The name of the data file to open and load in for processing.
      Expected to be a csv file suitable for load by pandas read_csv.

    Returns
    -------
    subject_summary_df - Returns a pandas dataframe summarizing the
      experiment subjects / participants.
    """
    # load input data frame
    df = pd.read_csv(data_file)
    df['correctValue'] = df.correct.map(correct_map)

    # drop all buffer trials, not needed in results here
    # NOTE: Is this true?  We do have reaction times for the buffer trials.
    #   Should the be dropped from calculations of the results for this table?
    mask = df.congruentTrialType != 'buffer'
    df = df[mask]
    
    # group data by posture and congruent conditions
    gdf = df.groupby(['date'])

    # construct a resulting summary dataframe of this grouped
    # data
    summary_dict = {
        'participant': gdf['participant'].first().astype(int),
        'condition': gdf['condition'].first().astype(int),
        'numTrials': gdf['participant'].count().astype(int),
        'accuracyMean': gdf['correctValue'].mean(),
        'accuracyStd': gdf['correctValue'].std(),
        'reactionTimeMean': gdf['reactionTime'].mean(),
        'reactionTimeStd': gdf['reactionTime'].std(),
    }
    subject_summary_df = pd.DataFrame(summary_dict)    

    # return the resulting dataframe
    return subject_summary_df


def save_table(subject_summary_df, output_file):
    """Create and save a generated LaTeX table of this dataframe.

    Parameters
    ----------
    subject_summary_df - A dataframe of the summarized subject information.
    output_file - The name of the file to save the table into.
    """
    caption = "Summary of experiment participants results"
    label = "table-subject-summary"
    header = ['part', 'cond', 'trials', 'accuracy', 'std', 'rt', 'std']
    subject_summary_df.to_latex(output_file,
                                index=True,
                                #header=True,
                                bold_rows=False,
                                float_format="%0.4f",
                                caption=caption,
                                label=label,
                                header=header,
                                longtable=True)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data', 
                        help='the name of the experiment (cleaned) data file to open and process')
    parser.add_argument('--output', default=None,
                        help='name of output table, defaults to table-subject-summary.tex')
    args = parser.parse_args()

    # determine output file name if not given explicitly
    output_file = args.output
    if output_file is None:
        # make full output file name, assume .png output by default
        output_file = 'table-subject-summary.tex'


    # generate and save the table for the asked for models
    subject_summary_df = generate_subject_summary_df(args.data)
    save_table(subject_summary_df, output_file)


if __name__ == "__main__":
    main()
