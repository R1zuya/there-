import os

class Config(object):
    LOGGER = True
    OWNER_ID = os.getenv("OWNER_ID")
    sudo_users = os.getenv("SUDO_USERS", "").split(",")
    GROUP_ID = int(os.getenv("GROUP_ID", 0))
    TOKEN = os.getenv("BOT_TOKEN")
    mongo_url = os.getenv("MONGO_URL")
    PHOTO_URL = os.getenv("PHOTO_URL", "").split(",")
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT")
    UPDATE_CHAT = os.getenv("UPDATE_CHAT")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    CHARA_CHANNEL_ID = int(os.getenv("CHARA_CHANNEL_ID", 0))
    api_id = int(os.getenv("API_ID", 0))
    api_hash = os.getenv("API_HASH")
