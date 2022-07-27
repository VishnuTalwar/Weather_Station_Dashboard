import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
from aws import dfa
from synop import dfs
from DRMS import dfd

fig1 = px.bar(dfs, x='date', y='No. of Stations', title='SYNOP', color_discrete_sequence=["#000000"])
fig2 = px.pie(dfd, values='No. of Stations', names='date', title='DRMS DATA',
              color_discrete_sequence=["#000000", "#34B3F1", "#F15412","#EEEEEE"], hole=0.45)
fig3 = px.line(dfa, x='date', y='No. of Stations', title='AWS ', markers=True,
               color_discrete_sequence=["#000000"])

fig1.update_layout(
    font_family="Montserrat Light 300", plot_bgcolor="#EEEEEE", xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"))
fig2.update_layout(
    font_family="Montserrat Light 300",
    annotations=[dict(text=' Out Of 5421', x=0.5, y=0.5, font_size=15, showarrow=False)])
fig3.update_layout(
    font_family="Montserrat Light 300", plot_bgcolor="#EEEEEE",
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    ))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([

    dbc.Row(

        dbc.Col(html.H1("DASHBOARD",
                        className='text-center'),
                width=12)
    ),

    dbc.Row([

        dbc.Col([

            dcc.Graph(id="synop", figure=fig1),

        ], width={'size': 6, 'offset': 1, 'order': 1},
            xs=12, sm=12, md=12, lg=7, xl=7
        ),

        dbc.Col([
            dcc.Graph(id="24hr", figure=fig2)
        ], width={'size': 4, 'offset': 0, 'order': 2},
            xs=12, sm=12, md=12, lg=5, xl=5
        ),

    ], justify='start'),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="aws", figure=fig3),
        ],  # width={'size':5, 'offset':1},
            xs=12, sm=12, md=12, lg=12, xl=12
        ),
    ], align="center")

], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)