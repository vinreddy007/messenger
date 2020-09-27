"""
Outputs bar chart of top people that have messaged me
"""
import pandas
import plotly
import plotly.express as px
import plotly.graph_objects as go
from python.analysis.constants import *

import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

MESSAGE_LENGTH = 'Total characters sent'

# Total messages from each friend in either dm or group chat
data = pandas.read_csv("../../processed_messages/group_chats/bros_after_trains.csv")
fig = go.Figure([go.Bar(x=data[SENDER].value_counts()[:15].index,
                        y=data[SENDER].value_counts()[:15].values)])
fig.show()

# Total messages by year
data
fig = px.histogram(data, x=DATE)
fig.show()

# Who's sent me the most characters
data[MESSAGE_LENGTH] = data[CONTENT].apply(lambda x: len(x))
total_chars_sent = data.groupby(SENDER).sum().sort_values(MESSAGE_LENGTH, ascending=False)[:15]
fig = px.bar(total_chars_sent.reset_index(), x=SENDER, y=MESSAGE_LENGTH)
fig.show()

# Take the main group chats and see the distribution of people



