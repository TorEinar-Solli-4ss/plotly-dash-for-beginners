from dash import Dash, html, dcc, callback, Input

app = Dash()

app.layout = [
    html.Div(children='Hello world'),
    html.Div([
        dcc.Button('Click me', id='my_button'),
    ])   
]

@callback(
    Input('my_button', 'n_clicks'),
    prevent_initial_call=True
)
def button_clicked(n_clicks):
    print(f'Button clicked {n_clicks} times')

if __name__ == '__main__':
    app.run(debug=True, port=8060)