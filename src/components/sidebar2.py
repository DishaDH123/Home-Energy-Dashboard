import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab2 import TAB2_DROPDOWN,tab2_selector,date_picker,choice
from data.data import energy_df_full

SIDEBAR2 = [dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px","padding-left": "10px","padding-top": "10px"}),
dbc.Row("___________________________________________"),
html.Br(),
dbc.Row("This part of the dashboard explores energy usage over time in the home. You can choose date range from the dropdown below. You can also explore what the weather was doing during the same time frame using the Climate Factor dropdown. ",class_name="description"),
html.Br(),
dbc.Label("Choose Date Range:",class_name="sub_title_2",style={"font-size":"20px"}),
html.Br(),
dbc.Row(date_picker),
html.Br(),
dbc.Label("Choose Climate Factor:",class_name="sub_title_2",style={"font-size":"20px"}),
html.Br(),
dbc.Row(choice),
# html.Br(),
# dbc.Row(TAB2_DROPDOWN),
# html.Br(),
# dbc.Row(tab2_selector),



]



@app.callback(
    Output('selection_tab2', 'options'),
    Input('tab2_dropdown', 'value'))
def set_checkbox2(tab2_dropdown):
    if tab2_dropdown==1:
        return [{'label': i, 'value': i} for i in energy_df_full['outside_humidity_status'].unique()]
    elif tab2_dropdown==2:
        return [{'label': i, 'value': i} for i in energy_df_full['outside_temperature_status'].unique()]
    elif tab2_dropdown==3:
        return [{'label': i, 'value': i} for i in energy_df_full['windspeed_status'].unique()]
