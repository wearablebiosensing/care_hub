import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback,State
from dash_bootstrap_components._components.Container import Container
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json
import glob
from sklearn import preprocessing
# Own imports
from util_dash_components import *
from iotex_data_analysis import data_viz_iotex 
from carewell_flask.carewell_FT_data import ft_usage 
import gspread as gs

## FOLLOWED -- Multistaged plotly app tutorials https://dash.plotly.com/urls

app_carehub = dash.Dash(__name__,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app_carehub.layout = html.Div( 
   [
    dcc.Location(id='url', refresh=False),
    html.Div(id='carehub_home',)
    ],
)
# Layout for carehub home page.
index_page = html.Div(children=[
    dbc.Container(dbc.Row(dbc.Col([navbar])), id="nav_bar"),
    html.Br(), 
    dbc.Container(dbc.Row(dbc.Col([cards])), id="cards_project_nav"),
])

# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


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
    #return app_carehub.layout

if __name__ == '__main__':
    app_carehub.run_server(debug=True)

    