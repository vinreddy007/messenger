import json
import os
import datetime
import csv
"""
Key group chats
1. Xanada
2. Bros after trains
3. Every combination containing Sasha and Leo
4. Pong Bros
"""

directory = 'messages/inbox/XanadaTrip2k_jA1FP4tyMg'

with open("xanada.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Sender', 'Content', 'Type'])

    for filename in os.listdir(directory):
        if filename.startswith("message"):
            data = json.load(open(os.path.join(directory, filename), "r"))
            for message in data["messages"]:
                try:
                    date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                    sender = message["sender_name"]
                    content = message["content"]
                    type = message["type"]
                    writer.writerow([date, sender, content, type])

                except KeyError:
                    pass

directory = 'messages/inbox/Brosaftertrains_HfhgIQWqxg'
with open("bros_after_trains.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Sender', 'Content', 'Type'])

    for filename in os.listdir(directory):
        if filename.startswith("message"):
            data = json.load(open(os.path.join(directory, filename), "r"))
            for message in data["messages"]:
                try:
                    date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                    sender = message["sender_name"]
                    content = message["content"]
                    type = message["type"]
                    writer.writerow([date, sender, content, type])

                except KeyError:
                    pass

directory = 'messages/inbox/pongbros__kquMV0DEw'
with open("pong_bros.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Sender', 'Content', 'Type'])

    for filename in os.listdir(directory):
        if filename.startswith("message"):
            data = json.load(open(os.path.join(directory, filename), "r"))
            for message in data["messages"]:
                try:
                    date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                    sender = message["sender_name"]
                    content = message["content"]
                    type = message["type"]
                    writer.writerow([date, sender, content, type])

                except KeyError:
                    pass

directory = 'messages/inbox/NakedCowboys_kB2Rrj2dhQ'
with open("naked_cowboys.csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Sender', 'Content', 'Type'])

    for filename in os.listdir(directory):
        if filename.startswith("message"):
            data = json.load(open(os.path.join(directory, filename), "r"))
            for message in data["messages"]:
                try:
                    date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                    sender = message["sender_name"]
                    content = message["content"]
                    type = message["type"]
                    writer.writerow([date, sender, content, type])

                except KeyError:
                    pass
