import dash
import dash_bootstrap_components as dbc
from dash import dcc as dcc
from dash import html as html
from dash.dependencies import Input , Output
from dash_bootstrap_components._components.Col import Col

import plotly.express as px
import pandas as pd

df = pd.read_csv('test.csv')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
                dbc.Row([
                    dbc.Col(html.H1("Covid19 Cases Confirmed Global", className='text-center text-info'))
                ]),

                dbc.Row([
                    dbc.Col([
                    dcc.Dropdown(id='Dpdwn', multi = False , value='Algeria',
                                     options=[{'label' : x, 'value' : x }
                                     for x in sorted (df['Country/Region'].unique())]),
                    dcc.Graph(id='grph' , figure={})                  
                ], width={'size' : 5}),

             ])
])

# @app.callback(
#      Output('grph','figure'),
#      Input('Dpdwn','value')
# )

# def update_grph(Country_name): 
#      dff = df[df['Country']==Country_name]
#      figln = px.line(dff,  x='Date', y=)
if __name__ == '__main__':
    app.run_server(debug=True, port=3000)