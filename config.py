# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22799061"))
API_HASH = os.environ.get("API_HASH", "7a30a19f333dedc82e5edaaee624e4e4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6115844718:AAHsG0hR28bSXQ_WG4zOqCQrC9qDTZp8MOg")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1832465028")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "pdiskshortnearn")
DATABASE_URL = os.getenv("DATABASE_URL", "dbadmin@somebody") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1832465028")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001525442971")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Pdiskshortnearn") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
