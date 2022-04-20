import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json

# app_carewell = dash.Dash(__name__)
df = pd.read_csv("/Users/shehjarsadhu/Desktop/UniversityOfRhodeIsland/Graduate/WBL/Project_carehub/care_hub_sandbox/carewell_flask/carewell_FT_data/Links_Master_Dates.csv")
patientIDs = df["PatientID"].unique().tolist()
# date_ids =  df['Dates']].unique()
print("Patient IDs", patientIDs)
# Find out number of days for each patient.
def get_days(df):
    total_days_list = []
    pids = []
    for i in patientIDs:
        df_patient = df[df["PatientID"]==i]
        dates_uniq = len(df_patient["Dates"].unique())
        #print("for pid ",i,"dates_uniq",dates_uniq)
        #print("Unique days: ",df_patient["Dates"].unique())
        total_days_list.append(dates_uniq)
        pids.append(i)
    return total_days_list,pids
total_days_list,pids = get_days(df)
print("total_days_list = ",total_days_list)

def get_top_websites(df):
    for i in patientIDs:
        print("PID ====",i)
        df_patient = df[df["PatientID"]==i]
        count_webhits = df_patient.groupby('URLS').nunique()#["Website"]
        print("count_webhits = \n",count_webhits,type(count_webhits))
        #count_webhits_df = count_webhits.to_frame(name=None)
       # print("count_webhits_df = ",count_webhits_df.shape,"\n",count_webhits_df.columns,"\n",type(count_webhits_df))
        #print("Website == \n",count_webhits_df["Website"],type(count_webhits_df["Website"][0]))
        #max_webhit = max(count_webhits_df)
        #print("max_webhit = ",max_webhit)

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

app_carewell_layout = html.Div([
    html.Div([
        html.Div([
            # dbc.Container(dbc.Row(dbc.Col([navbar])), id="nav_bar"),
            dcc.Dropdown(
                            id='patient_id_filter',
                            options=  [{'label': i, 'value': i} for i in patientIDs],
                            placeholder="Select Patient "
                        ),
                        dcc.Dropdown(
                            id='date_id_filter',
                            options=  [],
                            placeholder="Select Date "
                        ),
                    ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),
    #dbc.Container(dbc.Row(dbc.Col([card1])), id="card_view"),
    dcc.Graph(id='indicator-graphic-carewell'),
    html.Div(id='carewell_dash')

])
# Chained callback filer by patient ID and date.
@callback(
    Output('date_id_filter', 'options'),
    Input('patient_id_filter', 'value'))
def dates_dropdown(patient_id):
    date_id_list = df[df["PatientID"] ==patient_id]["Dates"].unique()
    return [{'label': i, 'value': i} for i in date_id_list]

# Displays graphs.
@callback(
    Output('indicator-graphic-carewell', 'figure'),
    Input('patient_id_filter', 'value'),
    Input('date_id_filter', 'value'),)
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
    fig.update_yaxes(title_text="Total Days of Use",title_font_family="IBM Plex San", row=1, col=1)
    fig.update_xaxes(title_text="Paticipant ID", title_font_family="IBM Plex San",row=1, col=1)
    fig.update_yaxes(title_text="Count of Websites visited", title_font_family="IBM Plex San",row=2, col=1)
    fig.update_xaxes(title_text="Visited Websites", title_font_family="IBM Plex San",row=2, col=1)
    fig.update_yaxes(title_text="Count of Websites visited",title_font_family="IBM Plex San", row=4, col=1)
    fig.update_xaxes(title_text="Visited Websites", title_font_family="IBM Plex San",row=4, col=1)

    #fig.update_xaxes(title = "Visited Websites",
    #title_font_family="IBM Plex San")

    fig.update_layout(
        font_family="IBM Plex Sans",
         template=large_rockwell_template,height=900, width=1500)
    return fig

# if __name__ == '__main__':
#     app_carewell.run_server(debug=True)