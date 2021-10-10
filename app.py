from flask import Flask
import dash

from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dashapps import dashapp1, dashapp2, dashapp3
from dashapps import bp as dashapp_bp
from flask_bootstrap import Bootstrap

server = Flask(__name__)
dashapp1.add_dash(server)
dashapp2.add_dash(server)
dashapp3.add_dash(server)

bootstrap = Bootstrap()
bootstrap.init_app(server)

server.register_blueprint(dashapp_bp, url_prefix="/dashboard")

@server.route("/")
def test_index():
    return "Main page"

if __name__ == "__main__":
    server.run(debug=True)

#url_base_pathname='/dash'

