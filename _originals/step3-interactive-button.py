from dash import Dash, html, dcc, callback, Input, State, Output

app = Dash()

app.layout = [
    html.Div(children='Hello world'),
    html.Div([
        dcc.Button('Click me', id='my_button'),
        html.Div(id='button_output')
    ])   
]

@callback(
    Output('button_output', 'children'),
    Input('my_button', 'n_clicks'),
    prevent_initial_call=True
)
def button_clicked(n_clicks):
    return f'Button clicked {n_clicks} times'

if __name__ == '__main__':
    app.run(debug=True, port=8060)