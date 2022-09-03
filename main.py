import glob
import os
import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output
from DRMS import df, t


fig2 = px.pie(df[0], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig4 = px.pie(df[1], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig5 = px.pie(df[2], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig6 = px.pie(df[3], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig7 = px.pie(df[4], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig8 = px.pie(df[5], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])
fig9 = px.pie(df[6], values='No. of Stations', names='date', hole=0.56,
              color_discrete_sequence=["#4AA96C", "#EB5353"])

fig2.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)

fig4.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)
fig5.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)
fig6.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)
fig7.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)
fig8.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)
fig9.update_layout(
    plot_bgcolor='#5B4B8A',
    annotations=[dict(text=' Out Of ' + str(t), x=0.5, y=0.5, font_size=10.5, showarrow=False)]
)

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([

    html.Div([
        html.H1("Dashboard For Real Time Monitoring")

    ], id="header", className="row flex-display", style={"margin-bottom": "5px"}),

    html.Div([
        html.Div([
            html.H2('SYNOP'),
            dcc.Graph(id="synop", animate=True),
            dcc.Interval(
                id='interval-component',
                interval=20 * 1000,  # in milliseconds
                n_intervals=0,
                disabled=False,
                max_intervals=-1
            ),

        ], className="create_container3 twelve columns", style={'margin-bottom': '20px', "margin-top": "20px"}),

    ], className="row flex-display"),

    html.Div([
        html.Div([
            html.H2('District Rainfall Monitoring System'),

            dcc.Graph(id="24hr", figure=fig2, style={'display': 'inline-block', 'width': '48vh', 'height': '40vh'}),
            dcc.Graph(id="24hr1", figure=fig4,
                      style={'display': 'inline-block', 'width': '48vh', 'height': '40vh'}),
            dcc.Graph(id="24hr2", figure=fig5,
                      style={'display': 'inline-block', 'width': '47vh', 'height': '40vh'}),
            dcc.Graph(id="24hr3", figure=fig6,
                      style={'display': 'inline-block', 'width': '48vh', 'height': '40vh'}),
            dcc.Graph(id="24hr4", figure=fig7,
                      style={'display': 'inline-block', "margin-left": "175px", 'width': '48vh', 'height': '40vh'}),
            dcc.Graph(id="24hr5", figure=fig8,
                      style={'display': 'inline-block', 'width': '48vh', 'height': '40vh'}),
            dcc.Graph(id="24hr6", figure=fig9,
                      style={'display': 'inline-block', 'width': '48vh', 'height': '40vh'}),

        ], className="create_container2 twelve columns", style={'margin-bottom': '20px'}),

        html.Div([
            html.H2('AWS'),
            dcc.Graph(id="aws", animate=True),

            dcc.Interval(
                id='interval-component2',
                interval=20 * 1000,  # in milliseconds
                n_intervals=0,
                disabled=False,
                max_intervals=-1)

        ], className="create_container3 twelve columns"),

    ], className="row flex-display"),

], id="mainContainer", style={"display": "flex", "flex-direction": "column"})


#
@app.callback(Output('synop', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_synop(n):
    path = r'C:\Users\vishn\OneDrive\Desktop\synop2'
    csv_files = glob.glob(path + "/*.csv")
    n = len(csv_files)
    li = csv_files[n - 1:n - 1 - 144:-1]
    # print(li)
    final = []
    for file in li:
        if os.stat(file).st_size != 0:
            final.append(file)

    df_list = (pd.read_csv(file,
                           sep=';',
                           engine='python') for file in li)

    big_df = pd.concat(df_list, ignore_index=True)
    big_df = big_df.iloc[1:, :]
    big_df['date'] = pd.to_datetime(big_df['date'], dayfirst=True, errors='coerce', utc=True)
    big_df = big_df[big_df['#id'].str.startswith('42') | big_df['#id'].str.startswith('43')]
    # big_df['date'] = big_df['date'].dt.tz_convert('Asia/Kolkata')
    df = big_df.drop_duplicates()
    df_grouped = (df.groupby(['date']))['#id'].count().rename('No. of Stations').to_frame()
    dfs = df_grouped.reset_index()

    dfs['Stations'] = dfs['No. of Stations']
    dfs['Stations'] = dfs['Stations'].apply(str)
    for index, row in dfs.iterrows():
        if row['No. of Stations'] >= 250:
            dfs.at[index, 'Stations'] = '250+'
        else:
            if row['No. of Stations'] >= 150:
                dfs.at[index, 'Stations'] = '150-250'
            else:
                dfs.at[index, 'Stations'] = '0-150'
    # print(dfs)
    fig = px.bar(dfs, x='date', y='No. of Stations', color='Stations',
                 color_discrete_map={'0-150': 'red', '150-250': '#FFB200', '250+': 'green'})
    fig.update_layout(
        font_family="Montserrat Light 300", plot_bgcolor="#FEFEFE", paper_bgcolor="#FEFEFE", xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(step="all"), dict(step="day")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"))
    return fig


@app.callback(Output('aws', 'figure'),
              Input('interval-component2', 'n_intervals'))
def update_aws(n):
    path = r'C:\Users\vishn\OneDrive\Desktop\aws2'
    csv_files = glob.glob(path + "/*.csv")
    n = len(csv_files)
    li = csv_files[n - 1:n - 1 - 144:-1]
    # print(li)
    final = []
    for file in li:
        if os.stat(file).st_size != 0:
            final.append(file)

    df_list = (pd.read_csv(file,
                           sep=';',
                           engine='python') for file in li)
    # print(df_list)
    big_df = pd.concat(df_list, ignore_index=True)
    big_df = big_df.iloc[1:, :]
    big_df['date'] = pd.to_datetime(big_df['date'], dayfirst=True, errors='coerce', utc=True)
    df2 = pd.read_csv("final_aws.csv")
    df_grouped = pd.merge(big_df, df2)
    df_grouped = df_grouped[["#id", "date"]]
    df_grouped = df_grouped.drop_duplicates()

    # df_grouped['date'] = df_grouped['date'].dt.tz_convert('Asia/Kolkata')

    df_grp = (df_grouped.groupby(['date']))['#id'].count().rename('No. of Stations').to_frame()
    dfa = df_grp.reset_index()
    dfa['Stations'] = dfa['No. of Stations']
    dfa['Stations'] = dfa['Stations'].apply(str)
    for index, row in dfa.iterrows():
        if row['No. of Stations'] >= 80:
            dfa.at[index, 'Stations'] = '80+'
        else:
            if row['No. of Stations'] >= 60:
                dfa.at[index, 'Stations'] = '60-80'
            else:
                dfa.at[index, 'Stations'] = '0-60'

    fig1 = px.bar(dfa, x='date', y='No. of Stations', color='Stations',
                  color_discrete_map={'0-60': 'red', '60-80': '#FFB200', '80+': 'green'})
    fig1.update_layout(
        font_family="Montserrat Light 300", plot_bgcolor="#FEFEFE",
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(step="all"), dict(step="day")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        ))
    return fig1

if __name__ == '__main__':
    app.run_server(debug=True)
