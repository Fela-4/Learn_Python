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

from app_contents import CONFIRMED, DEATHS, RECOVERED, make_dt_list
from ui_components import dropdown_graph


def main():
    url_dict = {
        CONFIRMED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        DEATHS: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        RECOVERED: "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
    }

    df_dict = {k: pd.read_csv(v) for k, v in url_dict.items()}
    dt_list_dict = {k: make_dt_list(df) for k, df in df_dict.items()}

    # TODO make the place_list_dict using functions from app_contents

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    app.layout = dbc.Container(
        [
            dbc.Row(
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
                    dropdown_graph(place_list_dict[CONFIRMED]),
                    dropdown_graph(place_list_dict[DEATHS]),
                ],
                justify="around",
            ),
            dbc.Row(
                [dropdown_graph(place_list_dict[RECOVERED])],
                justify="center",
            ),
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

    return app


if __name__ == "__main__":
    app = main()
    app.run_server(debug=True, port=3000)
