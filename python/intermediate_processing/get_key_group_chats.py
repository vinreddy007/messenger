import json
import os
import datetime
import csv
"""
Key group chats
1. Xanada
2. Bros after trains
3. Pong Bros
4. Naked Cowboys
5. Hinge
6. A gentleman's club
"""


def get_group_chat(gc_dir: str, gc_name: str):
    with open(gc_name, mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Date', 'Sender', 'Content', 'Type'])

        for filename in os.listdir(gc_dir):
            if filename.startswith("message"):
                data = json.load(open(os.path.join(gc_dir, filename), "r"))
                for message in data["messages"]:
                    try:
                        date = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1000)
                        sender = message["sender_name"]
                        content = message["content"]
                        type = message["type"]
                        writer.writerow([date, sender, content, type])

                    except KeyError:
                        pass


get_group_chat('../../raw_messages/inbox/xanadatrip2k_ja1fp4tymg', '../../processed_messages/group_chats/xanada.csv')
get_group_chat('../../raw_messages/inbox/brosaftertrains_hfhgiqwqxg', "../../processed_messages/group_chats/bros_after_trains.csv")
get_group_chat('../../raw_messages/inbox/pongbros__kqumv0dew', "../../processed_messages/group_chats/pong_bros.csv")
get_group_chat('../../raw_messages/inbox/nakedcowboys_kb2rrj2dhq', "../../processed_messages/group_chats/naked_cowboys.csv")
get_group_chat('../../raw_messages/inbox/hinge_uoqt0kewug', "../../processed_messages/group_chats/hinge.csv")
get_group_chat('../../raw_messages/inbox/agentlemansclub_3vr7umlkkw', "../../processed_messages/group_chats/a_gentlemans_club.csv")


