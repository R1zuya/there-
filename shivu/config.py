class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
     OWNER_ID="7368341648"
     SUDO_USERS="7368341648, 1102584877, 6653725844, 2107880985, 6149361523, 7013604559"
     GROUP_ID="-1001593116522"
     BOT_TOKEN="6913009476:AAE1fdTf_TvbDCBNWiAh1XyHhchpeftUez4"
     MONGO_URL="mongodb+srv://Douma:Douma@douma.yjsryni.mongodb.net"
     PHOTO_URL="url1,url2"
     SUPPORT_CHAT="Anime_chat_enigmatic"
     UPDATE_CHAT="anime_chat_enigmatic"
     BOT_USERNAME="@guess_waifu_robot" 
     CHARA_CHANNEL_ID="-1002091239384"
     API_ID="6252332"
     API_HASH="2bf5e96a75ca073fd4f37ca9562971d3"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
