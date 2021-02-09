"""
Filled area chart of messages over time, binned by month
Tracks all messages I sent to any chat
"""
import pandas
import plotly.graph_objects as go
from python.analysis.constants import *


def messages_over_time(messages: pandas.DataFrame):
    messages['Count'] = 1
    counts = pandas.DataFrame(index=messages[DATE], data=messages['Count'].to_numpy()).resample('M').count()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=counts.index, y=counts.iloc[:, 0], fill='tozeroy', mode='none'))
    fig.update_yaxes(title_text='Messages')
    fig.update_xaxes(title_text='Date')
    fig.layout.update(title_text='Messages by month')
    fig.show()
# fig.write_image(f'{OUTPUT_PATH}/messages_over_time.png')


# Parse the first column as a pandas.Timestamp object
data = pandas.read_csv(ALL_MESSAGES_PATH, parse_dates=[0])
my_messages = data[data[SENDER] == MY_NAME]

messages_over_time(my_messages)
