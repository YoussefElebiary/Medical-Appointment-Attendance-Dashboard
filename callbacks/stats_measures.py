from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

def register_stats_measures_callbacks(app, df):
    @app.callback(
        Output(component_id='SM_HIST', component_property='figure'),
        Input(component_id='SM_DROPDOWN', component_property='value')
    )
    def draw_SM_histogram(col):
        return px.histogram(df[col])

    @app.callback(
        Output(component_id='SM_PP_GRAPH', component_property='figure'),
        Input(component_id='SM_PP_1', component_property='value'),
        Input(component_id='SM_PP_2', component_property='value')
    )
    def draw_SM_pairplot(col1, col2):
        return px.scatter(
                df,
                x=col1,
                y=col2,
            ).update_layout(
                height=600,
                showlegend=False
            )