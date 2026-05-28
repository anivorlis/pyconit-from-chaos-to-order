# Numbers are good but let's add some visuals
# We will use matplotlib

import matplotlib.pyplot as plt

from ex01.e02 import dice_simulation, dice_statistics


def plot_dice_statistics(stats):
    '''Plot the dice statistics as a bar chart.'''
    faces = list(stats.keys())
    counts = list(stats.values())

    fig, ax = plt.subplots()
    ax.bar(faces, counts, color='steelblue', edgecolor='black')
    ax.set_xlabel('Dice face')
    ax.set_ylabel('Count')
    ax.set_title(f'Dice roll distribution ({sum(counts)} rolls)')
    ax.set_xticks(faces)
    return fig, ax


if __name__ == '__main__':
    results = dice_simulation(1000)
    stats = dice_statistics(results)
    plot_dice_statistics(stats)
    plt.show()
