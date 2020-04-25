import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from clark_plotly.utils import plotly_decorator

@plotly_decorator
def simple_plot(df, x, y, **kwargs):
    """
    x: column x axis
    y: list of lines to plot. It MUST be a list (even for a single plot)
    """
    data = []
    for yy in y:
        p = go.Scattergl(x = df[x],
                         y = df[yy],
                         mode = 'markers+lines',
                         name = yy)
        data.append(p)

    layout = go.Layout(**kwargs)
    fig = go.Figure(data = data, layout = layout)
    return fig

@plotly_decorator
def double_plot(df, x, y1, y2, subplot_title = None, **kwargs):
    """
    x: column x axis
    y: list of lines to plot. It MUST be a list (even for a single plot)
    """

    fig = make_subplots(2, 1, subplot_titles=subplot_title)

    # First plot
    for yy in y1:
        p = go.Scattergl(x=df[x],
                         y=df[yy],
                         mode='markers+lines',
                         name=yy)
        fig.append_trace(1, 1, p)

    # Second plot
    for yy in y2:
        p = go.Scattergl(x=df[x],
                         y=df[yy],
                         mode='markers+lines',
                         name=yy)
        fig.append_trace(2, 1, p)

    layout = go.Layout(**kwargs)
    fig.update_layout(layout)
    return fig