"""
Plot average sentiment by friend and my average sentiment over time
"""

import nltk
from python.analysis.constants import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas
import plotly.express as px
import plotly.graph_objects as go


class SentimentAnalysis:

    def __init__(self, messages):

        # Download the vader lexicon , especially suited for sentiment analysis for texting and social media
        nltk.download('vader_lexicon')

        self.messages = self._filter_non_text(messages)
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    @staticmethod
    def _filter_non_text(messages):
        """
        Filter out non-text content when TYPE is 'Call', 'Share', 'Subscribe' or 'Unsubscribe'
        i.e. calls, sharing attachments, people leaving and joining group chats
        """

        messages = messages[messages[TYPE] == 'Generic']

        return messages

    def _get_polarity(self, message):
        """
        Returns sentiment score from -1 to +1
        """
        polarity = self.sentiment_analyzer.polarity_scores(message)['compound']

        return polarity

    def plot_average_sentiments_by_friends(self, n_top_friends=25):
        """
        Plots average message sentiment for the top n friends
        """

        # Get messages from top n friends
        top_n_friends = self.messages.groupby(SENDER)[CONTENT].count().sort_values()[-n_top_friends:].index
        n_friends_messages = self.messages[self.messages[SENDER].isin(top_n_friends)]

        # Get composite sentiment score for each message
        n_friends_messages[SENTIMENT] = n_friends_messages[CONTENT].apply(self._get_polarity)

        average_sentiments = n_friends_messages.groupby(SENDER).mean().sort_values(by=SENTIMENT, ascending=False)

        fig = px.bar(average_sentiments.reset_index(), x=SENDER, y=SENTIMENT)

        return fig

    def plot_my_sentiments_over_time(self):
        """
        Plots my average message sentiment for each week
        """
        my_messages = self.messages[self.messages[SENDER] == MY_NAME]
        my_messages[SENTIMENT] = my_messages[CONTENT].apply(self._get_polarity)

        weekly_sentiments = my_messages.resample('SM', on=DATE).mean()

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=weekly_sentiments.index,
                y=weekly_sentiments[SENTIMENT],
                fill='tozeroy',
                mode='none'
            )
        )
        fig.update_yaxes(title_text='Average Sentiment')
        fig.update_xaxes(title_text='Date')
        fig.layout.update(title_text='Average Message Sentiment by Week')

        return fig


# Parse the first column as a pandas.Timestamp object
msgs = pandas.read_csv(ALL_MESSAGES_PATH, parse_dates=[0])
sentiment_analysis = SentimentAnalysis(messages=msgs)

# Show plots in browser and save to output directory as png files
sentiments_by_friend_fig = sentiment_analysis.plot_average_sentiments_by_friends(n_top_friends=25)
sentiments_by_friend_fig.show()
sentiments_by_friend_fig.write_image(f'{OUTPUT_PATH}/average_friends_sentiments.png')

sentiments_over_time_fig = sentiment_analysis.plot_my_sentiments_over_time()
sentiments_over_time_fig.show()
sentiments_over_time_fig.write_image(f'{OUTPUT_PATH}/average_sentiment_by_week.png')
