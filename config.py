"""

from os import getenv


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "")) "22746239"))
API_HASH = environ.get("API_HASH", "")

"""




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", ""))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("TesttxcorestBot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "5840594311"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", ".")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", ""))

