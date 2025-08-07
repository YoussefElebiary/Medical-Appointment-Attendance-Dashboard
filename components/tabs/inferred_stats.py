from dash import html, dcc
import plotly.express as px
import pandas as pd

def create_inferred_stats_tab(df: pd.DataFrame):
    df = df.copy()
    age_bins = [0, 12, 18, 30, 45, 60, 90]
    age_labels = ['0-12', '13-18', '19-30', '31-45', '46-60', '60+']
    df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
    df['DayOfWeek'] = pd.to_datetime(df['AppointmentDay']).dt.day_name()
    
    return html.Div(
        className="main-cont",
        children=[
            # Gender Pie Chart
            html.Div([
                html.H5("Appointments by Gender", className="graph-title"),
                dcc.Graph(
                    figure=px.pie(
                        df,
                        names=df['Gender'].map({'F': 'Female', 'M': 'Male'}),
                        hole=0.4,
                        color_discrete_sequence=px.colors.qualitative.Pastel
                    ).update_traces(
                        textposition='inside',
                        textinfo='percent+label'
                    ).update_layout(
                        uniformtext_minsize=12,
                        margin=dict(l=20, r=20, t=40, b=20)
                    )
                )
            ], className='graph-container'),
            
            html.Hr(className="hr-style"),
            
            # Age Group Analysis
            html.Div([
                html.H5("No-show Rate by Age Group", className="graph-title"),
                dcc.Graph(
                    figure=px.bar(
                        df.groupby('AgeGroup')['No-show'].value_counts(normalize=True).mul(100).unstack(),
                        x=age_labels,
                        y='Yes',
                        labels={'x': 'Age Group', 'Yes': 'No-show Rate (%)'},
                        text_auto='.1f',
                        color_discrete_sequence=['#EF553B']
                    ).update_layout(
                        yaxis_title='No-show Rate (%)',
                        margin=dict(l=60, r=20, t=40, b=60),
                        xaxis_tickangle=-45
                    )
                )
            ], className='graph-container'),
            
            html.Hr(className="hr-style"),
            
            # SMS Analysis
            html.Div([
                html.H5("SMS Impact on Attendance", className="graph-title"),
                dcc.Graph(
                    figure=px.bar(
                        df.groupby('SMS_received')['No-show'].value_counts(normalize=True).mul(100).unstack(),
                        x=['No SMS', 'Received SMS'],
                        y='Yes',
                        labels={'x': 'SMS Status', 'Yes': 'No-show Rate (%)'},
                        text_auto='.1f',
                        color_discrete_sequence=['#636EFA']
                    ).update_layout(
                        yaxis_title='No-show Rate (%)',
                        margin=dict(l=60, r=20, t=40, b=60)
                    )
                )
            ], className="graph-container"),
            
            html.Hr(className="hr-style"),
            
            # Day of Week Analysis
            html.Div([
                html.H5("Appointments by Weekday", className="graph-title"),
                dcc.Graph(
                    figure=px.bar(
                        df['DayOfWeek'].value_counts().reset_index(),
                        x='DayOfWeek',
                        y='count',
                        category_orders={'DayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 
                                                    'Thursday', 'Friday', 'Saturday', 'Sunday']},
                        labels={'count': 'Number of Appointments', 'DayOfWeek': ''},
                        color_discrete_sequence=['#00CC96']
                    ).update_layout(
                        margin=dict(l=60, r=20, t=40, b=60),
                        xaxis_tickangle=-45
                    )
                )
            ], className='graph-container'),
            
            html.Hr(className="hr-style"),
            
            # Handicap Analysis
            html.Div([
                html.H5("Attendance by Handicap Status", className="graph-title"),
                html.Div([
                    # Non-Handicapped
                    html.Div(
                        dcc.Graph(
                            figure=px.pie(
                                df[df['Handcap'] == 0],
                                names='No-show',
                                title='Non-Handicapped',
                                hole=0.4,
                                color_discrete_map={'Yes': '#EF553B', 'No': '#00CC96'}
                            ).update_traces(
                                textposition='inside',
                                textinfo='percent+label'
                            ).update_layout(
                                margin=dict(l=20, r=20, t=60, b=20),
                                showlegend=False
                            )
                        ),
                        className="half-width-chart"
                    ),
                    
                    # Handicapped
                    html.Div(
                        dcc.Graph(
                            figure=px.pie(
                                df[df['Handcap'] >= 1],
                                names='No-show',
                                title='Handicapped',
                                hole=0.4,
                                color_discrete_map={'Yes': '#EF553B', 'No': '#00CC96'}
                            ).update_traces(
                                textposition='inside',
                                textinfo='percent+label'
                            ).update_layout(
                                margin=dict(l=20, r=20, t=60, b=20),
                                showlegend=False
                            )
                        ),
                        className="half-width-chart"
                    )
                ], className="dual-chart-container")
            ], className='graph-container')
        ]
    )