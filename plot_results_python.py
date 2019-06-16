import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


def plot_results(version, x_limit=0.08, colors=None, markers=None, linewidth=3,
                 fontsize=12, figure_size=(11, 6)):
    r"""
    Method that generates the 300W Faces In-The-Wild Challenge (300-W) results
    in the form of Cumulative Error Distributions (CED) curves. The function
    renders the indoor, outdoor and indoor + outdoor results based on both 68
    and 51 landmark points in 6 different figures.

    Please cite:
    C. Sagonas, E. Antonakos, G. Tzimiropoulos, S. Zafeiriou, M. Pantic. "300
    Faces In-The-Wild Challenge: Database and Results", Image and Vision
    Computing, 2015.
    
    Parameters
    ----------
    version : 1 or 2
        The version of the 300W challenge to use. If 1, then the reported
        results are the ones of the first conduct of the competition in the
        ICCV workshop 2013. If 2, then the reported results are the ones of
        the second conduct of the competition in the IMAVIS Special Issue 2015.
    x_limit : float, optional
        The maximum value of the horizontal axis with the errors.
    colors : list of colors or None, optional
        The colors of the lines. If a list is provided, a value must be
        specified for each curve, thus it must have the same length as the
        number of plotted curves. If None, then the colours are linearly sampled
        from the jet colormap. Some example colour values are:

                'r', 'g', 'b', 'c', 'm', 'k', 'w', 'orange', 'pink', etc.
                or
                (3, ) ndarray with RGB values

    linewidth : float, optional
        The width of the rendered lines.
    fontsize : int, optional
        The font size that is applied on the axes and the legend.
    figure_size : (float, float) or None, optional
        The size of the figure in inches.
    """
    # Check version
    if version == 1:
        participants = ['Baltrusaitis', 'Hasan', 'Jaiswal', 'Milborrow', 'Yan',
                        'Zhou']
    elif version == 2:
        participants = ['Cech', 'Deng', 'Fan', 'Martinez', 'Uricar']
    else:
        raise ValueError('version must be either 1 or 2')
        
    # Initialize lists
    ced68 = []
    ced68_indoor = []
    ced68_outdoor = []
    ced51 = []
    ced51_indoor = []
    ced51_outdoor = []
    legend_entries = []

    # Load results
    results_folder = '../300W/'+'300W_v{}'.format(int(version))
    for f in participants:
        # Read file
        filename = f + '.txt'
        tmp = np.loadtxt(str(Path(results_folder) / filename), skiprows=4)
        # Get CED values
        bins = tmp[:, 0]
        ced68.append(tmp[:, 1])
        ced68_indoor.append(tmp[:, 2])
        ced68_outdoor.append(tmp[:, 3])
        ced51.append(tmp[:, 4])
        ced51_indoor.append(tmp[:, 5])
        ced51_outdoor.append(tmp[:, 6])
        # Update legend entries
        legend_entries.append(f + ' et al.')
        
    # 68 points, indoor + outdoor
    title = 'Indoor + Outdoor, 68 points'        
    _plot_curves(bins, ced68, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    # 68 points, indoor
    title = 'Indoor, 68 points'
    _plot_curves(bins, ced68_indoor, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    # 68 points, outdoor
    title = 'Outdoor, 68 points'
    _plot_curves(bins, ced68_outdoor, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    # 51 points, indoor + outdoor
    title = 'Indoor + Outdoor, 51 points'
    _plot_curves(bins, ced51, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    # 51 points, indoor
    title = 'Indoor, 51 points'
    _plot_curves(bins, ced51_indoor, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    # 51 points, outdoor
    title = 'Outdoor, 51 points'
    _plot_curves(bins, ced51_outdoor, legend_entries, title, x_limit=x_limit,
                 colors=colors, linewidth=linewidth, fontsize=fontsize,
                 figure_size=figure_size)
    plt.show()
    
def _plot_curves(bins, ced_values, legend_entries, title, x_limit=0.08,
                 colors=None, linewidth=3, fontsize=12, figure_size=None):
    # number of curves
    n_curves = len(ced_values)
    
    # if no colors are provided, sample them from the jet colormap
    if colors is None:
        cm = plt.get_cmap('jet')
        colors = [cm(1.*i/n_curves)[:3] for i in range(n_curves)]
        
    # plot all curves
    fig = plt.figure()
    ax = plt.gca()
    for i, y in enumerate(ced_values):
        plt.plot(bins, y, color=colors[i],
                 linestyle='-',
                 linewidth=linewidth, 
                 label=legend_entries[i])
        
    # legend
    ax.legend(prop={'size': fontsize}, loc=0)
    
    # axes
    for l in (ax.get_xticklabels() + ax.get_yticklabels()):
        l.set_fontsize(fontsize)
    ax.set_xlabel('Point-to-point Normalized RMS Error', fontsize=fontsize)
    ax.set_ylabel('Images Proportion', fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)

    # set axes limits
    ax.set_xlim([0., x_limit])
    ax.set_ylim([0., 1.])
    ax.set_yticks(np.arange(0., 1.1, 0.1))
    
    # grid
    plt.grid('on', linestyle='--', linewidth=0.5)
    
    # figure size
    if figure_size is not None:
        fig.set_size_inches(np.asarray(figure_size))

def main():
    plot_results(1)
    plot_results(2)

if __name__ == '__main__':
    main()
