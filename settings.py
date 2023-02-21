import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 30 second video split size by default
SPLIT_SIZE = 30

def change_split_size(new_split_size):
    SPLIT_SIZE = new_split_size
