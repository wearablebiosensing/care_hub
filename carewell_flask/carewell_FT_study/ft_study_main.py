import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import gspread as gs

card_content1 = [
    dbc.CardBody(
        [
            html.H5("Links Group", className="card-title"),
            html.P(
                "FT Study Links Group Data",
                className="card-text",
            ),
            dbc.CardLink("Go to Links Group dashboard", href="/carewell-ftlinksgroup"),

        ]
    ),
]
card_content2 = [
    dbc.CardBody(
        [
            html.H5("App Group", className="card-title"),
            html.P(
                "BT study App Group Data",
                className="card-text",
            ),
        dbc.CardLink("Go to carewell dashboard", href="carewell-ftappgroup"),
        ]
    ),
]
row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content1, color="", outline=True)),
        dbc.Col(dbc.Card(card_content2, color="", outline=True)),
    ],
    className="mb-4",
)
row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content1, color="", outline=True)),
        dbc.Col(dbc.Card(card_content2, color="", outline=True)),
    ],
    className="mb-4",
)

cards_carewell = html.Div([row_1])

app_ft_study_carewell_layout = html.Div([
    dbc.Container(dbc.Row(dbc.Col([cards_carewell])), id="cards_project_nav"),
    html.Div(id='carewell_dash')
])