import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from layouts.recall_plot import recall_plot_layout
from create_callbacks import create_callbacks

app = dash.Dash()
app.layout = recall_plot_layout()
app = create_callbacks(app)

if __name__ == '__main__':

    app.run_server(debug=True)