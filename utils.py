
import pandas as pd
import numpy as np
from plotly.offline import plot

def plotly_decorator(func):
    """
    If "save" key is in kwargs save the plot as html file using the "filename" key in kwargs
    """
    def wrapper(*args, **kwargs):

        # Setup 'save' and 'filename' key
        if not 'save' in kwargs:
            save = False
        else:
            save = kwargs['save']
            kwargs.pop('save')

        if not 'filename' in kwargs:
            filename = np.nan
        else:
            filename = kwargs['filename']
            kwargs.pop('filename')


        fig = func(*args, **kwargs)

        if save:
            assert isinstance(filename, str)
            assert filename.endswith('.html')
            plot(fig, auto_open=False, filename=filename)

        return fig
    return wrapper
