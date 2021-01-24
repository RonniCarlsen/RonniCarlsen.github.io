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

## Change the 'date' from string to DateTime.
# KCLT['date'] = pd.to_datetime(KCLT['date'])
# print(KCLT.dtypes)

## Converts date into a date index
# KCLT.index = KCLT.date

## Create line plot of actual temp, min, mean, max (NOT WORKING!)

# days = list(range(1, 366, 1))
# x = KCLT.index
# x_rev = x[::-1]
#
# y1 = KCLT.actual_mean_temp
# y1_upper = KCLT.actual_max_temp
# y1_lower = KCLT.actual_min_temp
# y1_lower = y1_lower[::-1]
#
# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=x + x_rev,
#         y=y1_upper + y1_lower,
#         fill='toself',
#         fillcolor='rgba(0,100,80,0.2)',
#         line_color='rgba(255,255,255,0)',
#         name='Max/min',
#     )
# )
#
# fig.add_trace(go.Scatter(
#     x=x,
#     y=y1,
#     line_color='rgb(0,100,80)',
#     name='Mean'
# ))
#
# fig.show()

## Plotting record_min_temp and record_max_temp (WORKING, needs detailing)

# fig = go.Figure()
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.index,
#         y=KCLT.record_max_temp,
#         mode='lines+markers',
#         line_color='firebrick',
#         name='record_max_temp'
#     )
# )
#
# fig.add_trace(
#     go.Scatter(
#         x=KCLT.index,
#         y=KCLT.record_min_temp,
#         mode='lines+markers',
#         line_color='royalblue',
#         name='record_max_temp'
#     )
# )
#
# fig.show()
# fig.write_html(os.path.join(os.path.abspath('./'), 'Plots', 'temp_min_max_record_scatter.html'))


## Plotting record_min_temp_year and record_max_temp_year (NOT WORKING, needs detailing)
# record_max_freq = KCLT['record_max_temp_year'].value_counts()
# record_min_freq = KCLT['record_min_temp_year'].value_counts()
# print(len(KCLT.record_min_temp_year))
# print(len(record_min_freq))

# print(*myList, sep='\n')
# print(max(record_min_freq))
# print(record_min_freq)
# fig = go.Figure(
#     data=[
#         go.Bar(
#             name='record_max_temp',
#             x=KCLT.record_max_temp_year,
#             y=20,
#         ),
#         go.Bar(
#             name='record_min_temp',
#             x=KCLT.record_min_temp_year,
#             y=20,
#         )
#     ]
# )
#
# fig.update_layout(barmode='group')
#
# fig.show()