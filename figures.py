"""
define class for drawing curves
"""

import os
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set(color_codes=True)
sns.set(font_scale=1.5)
sns.set_style("whitegrid", {'axes.edgecolor': '0.0',
                            'grid.color': '.8', 'legend.frameon': True})
 
class Line(object):
    """
    single line to be plot
    """

    def __init__(self, label, data, line_style="-", color="blue", line_width=2.5):
        self.label = label
        self.data = data
        self.line_style = line_style
        self.color = color
        self.line_width = line_width


class Figure(object):
    """
    figure
    """

    def __init__(self, figure_name, save_path="./",
                 xlabel=None, ylabel=None,
                 title=None, x_lim=None, y_lim=None):
        self.figure_name = figure_name
        self.save_path = save_path
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.x_lim = x_lim
        self.y_lim = y_lim

    def draw(self, lines):
        """
        draw figure
        """
        if not isinstance(lines, list):
            lines = [lines]

        plt.figure()
        for items in lines:
            data_len = len(items.data)
            x = np.linspace(1, data_len, data_len)
            plt.plot(x, items.data, items.line_style,
                     linewidth=items.line_width,
                     color=items.color,
                     label=items.label)

        if self.xlabel is not None:
            plt.xlabel(self.xlabel)
        if self.ylabel is not None:
            plt.ylabel(self.ylabel)
        if self.x_lim is not None:
            plt.xlim(self.x_lim)
        if self.y_lim is not None:
            plt.ylim(self.y_lim)
        if self.title is not None:
            plt.title(self.title)
        plt.legend(loc=0, fontsize="small")

        plt.savefig(os.path.join(self.save_path,
                                 self.figure_name + ".pdf"), format="pdf")
        plt.savefig(os.path.join(self.save_path,
                                 self.figure_name + ".png"), format="png")
