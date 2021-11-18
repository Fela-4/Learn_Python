import dash
import dash_bootstrap_components as dbc
from dash import dcc as dcc
from dash import html as html
from dash.dependencies import Input, Output
from dash_bootstrap_components._components.Col import Col
import numpy as np

import plotly.express as px
import pandas as pd

df = pd.read_csv("test.csv")

first_4_headings = df.head().columns[:4]
# # print()

from datetime import datetime

dt_list = []

for d_str in df.head().columns[4:]:
    dt = datetime.strptime(d_str, "%m/%d/%y")
    if dt.day == 1:
        new_dt_str = f"{dt.month}/{dt.day}/{str(dt.year)[2:]}"
        dt_list.append(new_dt_str)

dt_list_list = []

for dt in dt_list:
    dt_list_list.append(np.array(df[dt]))

data_array = np.vstack(dt_list_list)

new_df = pd.DataFrame(data_array.T, columns=dt_list)

# ['Province/State', 'Country/Region', 'Lat', 'Long']

countries = list(np.array(df[first_4_headings[1]]))
provs = list(np.array(df[first_4_headings[0]]))


count_prov_list = [f"{c}: {p}".replace(": nan", "") for c, p in zip(countries, provs)]

PLACE = "Place"

place_series = pd.Series(count_prov_list, name=PLACE)


col_inx = 1

col_name = first_4_headings[1]

new_df[PLACE] = place_series.copy()


new_df = new_df.set_index(PLACE)


place_list = list(np.array(new_df.index))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "Covid19 Cases Confirmed Global",
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
                        )
                        # dcc.Graph(id="grph", figure={}),
                    ],
                    width={"size": 5},
                ),
            ]
        ),
    ]
)

# @app.callback(
#      Output('grph','figure'),
#      Input('Dpdwn','value')
# )

# def update_grph(Country_name):
#      dff = df[df['Country']==Country_name]
#      figln = px.line(dff,  x='Date', y=)
if __name__ == "__main__":
    app.run_server(debug=True, port=3000)
