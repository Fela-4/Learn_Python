import dash
import dash_bootstrap_components as dbc
from dash import dcc as dcc
from dash import html as html
from dash.dependencies import Input, Output
from dash_bootstrap_components._components.Col import Col

import numpy as np
import plotly.express as px
import pandas as pd
from datetime import datetime

from app_contents import new_df1,new_df2,new_df3,place_list,place_list2,place_list3,df,df2,df3


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [   dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "Covid19 Global Cases",
                        className="text-center text-info",
                    )
                )
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="Dpdwn",
                            options=[{"label": v, "value": v} for v in place_list],
                            value=place_list[0],
                        ),
                        dcc.Graph(id="grph", figure={}),
                    ],
                    width={"size": 5},
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="Dpdwn2",
                            options=[{"label": x, "value":x} for x in place_list2],
                            value=place_list2[0],
                        ),
                        dcc.Graph(id="grph2", figure={}),
                    ],
                    width={"size": 5},
                ),
            ], justify="around"),

        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                        id="Dpdwn3",
                        options=[{"label": x, "value":x} for x in place_list2],
                        value=place_list2[0],
                    ),
                   dcc.Graph(id="grph3", figure={}),
                ],width={"size": 5},
            ),
        ], justify='center')
    ]
)


@app.callback(Output("grph", "figure"), Input("Dpdwn", "value"))
def update_grph(place):
    print()
    series = new_df1.loc[place]
    x = np.array(series.index)
    y = np.array(series)

    figure = {
        "data": [
            {"x": x, "y": y, "type": "line", "name": "SF"},
        ],
        "layout": {"title": "Covid Confirmed Cases"},
    }

    return figure

@app.callback(Output("grph2", "figure"), Input("Dpdwn2", "value"))
def update_grph(place):
    print()
    series = new_df2.loc[place]
    x = np.array(series.index)
    y = np.array(series)

    figure = {
        "data": [
            {"x": x, "y": y, "type": "line", "name": "SF"},
        ],
        "layout": {"title": "Covid Recovered Cases"},
    }

    return figure

@app.callback(Output("grph3", "figure"), Input("Dpdwn3", "value"))
def update_grph(place):
    print()
    series = new_df3.loc[place]
    x = np.array(series.index)
    y = np.array(series)

    figure = {
        "data": [
            {"x": x, "y": y, "type": "line", "name": "SF"},
        ],
        "layout": {"title": "Covid Total Deaths Per Regions"},
    }

    return figure


if __name__ == "__main__":
    app.run_server(debug=True, port=3000)