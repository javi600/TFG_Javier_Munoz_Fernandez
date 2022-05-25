import pandas as pd
import dash
from dash import html
from dash import dcc
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
with open('all_info_37590_70126_V6.pkl', 'rb') as inp:
    df_total = pickle.load(inp)
df_total=df_total.reset_index()
del df_total['index']



                                                                                            
app = dash.Dash()
                            
app.layout = html.Div(children=[html.Div(html.Img(src=app.get_asset_url('vavacars.png'), style={'height':'10%', 'width':'10%'})),html.H2('Brand Automobile Price Distribution', style={'textAlign':'center', 'color': '#008838'}),


                                html.Div([html.H2('Car Brand:', style={'color': '#02B3D5', 'margin-right': '2em'}), dcc.Dropdown(options=df_total['make'].unique().tolist(),value='Citroen', id='input-wheels',style={'textAlign':'center','height':'40px', 'font-size': 20,'width':350}),], 
                                style={'margin-right': '2em','font-size': 20}),
                                 
                                html.Div([
                                        html.Div(dcc.Graph(id='pie1-plot')),
                                        html.Div(dcc.Graph(id='bar2-plot')),
                                ], style={'display': 'flex'}),
                                html.Br(), 
                                html.H2('Model Automobile Price Distribution', 
                                style={'textAlign':'center', 'color': '#008838'}),
                                html.Div([
                                        html.Div(dcc.Graph(id='bar3-plot')),
                                        html.Div(dcc.Graph(id='bar5-plot')),
                                ], style={'display': 'flex'}),                                
                                html.Br(), 
                                html.H2('Brand Automobile automatik,manual Price comparation', 
                                style={'textAlign':'center', 'color': '#008838'}),
                                html.Div([
                                        html.Div(dcc.Graph(id='bar4-plot')),
                                        
                                ]),
                                html.Br(),
                                html.Div([
                                    html.H3('Current Month Income vs Average Month Income', 
                                style={'textAlign':'center', 'color': '#008838'}),
                                        html.Div(dcc.Graph(id='bar7-plot')),
                                        html.Div(dcc.Graph(id='bar8-plot')),
                                ], style={'display': 'flex'}), 
                                html.Br(),
                                html.H2('Brand Price Analyzer by Features, pick 1 or 2 features to be compared vs average price', style={'textAlign':'center', 'color': '#008838'}),
                                html.Div([html.H2('Comparing features', style={'color': '#02B3D5','margin-right': '2em'}), dcc.Dropdown(options=['car_seniority','transmission','Wheel drive','Type of Fuel','seatingCapacity','bodyType','Number of doors','NO_Feature1'],value='bodyType', id='input-wheels2',style={'textAlign':'center','height':'40px', 'font-size': 20,'width':350}),], 
                                style={'margin-right': '2em','font-size': 20}),
                                html.Div([html.H2('Comparing features', style={'color': '#02B3D5','margin-right': '2em'}), dcc.Dropdown(options=['car_seniority','transmission','Wheel drive','Type of Fuel','seatingCapacity','bodyType','Number of doors','NO_Feature2'],value='NO_Feature2', id='input-wheels3',style={'textAlign':'center','height':'40px', 'font-size': 20,'width':350}),], 
                                style={'margin-right': '2em','font-size': 20}),
                                html.Br(),
                                html.Div([
                                        html.Div(dcc.Graph(id='bar6-plot')),
                                        
                                ]),
                                ])

# add callback decorator
@app.callback( [Output(component_id='pie1-plot', component_property='figure'),Output(component_id='bar2-plot', component_property='figure'),Output(component_id='bar3-plot', component_property='figure'),Output(component_id='bar4-plot', component_property='figure'),Output(component_id='bar5-plot', component_property='figure'),Output(component_id='bar6-plot', component_property='figure'),Output(component_id='bar7-plot', component_property='figure'),Output(component_id='bar8-plot', component_property='figure')],#viene conjuntamente con la funcion de abajo, la cual tiene como parametro
               [Input(component_id='input-wheels', component_property='value'),Input(component_id='input-wheels2', component_property='value'),Input(component_id='input-wheels3', component_property='value')])#como parametro input el input componente id indicado, y de output, lo que se retorna en la funcion

# Add computation to callback function and return graph
def get_graph(entered_wheel,entered_wheel2,entered_wheel3):
    # Select 2019 data
    ddf=df_total[df_total['make']==entered_wheel]
    ddf = ddf[ddf['transmission'].notnull()]#this is to avoid error with graph number 4
    #ddf=ddf[ddf['model']!=""]#quito modelos sin nombre

    minn=df_total[['price']].sort_values(by=["price"],ascending=False).values.tolist()[-1]
    maxx=df_total[['price']].sort_values(by=["price"],ascending=False).values.tolist()[3]
    fig = px.box(ddf, y="price")
    fig.update_traces(fillcolor='rgb(55, 83, 109)',marker=dict(size=2,color='rgb(7, 183, 216)'))
    
    fig2 = px.histogram(ddf, x="price",nbins=18)
    fig2.update_xaxes(range = [minn[0],maxx[0]])
    for i in range(len(fig2.data)):
        fig2.data[i].marker.line.width = 3
        fig2.data[i].marker.line.color = "rgb(7, 183, 216)"
        fig2.data[i].marker.color = "rgb(55, 83, 109)"

    labels=[]
    for i,pos in enumerate(sorted(ddf['model'].unique())):
                labels.append(round(ddf[ddf["model"]==pos]["price"].mean(),2))
                labels.append(pos)
    dx= pd.DataFrame(np.asarray(labels).reshape(-1,2),columns=['price','model'])
    dx['price']=dx['price'].astype('float')
    fig3 = px.bar(dx,x="model", y="price",barmode = 'group')#,width=1450, height=605
        #fig.update_xaxes(tickvals=np.arange(7), ticktext=dx['price'].values.tolist())
    for i, t in enumerate([dx['price'].values.tolist()]):
                fig3.data[i].text = t
                fig3.data[i].textposition = 'outside'
    for i in range(len(fig3.data)):
        fig3.data[i].marker.line.width = 3
        fig3.data[i].marker.line.color = "rgb(0,80,181)"
        fig3.data[i].marker.color = "rgb(255,252,201)"

    fig4 = px.scatter(ddf[ddf['transmission'] != ''], x="year", y="price", color='mileage',facet_col="transmission",width=1450, height=555)#,width=1450, height=605

#groupby que explican estadisticos de un groupby, se explica los estadisticos de college para la columna wasitgoal
    candlestick_data = ddf.groupby(["model"], as_index=False).agg({"price": [lambda x:stats.mode(x)[0],'mean','min', 'max', 'first', 'last','sum']}).round(2)


    candlestick_data.columns.set_levels(['mode','mean','min', 'max', 'first', 'last','sum',""],level=1,inplace=True)
    candlestick_data.columns.set_levels(['price','car','Drive Type',],level=0,inplace=True)
    fig5 = go.Figure(data=[go.Candlestick(x=candlestick_data['car'],
                open=candlestick_data['price']['first'], 
                high=candlestick_data['price']['max'],
                low=candlestick_data['price']['min'], 
                close=candlestick_data['price']['last'])
                ])
    cs = fig5.data[0]

# Set line and fill colors
    cs.increasing.fillcolor = 'rgb(255,252,201)'

    cs.increasing.line.color = 'rgb(0,80,181)'
                      

    fig5.update_layout(xaxis_rangeslider_visible=False)

    
    ddf['seatingCapacity']=ddf['seatingCapacity'].astype(str)
    ddf['car_seniority']=ddf['car_seniority'].astype(str)
    if entered_wheel2=="":
        entered_wheel2="NO_Feature1"
    if entered_wheel3=="":
        entered_wheel3="NO_Feature2"
    
    
    if (entered_wheel3=="NO_Feature2" and entered_wheel2=="NO_Feature1") or (entered_wheel2==entered_wheel3):
        data2=ddf.groupby(['bodyType'])['price'].mean().round(2).reset_index()#bodyType
        data2=data2[data2['bodyType'] != '']
        fig6 = px.bar(data2, x="bodyType", y="price",
                        barmode = 'group',title="Pick at least one Feature, to get results like this one: ",width=1450, height=555)#,width=1450, height=555

        fig6.data[0].text = data2["price"].values.tolist()
        fig6.data[0].textposition = 'outside'

        for i in range(len(fig6.data)):
                fig6.data[i].marker.line.width = 4
                fig6.data[i].marker.line.color = "#008838"
                fig6.data[i].marker.color = "#02B3D5"    
    elif entered_wheel2=="NO_Feature1":
        data2=ddf.groupby([entered_wheel3])['price'].mean().round(2).reset_index()#bodyType
        data2=data2[data2[entered_wheel3] != '']
        fig6 = px.bar(data2, x=entered_wheel3, y="price",
                        barmode = 'group',width=1450, height=555)#,width=1450, height=555

        fig6.data[0].text = data2["price"].values.tolist()
        fig6.data[0].textposition = 'outside'
        for i in range(len(fig6.data)):
                fig6.data[i].marker.line.width = 4
                fig6.data[i].marker.line.color = "#008838"
                fig6.data[i].marker.color = "#02B3D5"  
        fig6.update_layout(title={'text': '<b>Results for '+str(entered_wheel)+'</b>'})
    elif entered_wheel3=="NO_Feature2":
        data2=ddf.groupby([entered_wheel2])['price'].mean().round(2).reset_index()#bodyType
        data2=data2[data2[entered_wheel2] != '']
        fig6 = px.bar(data2, x=entered_wheel2, y="price",
                        barmode = 'group',width=1450, height=555)#,width=1450, height=555

        fig6.data[0].text = data2["price"].values.tolist()
        fig6.data[0].textposition = 'outside'
        for i in range(len(fig6.data)):
                fig6.data[i].marker.line.width = 4
                fig6.data[i].marker.line.color = "#008838"
                fig6.data[i].marker.color = "#02B3D5"  
        fig6.update_layout(title={'text': '<b>Results for '+str(entered_wheel)+'</b>'})
    else:
        data2=ddf.groupby([entered_wheel2,entered_wheel3])['price'].mean().round(2).reset_index()#bodyType
        data2=data2[(data2[entered_wheel2]!='') & (data2[entered_wheel3] != '')]
        fig6 = px.bar(data2, x=entered_wheel2, y="price",
                        color=entered_wheel3, barmode = 'group',width=1450, height=555)#,width=1450, height=555

        labels=[]
        for i,pos in enumerate(data2[entered_wheel3].unique()):
                labels.append(data2[data2[entered_wheel3]==pos]["price"].values.tolist())


        for i, t in enumerate(labels):
                fig6.data[i].text = t
                fig6.data[i].textposition = 'outside'
        fig6.update_layout(uniformtext_minsize=11.5, uniformtext_mode='hide')
        colors=['#02B3D5','#008838','#101820', '#0085CA','#BFC0BF', '#001489','#A71930','#FFB612','#4f2683','#125740','#69BE28','#203731','#B3995D','#FFB612','#FB4F14','pink','brown','black','yellow','purple','green','cyan','blue','red']

        for i2,pos in enumerate(colors):
                if i2<len(data2[entered_wheel3].unique().tolist()):
                    fig6.data[i2].marker.line.width = 3
                    
                    fig6.data[i2].marker.line.color = "white"
                    fig6.data[i2].marker.color = pos
        fig6.update_layout(title={'text': '<b>Results for '+str(entered_wheel)+'</b>'})
        

    data1 = ddf.set_index('vehicleAddedDate') 
    Precio_Coche_mes=data1.resample('m').sum().loc[:,['price']].round(2)
    data1 = df_total.set_index('vehicleAddedDate') 
    Precio_Coche_mes=Precio_Coche_mes.reset_index()

    Precio_Coche_mes['year'] = pd.DatetimeIndex(Precio_Coche_mes['vehicleAddedDate']).year
    Precio_Coche_mes['month'] = pd.DatetimeIndex(Precio_Coche_mes['vehicleAddedDate']).month
    Mapping = {1 : "January",2 : "February",3 : "March",4 : "April",
            5 : "May",6 : "June",7 : "July",8 : "August",9 : "September",10 : "October",11 : "November",12 : "December"}

    Precio_Coche_mes["Month"] = Precio_Coche_mes["month"].map(Mapping)
    Precio_Coche_mes["Sales_month"]=Precio_Coche_mes["Month"]+"_"+Precio_Coche_mes["year"].astype(str)
    maxincome=max(Precio_Coche_mes['price'])
    valuemean=round(Precio_Coche_mes['price'].mean(),2)
    value=Precio_Coche_mes['price'].values.tolist()[-1]
    if value>=valuemean:
        fig7 = go.Figure(go.Indicator(
            mode = "number+gauge+delta", value = value,
            delta = {'reference': valuemean, 'position': "top"},
            gauge = {
                'shape': "angular",
                'axis': {'range': [0, maxincome]},
                'threshold': {
                    'line': {'color': "yellow", 'width': 3},
                    'thickness': 0.75, 'value': valuemean},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, maxincome], 'color': "#9DFE9D"}],
                'bar': {'color': "#00A350"}}))
    else:
        fig7 = go.Figure(go.Indicator(
            mode = "number+gauge+delta", value = value,
            delta = {'reference': valuemean, 'position': "top"},
            gauge = {
                'shape': "angular",
                'axis': {'range': [0, maxincome]},
                'threshold': {
                    'line': {'color': "yellow", 'width': 3},
                    'thickness': 0.75, 'value': valuemean},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, maxincome], 'color': "#ffcccb"}],
                'bar': {'color': "#F7330E"}}))
    fig7.add_annotation(x=valuemean/(maxincome), y=1.05,
                text="Mean Montly Average Overall",
            showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="yellow"
                ),
            align="center",
            ax=0,
            ay=0,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#ff7f0e",
            opacity=0.8
            )
    fig7.add_annotation(x=0.9, y=0,
                text="Highest Month Income",
            showarrow=True,
            font=dict(
                family="Calibri",
                size=11.15,
                color="black"
                ),
            align="center",
            arrowhead=2,
            #arrowsize=3,
            arrowwidth=1.20,
            ax=-85,
            ay=-0,
            opacity=0.65
            )

    datas=ddf.groupby(['available']).size().reset_index(name='Count')#bodyType rangoo
    df=datas.sort_values(by=["Count"],ascending=False)
    fig8 = px.pie(df, values="Count", names=df.columns.values.tolist()[0], title='Availability',hole=0.35) 
    fig8.update_traces(textfont_size=18,marker=dict(colors=['#02B3D5', '#008838']))#,line=dict(color=['white']*2, width=[0.5,0.5])

    return [fig, fig2,fig3,fig4,fig5,fig6,fig7,fig8]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)