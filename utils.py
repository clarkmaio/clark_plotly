
import pandas as pd
import numpy as np
from plotly.offline import plot

def plotly_decorator(func):
    """
    If "save" key is in kwargs save the plot as html file using the "filename" key in kwargs
    """
    def wrapper(*args, **kwargs):

        fig = func(*args, **kwargs)

        if 'save' in kwargs:
            save = kwargs['save']
            if save:
                assert isinstance(kwargs['filename'], str)
                plot(fig, auto_open=False, filename=kwargs['filename'])

        return fig
    return wrapper
