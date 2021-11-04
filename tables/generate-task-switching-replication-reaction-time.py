#!/usr/bin/env python
"""Generate a LaTeX table of results of reaction time means
and standard deviations for task switching replication grouped
by posture and congruancyconditions.
"""
import argparse
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
table_dir = '.'
description = """
This script will generate a table of results summarizing
the reaction time experimental data for all
subjects, grouped by the experiment posture and congruancy
conditions.
"""

correct_map = {
    'no': 0.0,
    'yes': 1.0,
}

def generate_reaction_time_df(data_file):
    """Generate summary dataframe of reaction time results
    from input data file.

    Parameters
    ----------
    data_file - The name of the data file to open and load in for processing.
      Expected to be a csv file suitable for load by pandas read_csv.

    Returns
    -------
    rt_accuracy_df - Returns a pandas dataframe summarizing reaction time and
      accuracy data collected from experiments.
    """
    # load input data frame
    df = pd.read_csv(data_file)
    df['correctValue'] = df.correct.map(correct_map)

    # drop all buffer trials, not needed in results here
    # NOTE: Is this true?  We do have reaction times for the buffer trials.
    #   Should the be dropped from calculations of the results for this table?
    mask = df.congruantTrialType != 'buffer'
    df = df[mask]
    
    # group data by posture and congruant conditions
    gdf = df.groupby(['posture', 'congruantTrialType', 'switchTrialType'])

    # construct a resulting summary dataframe of this grouped
    # data
    summary_dict = {
        'accuracyMean': gdf['correctValue'].mean(),
        'accuracyStd': gdf['correctValue'].std(),
        'reactionTimeMean': gdf['reactionTime'].mean(),
        'reactionTimeStd': gdf['reactionTime'].std()
    }
    reaction_time_df = pd.DataFrame(summary_dict)    

    # return the resulting dataframe
    return reaction_time_df


def save_table(reaction_time_df, output_file):
    """Create and save a generated LaTeX table of this dataframe.

    Parameters
    ----------
    reaction_time_df - A dataframe of the summarized reaction time data.
    output_file - The name of the file to save the table into.
    """
    caption = "Means and standard deviations of accuracy and reaction times (in ms) as a function of posture and experiment trial types."
    label = "table-task-switching-replication-reaction-time"
    header = ['accuracy', 'std', 'rt', 'std']
    reaction_time_df.to_latex(output_file,
                              index=True,
                              #header=True,
                              bold_rows=False,
                              float_format="%0.4f",
                              caption=caption,
                              label=label,
                              header=header,
                              longtable=False)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data', 
                        help='the name of the experiment (cleaned) data file to open and process')
    parser.add_argument('--output', default=None,
                        help='name of output table, defaults to table-task-switching-replication-reaction-time.tex')
    args = parser.parse_args()

    # determine output file name if not given explicitly
    output_file = args.output
    if output_file is None:
        # make full output file name, assume .png output by default
        output_file = 'table-task-switching-replication-reaction-time.tex'


    # generate and save the table for the asked for models
    reaction_time_df = generate_reaction_time_df(args.data)
    save_table(reaction_time_df, output_file)


if __name__ == "__main__":
    main()
