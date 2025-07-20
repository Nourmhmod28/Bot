import os
from os import getenv

from dotenv import load_dotenv

load_dotenv("sample.env")

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8036362196:AAGTTY6lSm06_fSajull3j8eEXUkKOa8EXs")

    APP_ID = int(os.environ.get("APP_ID", 28668915))
    
    API_HASH = os.environ.get("API_HASH", "eab516f19b155a1b7755a9f4bb6047ba")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1411672636))
    
    Devs = [1405636280,1411672636]
    
    

