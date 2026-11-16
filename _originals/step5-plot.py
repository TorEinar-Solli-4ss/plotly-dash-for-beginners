from dash import Dash, html, dcc, callback, Input, State, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

rng = np.random.default_rng(seed=42)
bar_fig = px.bar(
    x=['A', 'B', 'C', 'D', 'E'],
    y=rng.integers(1, 100, size=5),
    labels={'x': 'Category', 'y': 'Value'},
    color_discrete_sequence=['#00A0B0'],
)

app.layout = dbc.Container([
    html.H1('Inputs vs states', className='mt-4'),
    html.P('The button reads the number only when clicked.', className='hint'),
    html.Div([
        dbc.Label('Enter number:', html_for='my_input'),
        dbc.Input(id='my_input', type='number', value=0, style={'maxWidth': '200px'}),
    ], className='mb-3'),
    html.Div([
        dbc.Button('Click me', id='my_button', className='me-2'),
        dbc.Button('Click me too :)', id='my_second_button', className='me-2', color='secondary'),
        dbc.Button('Click me three!', id='my_third_button', className='me-2', color='secondary'),
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
    dcc.Graph(figure=None, className='mt-4', id='my_fig'),
    # dcc.Dropdown(['NYC', 'MTL', 'SF'], value=None, id='demo-dropdown', placeholder='Select a city'),
], className='py-3')

@callback(
    Output('button_output', 'children'),
    Input('my_button', 'n_clicks'),
    State('my_input', 'value'),
    prevent_initial_call=True
)
def button_clicked(n_clicks, input_value):
    return f'Button clicked {n_clicks} times, input field value is {input_value}'

@callback(
    Output('my_fade', 'is_in'),
    Input('my_second_button', 'n_clicks'),
    State('my_fade', 'is_in'),
    prevent_initial_call=True
)
def second_button_clicked(n_clicks, is_in):
    return not is_in

def create_bar_plot():
    rng = np.random.default_rng()
    fig = px.bar(
        x=['A', 'B', 'C', 'D', 'E'],
        y=rng.integers(1, 100, size=5),
        labels={'x': 'Category', 'y': 'Value'},
        color_discrete_sequence=['#00A0B0'],
    )
    return fig

@callback(
    Output('my_fig', 'figure'),
    Input('my_third_button', 'n_clicks'),
    prevent_initial_call=True
)
def third_button_clicked(n_clicks):
    return create_bar_plot()

if __name__ == '__main__':
    app.run(debug=True, port=8060)