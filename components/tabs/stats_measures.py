from dash import html, dcc, dash_table
import plotly.express as px
import pandas as pd

def create_stats_measures_tab(df: pd.DataFrame, numeric_cols):
    return html.Div(children=[
        # Statistical Measures
        html.H5(children="Statistical Measures", className="graph-title"),
        dash_table.DataTable(
            data=df.describe().reset_index().to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'className': 'table-cell'},
            style_header={'className': 'table-header'}
        ),
        html.Br(),
        html.Hr(className="hr-style"),
        html.Br(),
        
        # Data Distribution
        html.H5(children='Data Distribution', className="graph-title"),
        dcc.Dropdown(
            options=[col for col in df.drop(['PatientId', 'AppointmentID'], axis=1).columns],
            value=[col for col in df.drop(['PatientId', 'AppointmentID'], axis=1).columns][0],
            id='SM_DROPDOWN',
            className='dropdown-style',
        ),
        html.Div(
            dcc.Graph(figure={}, id='SM_HIST'),
            className='graph-container',
        ),
        html.Br(),
        html.Hr(className="hr-style"),
        html.Br(),
        
        # Data Correlation
        html.H5(children='Data Correlation', className="graph-title"),
        html.Div(
            dcc.Graph(figure=px.imshow(
                    numeric_cols.corr(),
                    color_continuous_scale='RdBu_r',
                    zmin=-1,
                    zmax=1,
                    text_auto=True,
                    aspect="auto"
                ).update_layout(
                    xaxis_title='Features',
                    yaxis_title='Features',
                    height=600
                )
            ), className='graph-container',
        ),
        html.Br(),
        html.Hr(className="hr-style"),
        html.Br(),
        
        # Pair Plot
        html.H5(children='Pair Plot', className="graph-title"),
        html.Div(children=[
            dcc.Dropdown(
                options=[col for col in numeric_cols.columns],
                value=[col for col in numeric_cols.columns][0],
                id='SM_PP_1',
                className='dropdown-style',
                style={'flex-grow': "1"}
            ),
            dcc.Dropdown(
                options=[col for col in numeric_cols.columns],
                value=[col for col in numeric_cols.columns][1],
                id='SM_PP_2',
                className='dropdown-style',
                style={'flex-grow': "1"}
            ),
        ], className='dropdown-container'),
        html.Div(
            dcc.Graph(figure={}, id="SM_PP_GRAPH"),
            className='graph-container'
        )
    ], className="main-cont")