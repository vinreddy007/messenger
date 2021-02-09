"""
Analyzes groupchats
"""
import pandas
import plotly.express as px
import plotly.graph_objects as go
from python.analysis.constants import *

MESSAGE_LENGTH = 'Total characters sent'

# Total messages from each friend in either dm or group chat
# fig = go.Figure([go.Bar(x=data[SENDER].value_counts()[:15].index,
#                         y=data[SENDER].value_counts()[:15].values)])
# fig.show()


def messages_by_month(messages: pandas.DataFrame):
    """
    Area chart over time of messages sent by month
    """
    messages[DATE] = messages[DATE].apply(lambda x: pandas.to_datetime(x))
    messages['Count'] = 1
    counts = pandas.DataFrame(index=messages[DATE], data=messages['Count'].to_numpy()).resample('W').count()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=counts.index, y=counts.iloc[:, 0], fill='tozeroy', mode='none'))
    fig.update_yaxes(title_text='Messages')
    fig.update_xaxes(title_text='Date')
    fig.layout.update(title_text='Messages by month')
    fig.show()


def message_split(messages: pandas.DataFrame):
    """
    Pie chart containing split of messages sent for group chat
    """
    messages[MESSAGE_LENGTH] = messages[CONTENT].apply(lambda x: len(x))
    total_chars_sent = messages.groupby(SENDER).sum().sort_values(MESSAGE_LENGTH, ascending=False)[:15]
    fig = px.pie(total_chars_sent.reset_index(), values=MESSAGE_LENGTH, names=SENDER)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()


group_chat_name = "../../processed_messages/group_chats/a_gentlemans_club.csv"
data = pandas.read_csv(group_chat_name)
messages_by_month(data.copy(deep=True))
message_split(data.copy(deep=True))



