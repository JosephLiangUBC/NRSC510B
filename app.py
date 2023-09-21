import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# Initialize Dash app
app = dash.Dash(__name__)

# Read data from SQLite database
conn = sqlite3.connect('c_elegans_data.db')
df = pd.read_sql_query("SELECT * FROM experiment_data", conn)
conn.close()

# Create an initial plot
fig = px.scatter(df, x="time", y="dura")
scatter_fig = px.scatter(df, x="time", y="dura")
histogram_fig = px.histogram(df, x="speed")
gene_counts = df['Gene'].value_counts().reset_index()
gene_counts.columns = ['Gene', 'count']
bar_fig = px.bar(gene_counts, x='Gene', y='count')

# Define Dash layout
app.layout = html.Div([
    dcc.Dropdown(
        id='yaxis-column',
        options=[{'label': col, 'value': col} for col in ['dura', 'dist', 'prob', 'speed']],
        value='dura'
    ),
    dcc.Graph(id='scatter-plot', figure=fig)
])

app.layout = html.Div([
    dcc.Dropdown(
        id='yaxis-column',
        options=[{'label': col, 'value': col} for col in ['dura', 'dist', 'prob', 'speed']],
        value='dura'
    ),
    dcc.Graph(id='scatter-plot', figure=scatter_fig),
    dcc.Graph(id='histogram-plot', figure=histogram_fig),
    dcc.Graph(id='bar-plot', figure=bar_fig)
])

# Define callback for updating graph
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('yaxis-column', 'value')]
)
def update_scatter_plot(yaxis_column_name):
    return px.scatter(df, x="time", y=yaxis_column_name)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
