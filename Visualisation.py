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
#                 colorscale='BrBg',
#                 reversescale=True, zmid=0
#             )
#         )
# fig.update_layout(title="Correlation heatmap of the KCLT weather station attributes")
#
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'KCLT_heatmap.html'))

## SPLOM
# fig = go.Figure(data=go.Splom(
#                 dimensions=[dict(label='record_max_temp',
#                                  values=KCLT['record_max_temp']),
#                             dict(label='record_min_temp',
#                                  values=KCLT['record_min_temp']),
#                             dict(label='average_max_temp',
#                                  values=KCLT['average_max_temp']),
#                             dict(label='average_min_temp',
#                                  values=KCLT['average_min_temp']),
#                             dict(label='actual_max_temp',
#                                  values=KCLT['actual_max_temp']),
#                             dict(label='actual_min_temp',
#                                  values=KCLT['actual_min_temp']),
#                             dict(label='actual_mean_temp',
#                                  values=KCLT['actual_mean_temp'])],
#                 diagonal_visible=False,
#                 marker=dict(
#                     line_color='white',
#                     line_width=0.5),
#
#                 ))
#
#
# fig.update_layout(
#     title='SPLOM of the attribute with high correlation from heatmap',
#     width=1200,
#     height=750,
# )

# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'SPLOM.html'))

##Create scatter line plot of actual temp, min, mean, max and boxplot(WORKING, done)

# fig = make_subplots(rows=2,
#                     cols=1)
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_max_temp,
#         name='Max',
#         line=dict(color='firebrick', width= 4, dash= 'dot')
#         ),
#         row=1,
#         col=1
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_mean_temp,
#         marker_color='grey',
#         name='Mean'
#         ),
#         row=1,
#         col=1
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.actual_min_temp,
#         name='Min',
#         line=dict(color='royalblue', width= 4, dash= 'dash')
#         ),
#         row=1,
#         col=1
# )
#
# fig.add_trace(
#     go.Box(
#         y=KCLT.actual_max_temp,
#         boxpoints='all',
#         jitter=0.5,
#         whiskerwidth=0.2,
#         marker_size=2,
#         line_width=1,
#         marker_color='firebrick',
#         name='max',
#         showlegend=False
#         ),
#         row=2,
#         col=1
# )
#
# fig.add_trace(
#     go.Box(
#         y=KCLT.actual_mean_temp,
#         boxpoints='all',
#         jitter=0.5,
#         whiskerwidth=0.2,
#         marker_size=2,
#         line_width=1,
#         marker_color='grey',
#         name='mean',
#         showlegend=False
#         ),
#         row=2,
#         col=1
# )
# fig.add_trace(
#     go.Box(
#         y=KCLT.actual_min_temp,
#         boxpoints='all',
#         jitter=0.5,
#         whiskerwidth=0.2,
#         marker_size=2,
#         line_width=1,
#         marker_color='royalblue',
#         name='min',
#         showlegend=False
#         ),
#         row=2,
#         col=1
# )
#
# fig.update_yaxes(title='Temperature (degrees F)')
# fig.update_layout(title='Temperature measured at the KCLT weather station ')
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'temp_min_max_avg_scatter.html'))



## Plotting record and average precipitation as a scatter plot (WORKING, done)
#
# fig = go.Figure()
#
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
#     line_color='grey',
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
#
#
# fig.update_yaxes(title_text='rain/snow')
# fig.update_layout(
#                 font=dict(
#                     size=14,
#                     ),
#                 title_text='Precipitation of July 2014 to July 2015'
#                 )
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'record_average_precipitation_scatter.html'))


## Plotting record_min_temp and record_max_temp (WORKING, done)
#
# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.record_max_temp,
#         mode='lines+markers',
#         # line_color='firebrick',
#         marker=dict(
#             color=KCLT.record_max_temp,
#             colorbar=dict(
#                 title="Max temp"
#             ),
#             colorbar_x=1,
#             colorscale='reds',
#         ),
#         line=dict(
#                 color='firebrick'
#         ),
#         showlegend=False,
#         name='record max temp'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.date,
#         y=KCLT.record_min_temp,
#         mode='lines+markers',
#         # line_color='royalblue',
#         marker=dict(
#             color=KCLT.record_min_temp,
#             colorbar=dict(
#                 title="Min temp"
#             ),
#             colorbar_x=1.07,
#             colorscale='blues',
#             reversescale=True,
#
#         ),
#         line=dict(
#                 color='royalblue'
#         ),
#         showlegend=False,
#         name='record min temp'
#     )
# )
# fig.update_traces(marker_line_width=0.5)
# fig.update_yaxes(title='Temperature (degrees F)')
# fig.update_layout(title='The highest and lowest temperature measured on that day since 1880 at KCLT weather station')

# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'temp_min_max_record_scatter.html'))

## Creating bar plot of the temperature records meassured at KCLT.
#
# freq_max = KCLT.groupby(['record_max_temp_year'], as_index=False)[['record_max_temp']].count()
# freq_min = KCLT.groupby(['record_min_temp_year'], as_index=False)[['record_min_temp']].count()
#
# fig = go.Figure()
# fig.add_trace(
#             go.Bar(
#                 x=KCLT.record_max_temp_year,
#                 y=KCLT.record_max_temp,
#                 marker_color='firebrick',
#                 name='Maximum temperature records'
#
#             )
# )
# fig.add_trace(
#             go.Bar(
#                 x=KCLT.record_min_temp_year,
#                 y=KCLT.record_min_temp,
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
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'Bar_plot_min_max_records.html'))

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