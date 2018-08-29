# import required libraries
import matplotlib.pyplot as plt
from math import pi

# define functions

def spider(skills, categories):
    my_dpi=96
    plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)

    # Create a color palette:
    my_palette = plt.cm.get_cmap("Set2", len(skills.index))

    # number of variable
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    for row in range(0, len(skills.index)):
        # Initialise the spider plot
        ax = plt.subplot(1,1,row+1, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=7)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([1,2,3,4], ["1","2","3","4"], color="grey", size=7)
        plt.ylim(0,5)

        # Ind1
        values=skills.loc[skills.index[row]].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, color=my_palette(row), linewidth=2, linestyle='solid')
        ax.fill(angles, values, color=my_palette(row), alpha=0.4)

        # Add a title
        plt.title('skills from '+skills.index[row], size=10, color=my_palette(row), y=1.1)

    plt.tight_layout()
