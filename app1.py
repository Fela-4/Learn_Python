import dash
from dash import dcc as dcc
from dash import html as html
from dash.dependencies import Input , Output


import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

colors = {
    'text': '#800000'
    
}

app.layout = html.Div([
                html.H1('Covid Cases Confirmed Globally',
                style ={
                        'textAlign': 'center',
                        'color': colors['text']
                }
                
                )
            ]),
            html.Div([
                dcc.Dropdown(
                     id='drpdwn-1',
                     options=[{'label': x , 'value': x} for x in ],
                     value=''
                )



])

if __name__ == '__main__':
    app.run_server(debug=True,port =3000)