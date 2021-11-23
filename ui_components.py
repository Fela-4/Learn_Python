import dash_bootstrap_components as dbc
import dash_core_components as dcc


def dropdown_graph(place_list: list):
    return dbc.Col(
        [
            dcc.Dropdown(
                id="Dpdwn",
                options=[{"label": v, "value": v} for v in place_list],
                value=place_list[0],
            ),
            dcc.Graph(id="grph", figure={}),
        ],
        width={"size": 5},
    )
