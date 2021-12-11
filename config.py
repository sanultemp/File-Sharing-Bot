import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2128336507:AAEK2p80aK4vnodlysHqPIxLRl16ZqkRos0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7469109"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4d4023337b8cc46c306af69adb5fc21a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001213969888"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2118362497"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://xuaugthswnujyu:590b15ba13418be84040707be1ceafa801eee70ed7131310e74a406f618f04a3@ec2-54-157-16-125.compute-1.amazonaws.com:5432/d5iiadqus3vo7t")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hi {first},\n\nI am the Flix Cinema's Requests Bot. 😊")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2118362497 1606409678 1140699369 1630262415 1834244060 1255474577 1383355894 1870040069 1783351746").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(2118362497)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
