from dash import html, dash_table
import pandas as pd

def create_view_data_tab(df):
    return html.Div(children=[
        html.H5(children="View Data", className="graph-title"),
        dash_table.DataTable(
            data=df.to_dict('records'),
            page_size=15,
            style_table={'overflowX': 'auto'},
            style_cell={'className': 'table-cell'},
            style_header={'className': 'table-header'}
        )
    ], className="main-cont")