import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
fontawesome_stylesheet = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, fontawesome_stylesheet])

#app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the automobiles data into pandas dataframe
z_Feature_Airbags =  pd.read_csv('z_Feature_Airbags.csv', 
                            encoding = "ISO-8859-1",
                            )
z_Feature_Climate_Or_Infotainment =  pd.read_csv('z_Feature_Climate_Or_Infotainment.csv', 
                            encoding = "ISO-8859-1",
                            )
z_Feature_Exterior_Equipment =  pd.read_csv('z_Feature_Exterior_Equipment.csv', 
                            encoding = "ISO-8859-1",
                            )
z_Feature_Paint_Type =  pd.read_csv('z_Feature_Paint_Type.csv', 
                            encoding = "ISO-8859-1",
                            )         
z_Feature_Upholstery_Fabric =  pd.read_csv('z_Feature_Upholstery_Fabric.csv', 
                            encoding = "ISO-8859-1",
                            )
z_Feature_Interior_Equipment =  pd.read_csv('z_Feature_Interior_Equipment.csv', 
                            encoding = "ISO-8859-1",
                            )
top_rated_brands =  pd.read_csv('top_rated_brands.csv', 
                            encoding = "ISO-8859-1",
                            )
top_rated_Modelo =  pd.read_csv('top_rated_Modelo.csv', 
                            encoding = "ISO-8859-1",
                            )       
top_rated_bodytype =  pd.read_csv('top_rated_bodytype.csv', 
                            encoding = "ISO-8859-1",
                            )     
z_Feature_Front =  pd.read_csv('z_Feature_Front.csv', 
                            encoding = "ISO-8859-1",
                            )       
z_Feature_Rear =  pd.read_csv('z_Feature_Rear.csv', 
                            encoding = "ISO-8859-1",
                            )   
Top_Weekday =  pd.read_csv('Top_Weekday.csv', 
                            encoding = "ISO-8859-1",
                            )      
Precio_Coche_mes =  pd.read_csv('Precio_Coche_mes.csv', 
                            encoding = "ISO-8859-1",
                            )     
location =  pd.read_csv('location.csv', 
                            encoding = "ISO-8859-1",
                            )                      
warehouse =  pd.read_csv('warehouse.csv', 
                            encoding = "ISO-8859-1",
                            )  
color =  pd.read_csv('color.csv', 
                            encoding = "ISO-8859-1",
                            )  

class switch:

	def __init__(self, variable, comparator=None, strict=False):
		self.variable = variable
		self.matched = False
		self.matching = False
		if comparator:
			self.comparator = comparator
		else:
			self.comparator = lambda x, y: x == y
		self.strict = strict

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def case(self, expr, break_=False):
		if self.strict:
			if self.matched:
				return False
		if self.matching or self.comparator(self.variable, expr):
			if not break_:
				self.matching = True
			else:
				self.matched = True
				self.matching = False
			return True
		else:
			return False

	def default(self):
		return not self.matched and not self.matching
    
    
def picking_plot(option):
    def uno_ing():
            return z_Feature_Airbags.sort_values(by=["Count"],ascending=False)

    def dos_ing():
            return z_Feature_Paint_Type.sort_values(by=["Count"],ascending=False)

    def tres_ing():
            return z_Feature_Exterior_Equipment.sort_values(by=["Count"],ascending=False)

    def cuatro_ing():
            return z_Feature_Interior_Equipment.sort_values(by=["Count"],ascending=False)

    def cinco_ing():
            return z_Feature_Upholstery_Fabric.sort_values(by=["Count"],ascending=False)
    def seis_ing():
            return z_Feature_Climate_Or_Infotainment.sort_values(by=["Count"],ascending=False)
    def siete_ing():
            return top_rated_brands.sort_values(by=["Count"],ascending=False)
    def ocho_ing():
            return top_rated_Modelo.sort_values(by=["Count"],ascending=False)
    def nueve_ing():
            return top_rated_bodytype.sort_values(by=["Count"],ascending=False)
    def diez_ing():
            return z_Feature_Front.sort_values(by=["Count"],ascending=False)
    def once_ing():
            return z_Feature_Rear.sort_values(by=["Count"],ascending=False)
    def doce_ing():
            return Top_Weekday.sort_values(by=["Count"],ascending=False)
    def trece_ing():
            return Precio_Coche_mes
    def catorce_ing():
            return location.sort_values(by=["Count"],ascending=False)
    def quince_ing():
            return warehouse.sort_values(by=["Count"],ascending=False)
    def dieciseis_ing():
            return color.sort_values(by=["Count"],ascending=False)
    def error():
        print('error')

    get_horas_ing = {
        "Arb": uno_ing,
        'PT': dos_ing,
        'EE': tres_ing,
        'IE': cuatro_ing,
        'UF': cinco_ing,
        'CI': seis_ing,
        'TB': siete_ing,
        'TM': ocho_ing,
        'TBO': nueve_ing,
        'Fr': diez_ing,
        'Re': once_ing,
        'TW': doce_ing,
        'TPr': trece_ing,
        'Loc': catorce_ing,
        'War': quince_ing,
        'color': dieciseis_ing,
    }
    def error():
        print('error')

    #tomamos la función asociada a la variable y la invocamos
    return get_horas_ing.get(option, error)()



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, fontawesome_stylesheet])

card3 = dbc.Card([
        dbc.CardBody([
                html.H4("Vehicle Production", className="card-title"),
                html.P(
                    "Ukraine Crisis Impact",
                    className="card-value",
                ),
                html.P(
                    "Also affects Turkey",
                    className="card-target",
                ),
                html.Span([
                    html.I(className="fas fa-arrow-circle-down down"),
                    html.Span("15% less cars will be make in Europe in the first half of this year",
                    className="down")
                ])
            ])
        ])
card = dbc.Card([
        dbc.CardBody([
                html.H4("Vavacars Performance", className="card-title"),
                html.P(
                    "9535",
                    className="card-value",
                ),
                html.P(
                    "Sold cars",
                    className="card-target",
                ),
                html.Span([
                    html.Span("From October 2021 to April 2022",
                    className="mid")
                ])
            ])
        ])                                                                                        
card2 = dbc.Card([
        dbc.CardBody([
                html.H4("Sell Performance per week", className="card-title"),
                html.P(
                    "101.9",
                    className="card-value",
                ),
                html.P(
                    "More cars sold per week in this year vs last year.",
                    className="card-target",
                ),
                html.Span([
                    html.I(className="fas fa-arrow-circle-up up"),
                    html.Span("426.3 weekly cars sold on average, increasing 31.5% last year results",
                    className="up")
                ])
            ])
        ])  
card4 = dbc.Card([
        dbc.CardBody([
                html.H4("Sell Performance per day", className="card-title"),
                html.P(
                    "62",
                    className="card-value",
                ),
                html.P(
                    "Cars sold per day (average)",
                    className="card-target",
                ),
                html.Span([
                    html.I(className="fas fa-arrow-circle-up up"),
                    html.Span("That is 11.8 more cars sold per day in 2022 vs 2021",
                    className="up")
                ])
            ])
        ])      
                            
app.layout = html.Div(children=[ html.Div(html.Img(src=app.get_asset_url('vavacars.png'), style={'height':'10%', 'width':'10%'})),
                                # html.H2('Car ', 
                                # style={'textAlign': 'center', 'color': '#503D36',
                                # 'font-size': 35}),
                                html.Div([
                                       html.Div(card3),
                                        html.Div(card),
                                        html.Div(card2),
                                        html.Div(card4),
                                ], style={'width':'100%','display': 'flex'}),#'margin-right': '20em','margin-left': '35em','margin-left': '1.5em'
                                html.Br(), #style={'margin-right': '2em','font-size': 20}
                                html.Br(), #style={'margin-right': '2em','font-size': 20}
                                html.Br(), #style={'margin-right': '2em','font-size': 20}
                               html.H2('Car Automobile Top Rated Features', 
                                style={'color': '#008838','textAlign': 'center', #'color': '#503D36',
                                'font-size': 35}),

                                html.Br(),
                                html.Div([html.H2('Feature Type:', style={'color': '#02B3D5'}), dcc.Dropdown(options=[#, style={'color': '#02B3D5'}
            {'label': 'Airbags', 'value': 'Arb'},
            {'label': 'Paint Type', 'value': 'PT'},
            {'label': 'Exterior Equipment', 'value': 'EE'},
            {'label': 'Interior Equipment', 'value': 'IE'},
            {'label': 'Upholstery Fabric', 'value': 'UF'},
            {'label': 'Climate Or Infotainment', 'value': 'CI'},
            {'label': 'Brand', 'value': 'TB'},
            {'label': 'Model', 'value': 'TM'},
            {'label': 'Body Type', 'value': 'TBO'},
            {'label': 'Front', 'value': 'Fr'},
            {'label': 'Rear', 'value': 'Re'},
            {'label': 'Top weekday', 'value': 'TW'},
            {'label': 'Montly Income Sales', 'value': 'TPr'},
            {'label': 'Location with most cars', 'value': 'Loc'},
             {'label': 'Warehouse with most cars', 'value': 'War'},
             {'label': 'Colors', 'value': 'color'},
        ],value='Arb', id='input-wheels',style={'textAlign':'center','height':'40px', 'font-size': 20,'width':350}),], 
                                style={'margin-right': '2em','font-size': 20}),
                                html.Div([
                                        html.Div(dcc.Graph(id='pie1-plot')),
                                        html.Div(dcc.Graph(id='bar2-plot')),
                                ], style={'display': 'flex'}),
                                ])

# add callback decorator
@app.callback( [Output(component_id='pie1-plot', component_property='figure'),Output(component_id='bar2-plot', component_property='figure')],#viene conjuntamente con la funcion de abajo, la cual tiene como parametro
               Input(component_id='input-wheels', component_property='value'))#como parametro input el input componente id indicado, y de output, lo que se retorna en la funcion

# Add computation to callback function and return graph
def get_graph(entered_wheel):
    # Select 2019 data
    df =picking_plot(entered_wheel)

    if entered_wheel=='TB' or entered_wheel=='TM':#primera condicion debido a que no quiero meter todos ya que habrian muchisimas barras entonces hafgo un head
        fig2 = px.bar(df.head(14), x=df.columns.values.tolist()[0], y="Count", title='Top Rated '+df.columns.values.tolist()[0]) 

        fig = px.pie(df.head(14), values="Count", names=df.columns.values.tolist()[0], title='Top Rated '+df.columns.values.tolist()[0]) 


    elif entered_wheel=='TPr':#segunda condicion cuando pongo precio es distinto ya que no saco pie por ejemplo
        fig = px.line(df, x="Sales_month", y="price",width=600, height=400,title="Avarage Income Sales by Month")
        
        fig.update_traces(mode="markers+lines")
        fig.update_traces(line_color='#101820', line_width=3)
        #df=df.sort_values(by=["price"],ascending=False)
        fig2 = px.bar(df.head(14), x="Sales_month", y="price", title='Top Income Sales by month') 
        for i in range(len(fig2.data)):
            fig2.data[i].marker.line.width = 4
            fig2.data[i].marker.line.color = "#0085CA"  
            fig2.data[i].marker.color = "#101820"

        return[fig,fig2]


    elif entered_wheel=='color':#tercera condicion porque le cambio el color a las barras
        fig = px.pie(df, values="Count", names=df.columns.values.tolist()[0], title='Top Rated '+df.columns.values.tolist()[0]) 
        fig.update_traces(marker=dict(colors=df['hexcolor']))

        colors1=df["hexcolor"].values.tolist()


        fig2 = go.Figure(data=[go.Bar(
            x=df['color'], y=df['Count'],
            marker_color=colors1[:]

        )])
        fig2.update_layout(title_text='Top Rated Car Colors')
        return[fig,fig2]


    else:#por aqui entraria todo lo demás
        fig2 = px.bar(df, x=df.columns.values.tolist()[0], y="Count", title='Top Rated '+df.columns.values.tolist()[0]) 
        fig = px.pie(df, values="Count", names=df.columns.values.tolist()[0], title='Top Rated '+df.columns.values.tolist()[0]) 

    

    for i in range(len(fig2.data)):
        fig2.data[i].marker.line.width = 4
        fig2.data[i].marker.line.color = "#0085CA"  
        fig2.data[i].marker.color = "#101820"
    

    fig.update_traces(marker=dict(colors=['#101820', '#0085CA','#BFC0BF','#DFF3FD', '#001489','#A71930','#FFB612','#002C5F','#125740','#69BE28','#97233F','#203731','B3995D','FFB612','#FB4F14']))

    return [fig, fig2]

    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8056)