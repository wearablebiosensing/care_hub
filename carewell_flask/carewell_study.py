import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import gspread as gs

card_content1 = [
    # dbc.CardHeader("IoTex"),
    dbc.CardBody(
        [
            html.H5("Feasiability Study", className="card-title"),
            html.P(
                "A Smart Glove Digital Health Platform for Monitoring Parkinsons Disease Symptoms",
                className="card-text",
            ),
            dbc.CardLink("Go to Feasiability Study dashboard", href="/carewell-ftusage"),

        ]
    ),
]
card_content2 = [
    # dbc.CardHeader("Carewell"),
    dbc.CardBody(
        [
            html.H5("Beta Study", className="card-title"),
            html.P(
                "A Digital Health Platform for Caregivers of Dementia Patients",
                className="card-text",
            ),
        dbc.CardLink("Go to carewell dashboard", href="/carewell"),
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

app_carewell_layout = html.Div([
    dbc.Container(dbc.Row(dbc.Col([cards_carewell])), id="cards_project_nav"),
    # dcc.Graph(id='indicator-graphic-carewell'),
    html.Div(id='carewell_dash')
])