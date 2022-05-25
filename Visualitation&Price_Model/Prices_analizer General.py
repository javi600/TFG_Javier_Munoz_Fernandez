import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
import numpy as np
from scipy import stats 
app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the automobiles data into pandas dataframe
import pickle
with open('all_info_37590_70126_V7_withincidencias.pkl', 'rb') as inp:
    df_total = pickle.load(inp)
df_total=df_total.reset_index()
del df_total['index']


import plotly.express as px
# grouping results tenerr en mente de añadir
data1 = df_total.set_index('vehicleAddedDate') 
Precio_Coche_mes=data1.resample('w').sum().loc[:,['price']].round(2)
Precio_Coche_mes=Precio_Coche_mes.reset_index()

fig = px.line(Precio_Coche_mes, x="vehicleAddedDate", y="price",title="Weekly Average Income")

fig.update_traces(mode="markers+lines")
fig.update_traces(line_color='#02B3D5', line_width=3)

data2=df_total.groupby(['transmission','Type of Fuel'])['price'].mean().round(2).reset_index()
data2=data2[(data2['transmission']!='') & (data2['Type of Fuel'] != '')]
fig2 = px.bar(data2, x="Type of Fuel", y="price",
                color="transmission", barmode = 'group',title="Price Distribution depending on fuel type and transmission")

labels=[]
for i,pos in enumerate(data2["transmission"].unique()):
        labels.append(data2[data2["transmission"]==pos]["price"].values.tolist())


for i, t in enumerate(labels):
        fig2.data[i].text = t
        fig2.data[i].textposition = 'outside'

for i in range(len(fig2.data)):
    if i==0:
        fig2.data[i].marker.line.width = 3
        fig2.data[i].marker.line.color = "rgb(55, 83, 109)"
        fig2.data[i].marker.color = "rgb(7, 183, 216)"
    elif i==1:
        fig2.data[i].marker.line.width = 3
        fig2.data[i].marker.line.color = "#007530"
        fig2.data[i].marker.color = "#51AF71"            
data3=df_total.groupby(['transmission','Wheel drive'])['price'].mean().round(2).reset_index()
data3=data3[(data3['transmission']!='') & (data3['Wheel drive'] != '')]
fig3 = px.bar(data3, x="Wheel drive", y="price",
                color="transmission", barmode = 'group',title="Price Distribution depending on Wheel Drive and transmission")

labels=[]
for i,pos in enumerate(data3["transmission"].unique()):
        labels.append(data3[data3["transmission"]==pos]["price"].values.tolist())


for i, t in enumerate(labels):
        fig3.data[i].text = t
        fig3.data[i].textposition = 'outside'

for i in range(len(fig3.data)):
    if i==0:
        fig3.data[i].marker.line.width = 3
        fig3.data[i].marker.line.color = "rgb(55, 83, 109)"
        fig3.data[i].marker.color = "rgb(7, 183, 216)"
    elif i==1:
        fig3.data[i].marker.line.width = 3
        fig3.data[i].marker.line.color = "#007530"
        fig3.data[i].marker.color = "#51AF71"    


data2=df_total.groupby(['transmission','Wheel drive'])['price'].mean().round(2).reset_index()#bodyType
data2=data2[(data2['transmission']!='') & (data2['Wheel drive'] != '')]
fig6 = px.bar(data2, x="Wheel drive", y="price",
                color="transmission", barmode = 'group')

labels=[]
for i,pos in enumerate(data2["transmission"].unique()):
        labels.append(data2[data2["transmission"]==pos]["price"].values.tolist())


for i, t in enumerate(labels):
        fig6.data[i].text = t
        fig6.data[i].textposition = 'inside'

for i in range(len(fig6.data)):
    if i==0:
        fig6.data[i].marker.line.width = 3
        fig6.data[i].marker.line.color = "rgb(55, 83, 109)"
        fig6.data[i].marker.color = "rgb(7, 183, 216)"
    elif i==1:
        fig6.data[i].marker.line.width = 3
        fig6.data[i].marker.line.color = "#007530"
        fig6.data[i].marker.color = "#51AF71"    
fig6.update_layout(barmode='stack')

data4=df_total.groupby(['Wheel drive','Type of Fuel'])['price'].mean().round(2).reset_index()

fig6.add_traces(go.Scatter(x= data2['Wheel drive'], y=data4[data4['Type of Fuel']=='Diesel'].sort_values('Type of Fuel')['price'].values.tolist(),mode='lines+markers', line=dict(color="#FFEF00"),name='Diesel'))
fig6.add_traces(go.Scatter(x= data2['Wheel drive'], y=data4[data4['Type of Fuel']=='Gasoline'].sort_values('Type of Fuel')['price'].values.tolist(),mode='lines+markers', line=dict(color="#005414"),name='Gasoline'))
fig6.add_traces(go.Scatter(x= data2['Wheel drive'], y=data4[data4['Type of Fuel']=='Hybrid'].sort_values('Type of Fuel')['price'].values.tolist(),mode='lines+markers', line=dict(color="#4D4DFF"),name='Hybrid'))
fig6.add_traces(go.Scatter(x= data2['Wheel drive'], y=data4[data4['Type of Fuel']=='Liquefied petroleum gas'].sort_values('Type of Fuel')['price'].values.tolist(),mode='lines+markers', line=dict(color="#FFC600"),name='Liquefied petroleum gas'))



df_EurTry=pd.read_csv('TurkishCurrencyRates.csv')
fig7 = px.line(df_EurTry, x="Date", y="Último",title="Weekly Average EUR-TRY RATE")

fig7.update_traces(mode="markers+lines")
fig7.update_traces(line_color='#007530', line_width=3)

app = dash.Dash()
                            
app.layout = html.Div(children=[html.Div(html.Img(src=app.get_asset_url('vavacars.png'), style={'height':'10%', 'width':'10%'})), html.H2('Price Distribution', style={ 'color': '#008838'}),#'textAlign':'center',

                                 
                                html.Div([
                                        html.Div(dcc.Graph(figure=fig3)),
                                        html.Div(dcc.Graph(figure=fig2)),
                                ], style={'display': 'flex'}),
                                html.Br(), 
                                html.Div([dcc.Graph(figure=fig6)], 
                                style={'margin-right': '2em','font-size': 20}),
                                html.Br(),
                                #html.Div([dcc.Graph(figure=fig)], 
                                #style={'margin-right': '2em','font-size': 20}),
                                html.Br(),
                                html.Div([
                                        html.Div(dcc.Graph(figure=fig)),
                                        html.Div(dcc.Graph(figure=fig7)),
                                ], style={'display': 'flex'}),
                                ])

# add callback decorator


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8058)