from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymongo as pymongo
import certifi
import os

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

# Connection to DB
link = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}"
print(link)
client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}", tlsCAFile=certifi.where())
# DB Collection
db = client["OP-TCG-DB"]

app = FastAPI()

origins = ['https://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['GET'],
    allow_headers = ['*']
)

@app.get("/all")
async def all_cards():
    cards = db.card.find({},{"_id":0})
    cardString = ""
    for card in cards:
        cardString += f"{card},"
    return cardString

@app.get("/card/{name}")
async def get_query(name):
    return {"Name": f"{name}"}

@app.get("/set/{name}")
async def get_query(name):
    name = name.upper()
    cards = db.card.find({"set_id":f"{name}"},{"_id":0})
    cardString = ""
    for card in cards:
        cardString += f"{card},"
    return cardString

@app.get("/count")
def get_card_count(apiKey, count):
    cardCount = db.card.count_documents({})
    return {"Cards in DB": cardCount}
