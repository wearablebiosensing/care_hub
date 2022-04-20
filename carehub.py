import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json
import glob
from sklearn import preprocessing
# Own imports
from iotex_data_analysis import data_viz_iotex 
from carewell_flask.carewell_FT_data import ft_usage 
## FOLLOWED -- Multistaged plotly app tutorials https://dash.plotly.com/urls

app_carehub = dash.Dash(__name__,suppress_callback_exceptions=True)


app_carehub.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='carehub_home')])

index_page = html.Div([
    dcc.Link('Go to iotex dashboard', href='/iotex'),
    html.Br(),
    dcc.Link('Go to carewell dashboard', href='/carewell'),
])

# Update the index
@app_carehub.callback(Output('carehub_home', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/iotex':
        return data_viz_iotex.app_iotex_layout
    elif pathname == '/carewell':
        return ft_usage.app_carewell_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here
    return index_page
if __name__ == '__main__':
    app_carehub.run_server(debug=True)

    