from dash import Dash, State, html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define what the page looks like
app.layout = html.Div(
    [
        html.Div([
            html.H1("Hello, World!"),
            html.P("This is my first Dash app."),
        ]),
    ],
    className="page",  # page gutter + 24px between each child div, see assets/style.css
)

# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
