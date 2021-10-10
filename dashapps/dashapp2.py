import dash
from dash import dcc
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

URL_BASE = '/dashboard/dashapp2/'
MIN_HEIGHT = 500

def add_dash(flask_app):
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
    ]

    app = dash.Dash(
        __name__,
        server=flask_app,
        url_base_pathname=URL_BASE,
        external_stylesheets=external_stylesheets
    )

    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [2, 2, 2, 3, 3, 3],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = dbc.Container([
        html.H1('Hello Dash 2'),
        html.Div('''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
