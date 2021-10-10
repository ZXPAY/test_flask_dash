#https://github.com/shkiefer/dash_in_flask_msal/tree/msal_login/app/dashapps
import dash
import pandas as pd
import plotly.express as px
from flask import render_template
import dash_bootstrap_components as dbc
from dashapps import dashapp1, dashapp2, dashapp3, bp

@bp.route("/")
def test_index():
    return "Dashboard main page"


@bp.route("/dash")
def test_dash1():
    return render_template("dashapp1.html", dash1_url=dashapp1.URL_BASE
                                            , dash2_url=dashapp2.URL_BASE
                                            , dash3_url=dashapp3.URL_BASE
                                            , min_height=500)
