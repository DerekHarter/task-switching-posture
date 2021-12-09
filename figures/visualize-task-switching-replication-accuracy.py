#!/usr/bin/env python
"""Create figure visualization of task switching replication experiment
accuracy results.  This figure summarizes subject accuracy on task
broken down by posture (sitting vs. standing) and congruancy
(congruent vs. incongruent) conditions.

"""
import argparse
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# other global constants / locations.  parameterize these if we need
# flexibility to specify them on command line or move them around
figure_dir = '.'
description = """ This script creates a figure visualization of the task switching
replication experiment accuracy results.  The figure summarizes
accuracy on task by subjects broken down by posture (sitting
vs. standing) and congruancy (congruent vs. incongruent) conditions.
"""


correct_map = {
    'no': 0.0,
    'yes': 1.0,
}

def create_accuracy_figure(data_file, output_file):
    """Create and save the summarized accuracy figure broken down
    by posture and congruancy conditions.

    Parameters
    ----------
    data_file - The name of the input data file to load and process for
      figure visualization.  This is assumed to be a csv formatted file
      suitable to be read in by pandas read_csv() function.
    output_file - The resulting figure file name to create.
    """
    # load in data to dataframe for processing
    df = pd.read_csv(data_file)
    df['correctValue'] = df.correct.map(correct_map)

    # drop all buffer trials, not needed in results here
    mask = df.congruentTrialType != 'buffer'
    df = df[mask]

    # using seaborn high-level df, visualize accuracy by posture, and
    # using the hue (color) to split by congruent/incongruent
    fig, axes = plt.subplots(1, 2, figsize=(12, 8))

    # first visualize only congruent trials
    mask = df.congruentTrialType == 'congruent'
    df_congruent = df[mask]
    
    # plot congruent figure results
    sb.barplot(ax=axes[0],
               x='switchTrialType', order = ['noswitch', 'switch'],
               y='correctValue',
               hue='posture', hue_order = ['sitting', 'standing'],
               data=df_congruent, ci=95)

    # add in figure information and labels
    axes[0].set_xlabel('Condition')
    axes[0].set_ylabel('Proportion Correct (Accuracy)')
    axes[0].set_title('Congruent')
    axes[0].set_ylim([0.75, 1.0])
    
    # plot incongruent figure results
    mask = df.congruentTrialType == 'incongruent'
    df_incongruent = df[mask]
    sb.barplot(ax=axes[1],
               x='switchTrialType', order = ['noswitch', 'switch'],
               y='correctValue',
               hue='posture', hue_order = ['sitting', 'standing'],
               data=df_incongruent, ci=95)

    # add in figure information and labels
    axes[1].set_xlabel('Condition')
    axes[1].set_ylabel('Proportion Correct (Accuracy)')
    axes[1].set_title('Incongruent')
    axes[1].set_ylim([0.75, 1.0])
    
    # save the resulting figure
    plt.savefig(output_file, transparent=True, dpi=300)


def main():
    """Main entry point for this figure visualizaiton creation
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data',
                        help='the name of the input data file to load and create figure from')
    parser.add_argument('--output', default=None,
                        help='name of output figure, defaults to figure-task-switching-replication-accuracy.png')
    args = parser.parse_args()

    # determine output file name if not given explicitly
    output_file = args.output
    if output_file is None:
        # make full output file name, assume .png output by default
        output_file = 'figure-stroop-replication-accuracy.png'

    # generate and save the figure for the asked for model
    create_accuracy_figure(args.data, output_file)


if __name__ == "__main__":
    main()
