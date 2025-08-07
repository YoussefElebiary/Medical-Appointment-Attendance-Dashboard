from dash import Dash, html, dcc
from data.load_data import load_data
from components.tabs.view_data import create_view_data_tab
from components.tabs.stats_measures import create_stats_measures_tab
from components.tabs.inferred_stats import create_inferred_stats_tab
# from components.tabs.report import create_report_tab
from callbacks.navigation import register_navigation_callbacks
from callbacks.stats_measures import register_stats_measures_callbacks

df, numeric_cols = load_data()

VD = create_view_data_tab(df)
SM = create_stats_measures_tab(df, numeric_cols)
IS = create_inferred_stats_tab(df)
# RP = create_report_tab(df)

# Initialize the app
app = Dash(__name__, title="Medical Appointment Analysis by Youssef Elebiary")

# Set up layout
app.layout = html.Div([
    dcc.Tabs(
        id='NavBar',
        value='SM',
        children=[
            dcc.Tab(label='Statistical Measures', value='SM'),
            dcc.Tab(label='Inferred Statistics', value='IS'),
            dcc.Tab(label='View Data', value='VD'),
            # dcc.Tab(label='Report', value='RP'),
        ],
        className='navbar'
    ),
    html.Div(id='TabContent', style={"margin-right": "0", "padding-right": "0"}),
])

# Register callbacks
register_navigation_callbacks(app, SM, IS, VD)
register_stats_measures_callbacks(app, df)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)