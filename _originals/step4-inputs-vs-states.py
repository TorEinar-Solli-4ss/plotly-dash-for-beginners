from dash import Dash, html, dcc, callback, Input, State, Output
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1('Inputs vs states', className='mt-4'),
    html.P('The button reads the number only when clicked.', className='hint'),
    html.Div([
        dbc.Label('Enter number:', html_for='my_input'),
        dbc.Input(id='my_input', type='number', value=0, style={'maxWidth': '200px'}),
    ], className='mb-3'),
    html.Div([
        dbc.Button('Click me', id='my_button', className='me-2'),
        dbc.Button('Click me too :)', id='my_second_button', color='secondary'),
    ], className='mb-3'),
    html.Div(id='button_output', className='mb-3'),
    dbc.Fade(
        dbc.Card(
            dbc.CardBody(
                html.P('This content fades in and out', className='card-text')
            )
        ),
        id='my_fade',
        is_in=False,
        appear=False,
    ),
], className='py-3')

@callback(
    Output('button_output', 'children'),
    Input('my_button', 'n_clicks'),
    State('my_input', 'value'),
    prevent_initial_call=True
)
def button_clicked(n_clicks, input_value):
    return f'Button clicked {n_clicks} times, input value is {input_value}'

@callback(
    Output('my_fade', 'is_in'),
    Input('my_second_button', 'n_clicks'),
    State('my_fade', 'is_in'),
    prevent_initial_call=True
)
def second_button_clicked(n_clicks, is_in):
    return not is_in

if __name__ == '__main__':
    app.run(debug=True, port=8060)