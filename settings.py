import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# For webhook only
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

# 30 second video split size by default
SPLIT_SIZE = 30
