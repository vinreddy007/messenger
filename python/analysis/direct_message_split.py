"""
Stacked Bar chart to look at the distribution of messages between me and each friend
Or plot it as a ratio, with a dashed line of 1
Average message length by person
Reactions by person
TODO: Create functions for making the charts. Call them all from a main function of sorts
"""
import pandas as pd
import numpy
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

import pandas
import plotly.express as px
import plotly.graph_objects as go
from python.analysis.constants import *
TOP_N_FRIENDS = 15
MESSAGE_LENGTH = 'Total characters sent'
FRIEND = 'Friend'

data = pandas.read_csv(DIRECT_MESSAGES_PATH, parse_dates=[0])
data[MESSAGE_LENGTH] = data[CONTENT].apply(lambda x: len(x))
top_people = data.groupby(TITLE)[MESSAGE_LENGTH].sum().sort_values(ascending=False)[:TOP_N_FRIENDS].index
data = data.groupby([TITLE, SENDER]).sum()
indexed_data = data.reindex(top_people, level=0)
data = indexed_data.reset_index()
data[SENDER] = data[SENDER].apply(lambda x: FRIEND if x != MY_NAME else x)


# DON't need the express
fig = px.bar(data, x=TITLE, y=MESSAGE_LENGTH, color=SENDER, barmode='group')
# fig.show()
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=top_people,
        y=data[data[SENDER] == FRIEND][MESSAGE_LENGTH],
        marker_color='mediumaquamarine',
        name=FRIEND
    )
)
fig.add_trace(
    go.Bar(
        x=top_people,
        y=data[data[SENDER] == MY_NAME][MESSAGE_LENGTH],
        marker_color='salmon',
        name=MY_NAME
    )
)

fig.update_layout(
    barmode='group',
    yaxis=dict(
        title='Total characters sent'
    )
)

fig.show()

# Plot of ratios
# Plot y = 1 line
ratios = numpy.zeros(TOP_N_FRIENDS)
for i, friend in enumerate(top_people):
    ratios[i] = indexed_data.loc[(friend, friend), MESSAGE_LENGTH] / indexed_data.loc[(friend, MY_NAME), MESSAGE_LENGTH]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=top_people,
        y=ratios
    )
)
# Add horizontal line at y=1 to see positive and negative ratios
fig.add_shape(
    dict(
        type="line",
        xref='paper',
        x0=0,
        y0=1,
        x1=1,
        y1=1,
        line=dict(
            color="black",
            dash="dash"
        ),
    )
)
fig.update_layout(
    yaxis=dict(
        title='Ratio of characters sent'
    )
)
fig.show()
fig.write_image(f'{OUTPUT_PATH}/direct_message_ratio.png')
