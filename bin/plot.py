#!/usr/bin/env python3

import sys
import glob
import os
import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


NUM_OSCILLATORS = 8


def everything_else(command, latest_folder):

    print("Creating Plot...")

    # List of lists to hold average counts
    averages = create_averages(NUM_OSCILLATORS)

    # Iterate through all .log files
    for filename in sorted(glob.glob(latest_folder + '/*.log')):
        if not filename.endswith(".log"):
            continue
        if filename.endswith("characterization_0.log"):
            #continue
            pass
        print(filename)
        f = open(filename,"r")

        # Create lists containing the lines we care about in the file
        attempts = []
        counts = []
        for line in f:
            if line.find("Attempt") != -1:
                if line.find("Frequency") == -1:
                    attempts.append(line)
                if line.find("Ring") != -1:
                    counts.append(line)

        # Script only works if the ranking don't intermittently change..
        # Let's fix the .elf so that we don't have this problem
        if not (compare_attempts(attempts)):
            print("Rankings inconsistent. Exiting...")
            sys.exit(1)


        # Split the CSV data and get the ring oscillator number and average
        for line in counts:
            split = line.split(',')
            ringosc_no = int(split[0][-1])
            average = int(split[-1].strip())
            averages[ringosc_no].append(average)

    return averages


def get_most_recent_run(command):
    # Get the most recent run
    directory = "/home/adam/RO-PUF/runs/logs/" + command + "/"
    list_of_folders = glob.glob(directory + "*")
    latest_folder = max(list_of_folders, key=os.path.getctime) + "/"
    return latest_folder


def create_averages(num_oscillators):
    # List of lists to hold average counts
    return [[] for _ in range(num_oscillators)]


def compare_attempts(attempts):
    # Make sure the rankings are consistent
    attempt0 = attempts[0].split(':')[1]
    attempt1 = attempts[1].split(':')[1]
    attempt2 = attempts[2].split(':')[1]
    
    if attempt0 != attempt1:
        return False
    if attempt1 != attempt2:
        return False
    return True


def plot_averages(averages):
    # Plot averages
    x_axis = [4*i for i in range(0,len(averages[0]))]
    for average in averages:
        plt.plot(x_axis,average)


def save_plot(latest_folder):
    # Save plot to file
    plt.xlabel('Hours')
    plt.ylabel('Count')
    plt.savefig(latest_folder + "/plot.png")


def parse_args():
    parser = argparse.ArgumentParser(description='Plot RO-PUF run')
    parser.add_argument('command', choices=['burn', 'control', 'test'])
    args = parser.parse_args()
    return args


def main():
    # all the other stuff...
    args = parse_args()
    command = args.command
    latest_folder = get_most_recent_run(command)
    averages = everything_else(command, latest_folder)
    plot_averages(averages)
    save_plot(latest_folder)


if __name__ == '__main__':
    main()
