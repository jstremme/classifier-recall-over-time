import dash
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from utilities.color_palette import ColorPalette
from utilities.load_data import get_performance_values

def create_callbacks(app):

    @app.callback(dash.dependencies.Output('graph', 'figure'),
                  [dash.dependencies.Input('threshold', 'value')])
    def update_graph(threshold):

        float_threshold = int(threshold)*0.01
        months, num_recalled, num_diagnosed, recall, precision  = get_performance_values(threshold=float_threshold)
        print('Months: {}'.format(months))
        print('Num Recalled: {}'.format(num_recalled))
        print('Num Diagnosed: {}'.format(num_diagnosed))
        print('Recall: {}'.format(recall))
        print('Precision: {}'.format(precision))

        colors = ColorPalette()
        trace1 = go.Bar(x=months,
                        y=num_recalled,
                        name='Recalled',
                        marker=dict(color=colors.recalled))
        trace2 = go.Bar(x=months,
                        y=num_diagnosed,
                        name='Diagnosed',
                        marker=dict(color=colors.diagnosed))

        return {
            'data': 
                [trace1, trace2],
            'layout': 
                go.Layout(
                    barmode='stack',
                    plot_bgcolor=colors.background,
                    paper_bgcolor=colors.background,
                    font={'color': colors.text},
                    title='Total Recall: {}\n'.format(recall)
                          + ' -- ' +
                          'Total Precision: {}'.format(precision),
                    xaxis={'title': 'Month (M)'},
                    yaxis={'title': 'Cases'})
        }

    return app

