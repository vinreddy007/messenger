"""
Stacked Bar chart to look at the distribution of messages between me and each friend
Or plot it as a ratio, with a dashed line of 1
Average message length by person
Reactions by person
"""

import numpy
import pandas
import plotly.graph_objects as go
from python.analysis.constants import *

TOP_N_FRIENDS = 15
MESSAGE_LENGTH = 'Total characters sent'
FRIEND = 'Friend'


class FriendSplit:
    def __init__(self, message_path=DIRECT_MESSAGES_PATH):
        data = pandas.read_csv(message_path, parse_dates=[0])
        data[MESSAGE_LENGTH] = data[CONTENT].apply(lambda x: len(x))
        self.top_friends = data.groupby(TITLE)[MESSAGE_LENGTH].sum().sort_values(ascending=False)[:TOP_N_FRIENDS].index
        data = data.groupby([TITLE, SENDER]).sum()
        self.indexed_data = data.reindex(self.top_friends, level=0)
        self.data = self.indexed_data.reset_index()
        self.data[SENDER] = self.data[SENDER].apply(lambda x: FRIEND if x != MY_NAME else x)

    def plot_top_friends(self):
        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=self.top_friends,
                y=self.data[self.data[SENDER] == FRIEND][MESSAGE_LENGTH],
                marker_color='mediumaquamarine',
                name=FRIEND
            )
        )
        fig.add_trace(
            go.Bar(
                x=self.top_friends,
                y=self.data[self.data[SENDER] == MY_NAME][MESSAGE_LENGTH],
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

    def plot_ratio_messages_sent(self):
        # Plot y = 1 line
        ratios = numpy.zeros(TOP_N_FRIENDS)
        for i, friend in enumerate(self.top_friends):
            ratios[i] = self.indexed_data.loc[(friend, friend), MESSAGE_LENGTH] / \
                        self.indexed_data.loc[(friend, MY_NAME), MESSAGE_LENGTH]

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=self.top_friends,
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


friend_split = FriendSplit(message_path=DIRECT_MESSAGES_PATH)
friend_split.plot_top_friends()
friend_split.plot_ratio_messages_sent()
