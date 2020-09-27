"""
Plot filled area chart of messages over time, binned by month
Tracks all messages I sent to any chat
"""
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

import pandas
import plotly
import plotly.express as px
import plotly.graph_objects as go
from python.analysis.constants import *
import plotly.figure_factory as ff

# Parse the first column as a pandas.Timestamp object
data = pandas.read_csv(ALL_MESSAGES_PATH, parse_dates=[0])
my_messages = data[data[SENDER] == "Vinay Reddy"]

# fig = px.histogram(my_messages, x=DATE, histnorm='density')
# fig.show()

# fig = ff.create_distplot([my_messages[DATE].to_list()], group_labels=['My messages'])
# fig.show()
my_messages['Count'] = 1
counts = pandas.DataFrame(index=my_messages[DATE], data=my_messages['Count'].to_numpy()).resample('M').count()
fig = go.Figure()
fig.add_trace(go.Scatter(x=counts.index, y=counts.iloc[:, 0], fill='tozeroy', mode='none'))
fig.update_yaxes(title_text='Messages')
fig.update_xaxes(title_text='Date')
fig.update_layout(title_text='Messages by month')
fig.show()
