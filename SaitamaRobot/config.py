# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2530486 # integer value, dont use ""
    API_HASH = "532ad7e9f870d49b8fa02284119c35ca"
    TOKEN = "BOT_TOKEN"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 884031659  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Goku_kun"
    SUPPORT_CHAT = 'GokuSupport'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001342399214  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001403508256  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "m6PlSL7hjmWXcOeAhKFXTE7s61Gu3S~eGojGFx3Cq5iseeGgFvGW55rm~WSOHdce"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 0  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgUAAx0CSKEfxgACCdlgRdI76BEQj2uFN7B3EX8YSvjzHQADAwACqaQ2Mb9tAuBEgcy7HgQ'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'S1GU5TMBG6AFQIXD'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'XD9FU8JEEWSF'  # Get your API key from https://timezonedb.com/api
    WALL_API = ''  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '80fa9ee6b189a7f1b23117006e62db210c23b9ef8aa30898bbd16b0df6d3067cefad1814c6f5cdadc0c66eebdf5d39dd2bbd305dbfc39c14a9169dc7415dd785'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    '''
    Use this if you are using REDIS Sever ->
    REDIS_URL = redis://you-server@redis.blabla.com:1080 #1080 is port number
    '''

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
