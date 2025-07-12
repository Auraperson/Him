from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "25580413"
# -------------------------------------------------------------
API_HASH = "f53003c5ff0fa40a25d0fe3933e21c37"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7791021817:AAFi4qoR1_3t5CHG7fYsNtuVDh9zd-dCvmQ")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://carofo7264:carofo7264@cluster0.s2ptcja.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7685184136"))
SUPPORT_GRP = "HeavenChatGroup"
UPDATE_CHNL = "AuraVisual"
OWNER_USERNAME = "UseSense"
