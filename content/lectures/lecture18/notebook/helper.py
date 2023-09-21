def ellipse(x, y, width=0.25 / 1.25, height=0.7 / 1.25, color='#7A7A7A', ax=None):
    from matplotlib.patches import Ellipse
    from matplotlib.patheffects import withStroke
    ellipse = Ellipse((x, y), width=width, height=height, clip_on=False, zorder=10, linewidth=1,
                      edgecolor='black', facecolor=color,
                      path_effects=[withStroke(linewidth=5, foreground='w')])
    # Ellipse(xy, width, height, angle=0, **kwargs)
    # xy coordinates of ellipse centre.
    # width: Total length (diameter) of horizontal axis.
    # height : Total length (diameter) of vertical axis.
    # angle : Rotation in degrees anti-clockwise.
    # clip_on: Set whether the artist uses clipping/trimmed
    # zorder: Set the zorder for the artist. Artists with lower zorder values are drawn first.

    ax.add_artist(ellipse)
    # !!!!!!!!
