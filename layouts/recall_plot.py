import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from utilities.color_palette import ColorPalette

def recall_plot_layout():

    colors = ColorPalette()

    return(

        html.Div(
            style={'backgroundColor': colors.background, 'fontFamily': 'Courier New'},
            children=[
                html.H1(
                    children='Model Recall M Months into the Future',
                    style={
                        'textAlign': 'center',
                        'color': colors.text,
                        'font': dict(family='Courier New')}
                ),
                dcc.Graph(id='graph', config={'displayModeBar': False}),
                html.Label('Model Threshold', style={
                        'textAlign': 'center',
                        'color': colors.text,
                        'fontFamily': 'Courier New'}),
                dcc.Slider(
                            id='threshold',
                            min=0,
                            max=100,
                            marks={i:str(i) for i in range(0, 110, 10)},
                            value=50)       
            ])
    )