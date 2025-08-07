from dash.dependencies import Input, Output

def register_navigation_callbacks(app, SM, IS, VD):
    @app.callback(
        Output('TabContent', 'children'),
        Input('NavBar', 'value')
    )
    def Navigate(tab):
        if tab == 'SM':
            return SM
        elif tab == 'IS':
            return IS
        elif tab == 'VD':
            return VD