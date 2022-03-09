from dash import dcc
from dash import Input,Output,html
import dash_bootstrap_components as dbc
from data.data import temperature_df_full
import altair as alt
from ..app import app

alt.data_transformers.enable('data_server')
alt.data_transformers.disable_max_rows()

from .example_slider import EXAMPLE_SLIDER


def plot1_altair(temperature_df_full,xcol="day_of_week"):
    
    chart1=alt.Chart(temperature_df_full).mark_line().encode(
        x=alt.X(xcol,sort=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),
        y='mean(temperature)',
        color="room_type"
        ).properties(height=200,width=800)
    return chart1.to_html()

def plot2_altair(temperature_df_full,xcol="day_of_week"):
    chart2=alt.Chart(temperature_df_full).mark_line().encode(
        x=alt.X(xcol,sort=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),
        y='mean(humidity)',
        color="room_type"
        ).properties(height=200,width=800)
    return chart2.to_html()

plot1=html.Iframe(id='plot1',srcDoc=plot1_altair(temperature_df_full,xcol="day_of_week"),style={'width': '100%', 'height': '400px'})
plot2=html.Iframe(id='plot2',srcDoc=plot2_altair(temperature_df_full,xcol="day_of_week"),style={'width': '100%', 'height': '400px'})



TAB1 = dbc.Tab(label="House Climate", children=["The average of temperature of the selected rooms is plotted with the selected time range", 
                                                plot1,"The average of humidity of the selected rooms is plotted with the selected time range",plot2])

@app.callback(
    Output('room_selector', 'options'),
    Input('tab1_dropdown', 'value'))
def set_checkbox(tab1_dropdown):
    if tab1_dropdown==1:
        return [{'label': i, 'value': i} for i in temperature_df_full['room_type'].unique()]
    elif tab1_dropdown==2:
        return [{'label': i, 'value': i} for i in temperature_df_full['direction'].unique()]
    elif tab1_dropdown==3:
        return [{'label': i, 'value': i} for i in temperature_df_full['floor'].unique()]
    elif tab1_dropdown==4:
        return [{'label': i, 'value': i} for i in temperature_df_full['time_of_day'].unique()]

@app.callback(
    Output('plot1','srcDoc'),
    Output('plot2','srcDoc'),
    Input('tab1_dropdown','value'),
    Input('selection_tab1','value'),
    Input('time_scale', 'value'))   
def update_plot(time_scale,selection_tab1,tab1_dropdown):
    if tab1_dropdown==1:
        df1 = temperature_df_full[temperature_df_full['room_type'].isin(selection_tab1)]
        if time_scale=="full":
            a="date"
        elif time_scale=="month":
            a="month"
        elif time_scale=="daily":
            a="day_of_week"
        else:
            a="hour_of_day"
    elif tab1_dropdown==2:
        df1 = temperature_df_full[temperature_df_full['direction'].isin(selection_tab1)]
        if time_scale=="full":
            a="date"
        elif time_scale=="month":
            a="month"
        elif time_scale=="daily":
            a="day_of_week"
        else:
            a="hour_of_day"
    elif tab1_dropdown==3:
        df1=temperature_df_full[temperature_df_full['floor'].isin(selection_tab1)]
        if time_scale=="full":
            a="date"
        elif time_scale=="month":
            a="month"
        elif time_scale=="daily":
            a="day_of_week"
        else:
            a="hour_of_day"
    else:
        df1=temperature_df_full[temperature_df_full['time_of_day'].isin(selection_tab1)]
        if time_scale=="full":
            a="date"
        elif time_scale=="month":
            a="month"
        elif time_scale=="daily":
            a="day_of_week"
        else:
            a="hour_of_day"
    return plot1_altair(df1,a),plot2_altair(df1,a)

if __name__ == '__main__':
    app.run_server(debug=True)
