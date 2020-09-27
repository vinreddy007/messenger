"""
Takes messages from all the json files and outputs to a single csv
https://towardsdatascience.com/download-and-analyse-your-facebook-messenger-data-6d1b49404e09
"""

import json
import os
import datetime
from tqdm import tqdm
import csv

directories = ["../../raw_messages/inbox", "../../raw_messages/archived_threads"]

with open("../../processed_messages/all_messages.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Sender', 'Content', 'Type'])

    for directory in directories:
        folders = os.listdir(directory)
        if ".DS_Store" in folders:
            folders.remove(".DS_Store")
        for folder in tqdm(folders):
            print(folder)
            for filename in os.listdir(os.path.join(directory, folder)):
                if filename.startswith("message"):
                    data = json.load(open(os.path.join(directory, folder, filename), "r"))
                    for message in data["messages"]:
                        try:
                            date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                            sender = message["sender_name"]
                            content = message["content"]
                            type = message["type"]
                            writer.writerow([date, sender, content, type])

                        except KeyError:
                            pass


