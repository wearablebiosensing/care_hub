import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback


import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import gspread as gs
# app_carewell = dash.Dash(__name__)
# https://docs.google.com/spreadsheets/d/13OqFGn_Tcxq37e-vI8Drw41ehG2ecucDD54JuQroHX4/edit#gid=1057782302
gc = gs.service_account(filename='/Users/shehjarsadhu/Desktop/carehub-361720-ebee0b4f8dfe.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/13OqFGn_Tcxq37e-vI8Drw41ehG2ecucDD54JuQroHX4/edit#gid=1057782302')
ws = sh.worksheet('links_master_sheet')
df = pd.DataFrame(ws.get_all_records())
print("df: --- ",df.head())
patientIDs = df["PatientID"].unique().tolist()
# date_ids =  df['Dates']].unique()
print("Patient IDs", patientIDs)
# Find out number of days for each patient.

#get_top_websites(df)
card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

card1 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Card 1", className="card-title"),
                    html.P("This card has some text content", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fa fa-list", style=card_icon),
            color="primary", outline=True,
            className="bg-primary",
            style={"maxWidth": 75},
        ),
    ],
    className="mt-4 shadow",
)

app_carewell_ftappgroup_layout = html.Div([
    html.Div([
        "Bt Study Analysis"
    ]),
    dcc.Graph(id='indicator-graphic-appgroupcarewell'),
])
# Chained callback filer by patient ID and date.
@callback(
    Output('date_id_filter2', 'options'),
    Input('patient_id_filter2', 'value'))
def dates_dropdown(patient_id):
    date_id_list = df[df["PatientID"] ==patient_id]["Dates"].unique()
    return [{'label': i, 'value': i} for i in date_id_list]

# Displays graphs.
@callback(
    Output('indicator-graphic-appgroupcarewell', 'figure'),
    Input('patient_id_filter2', 'value'),
    Input('date_id_filter2', 'value'),)
def update_graph(pid,date_id):
    colorscale = [[0, 'red'],[0.1, '#1C707F'],[1, 'teal']];
    print("Patient ID selected",pid)
    df_pid = df[df["PatientID"] == pid]
    # Calculate total number of websites visited in the unique day of all the patietns.
    unique_date_list = df_pid["Dates"].unique() # get x axis i.e unique dates for that patient selected.
    count_websites_visited = [] # same length as unique_date_list.
    for i in  unique_date_list:
         print("Unique websites on that day : ",df_pid[df_pid["Dates"]==i]["URLS"].unique())
         count_websites = len(df_pid[df_pid["Dates"]==i]["URLS"].unique())
         count_websites_visited.append(count_websites)
    print("unique_date_list: ",unique_date_list)
    print("day wise count_websites_visited: ",count_websites_visited)
    # date based df 
    df_date_pid = df_pid[df_pid["Dates"]==date_id]
    fig = make_subplots(rows=4, cols=1,
        subplot_titles=("Total Number of Days for all Patients In The Study (N=11)","Websites Visited in Total for All Days \n Patient ID: " +str(pid),  "Number of Websites Visited Over All Days" , "Websites visited for Day: " + str(date_id) +  "\n Patient ID: " +str(pid)))
    fig.add_trace(go.Bar(x=pids,y=total_days_list, text=total_days_list,marker_color='teal'),
              1, 1)
    fig.add_trace(go.Histogram(x=df_pid["URLS"], marker_color='teal'),
              2, 1)
    fig.add_trace(go.Bar(x=unique_date_list,y=count_websites_visited,text= count_websites_visited,marker_color='teal'),
              3, 1)
    fig.add_trace(go.Histogram(x=df_date_pid["URLS"], marker_color='teal'),
              4, 1)       

    large_rockwell_template = dict(
    layout=go.Layout(title_font=dict(family="Rockwell")))
    fig.update_yaxes(title_text="TO DO GET FT APP GROUP USAGE DATA: Total Days of Use",title_font_family="IBM Plex San", row=1, col=1)
    #fig.update_xaxes(title = "Visited Websites",
    #title_font_family="IBM Plex San")

    fig.update_layout(
        font_family="IBM Plex Sans",
         template=large_rockwell_template,height=900, width=1500)
    return fig