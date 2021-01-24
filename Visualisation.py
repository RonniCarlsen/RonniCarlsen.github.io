import numpy as np
import pandas as pd
import glob
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import os.path

## Import the csv-file into Python.
KCLT = pd.read_csv('.\\us-weather-history\\KCLT.csv', sep = ',')
# print(KCLT)
# print(KCLT.info())
# print(KCLT.describe())

## Change the 'date' from string to DateTime.
# KCLT['date'] = pd.to_datetime(KCLT['date'])
# print(KCLT.dtypes)

## Converts date into a date index
# KCLT.index = KCLT.date


## Looking for missing data in the dataFrame.
# for col in KCLT.columns:
#     pct_missing = np.mean(KCLT[col].isnull())
#     print('{} - {}%'.format(col, round(pct_missing*100)))

# Looking for Null-values in the dataFrame.
# print(KCLT.isnull().sum())

## Creates heatmap of the dataFrame
# fig = go.Figure(
#             go.Heatmap(
#                 x=KCLT.columns,
#                 y=KCLT.columns,
#                 z=KCLT.corr(),
#                 colorscale='RdBu',
#                 reversescale=True, zmid=0
#             )
#         )
# fig.update_layout(title="KCLT")
#
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'KCLT_heatmap.html'))


##Create scatter line plot of actual temp, min, mean, max (WORKING)
#
# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_max_temp,
#         name='Max',
#         line=dict(color='firebrick', width= 4, dash= 'dot')
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_mean_temp,
#         #line_color='',
#         name='Mean'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_min_temp,
#         name='Min',
#         line=dict(color='royalblue', width= 4, dash= 'dot')
#     )
# )
#
# fig.update_layout(title='Temperature measured at the KCLT weather station ',
#                     yaxis_title='Temperature (degrees F)')
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'temp_min_max_avg_scatter.html'))



## Plotting record and average precipitation as a scatter plot (WORKING)

# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#     x= KCLT.date,
#     y=KCLT.record_precipitation,
#     mode='lines+markers',
#     line_color='firebrick',
#     name='Highest amount of rain or snow on that day since 1880'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#     x= KCLT.date,
#     y=KCLT.average_precipitation,
#     mode='lines+markers',
#     line_color='royalblue',
#     name='Average amount of rain or snow on that day since 1880'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#     x= KCLT.date,
#     y=KCLT.actual_precipitation,
#     mode='lines+markers',
#     line_color='#0DAB76',
#     name='Measured amount of rain or snow for that day'
#     )
# )
# fig.update_yaxes(title_text='rain/snow')
# fig.update_layout(
#                 font=dict(
#                     size=14,
#                     ),
#                 title_text='Precipitation of July 2014 to July 2015'
#                 )
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'record_average_precipitation_scatter.html'))


## Plotting record_min_temp and record_max_temp (WORKING, needs detailing)

# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.record_max_temp,
#         mode='lines+markers',
#         line_color='firebrick',
#         name='record_max_temp'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.record_min_temp,
#         mode='lines+markers',
#         line_color='royalblue',
#         name='record_max_temp'
#     )
# )
#
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'temp_min_max_record_scatter.html'))

## box plot and scatter plot of record precipitation (WORKING, Ved ikke hvad jeg skal med plottet(indsæt et box plot over average også))
# fig = go.Figure()
# fig.add_trace(
#              go.Box(
#              y=KCLT.record_precipitation,
#             name='record_precipitation',
#             boxpoints='all',
#             jitter=0.5,
#             whiskerwidth=0.2,
#             marker_size=2,
#             line_width=1
#             )
#         )
# fig.show()
# df_max = KCLT.groupby(['record_max_temp_year'], as_index=True)[['record_max_temp_year']].count()
# df_min = KCLT.groupby(['record_min_temp_year'], as_index=True)[['record_min_temp_year']].count()'
df_max = KCLT.set_index(['record_max_temp_year']).count(level='record_max_temp_year')
print(df_max.info())
print(df_max)

#
# fig = go.Figure()
# fig.add_trace(
#             go.Bar(
#                 x=KCLT.record_max_temp_year,
#                 y=df_max[],
#                 marker_color='firebrick',
#                 name='Maximum temperature records'
#
#             )
# )
# fig.add_trace(
#             go.Bar(
#                 x=KCLT.record_min_temp_year,
#                 y=df_min[],
#                 marker_color='royalblue',
#                 name='Minimum temperature records'
#
#             )
# )
#
# fig.update_yaxes(title_text='Amount of records measured')
# fig.update_xaxes(title_text='Year of record')
# fig.update_layout(
#                 font=dict(
#                     size=14,
#                     ),
#                 title_text='Year and occurence of minimum and maximum records at KCLT',
#                 barmode='group'
#                 )
#
# fig.show()
