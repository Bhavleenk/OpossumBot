import os
import discord
import requests  #to get data from api it is for http
import json
import random
from replit import db

my_secret = os.environ['TOKEN']

intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
print(my_secret)

sad_words = [
  "sad", "depressed", "unhappy", "miserable", "angry", "depressing", "regret",
  "regretful", "dejected", "sorrowful", "down", "downhearted", "despairing",
  "heartbroken", "heart broken", "inconsolable", "mournful"
]

starter_encouragements = [
  "Cheer up!", "Hang in there.", "You are a great person/bot!","Tomorrow will be easier!"]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0][
    'a']  #q stands for quote it i sthe value
  return (quote)

def update_encouragements(encouraging_messages):
  if "encouragements" in db.keys():
    encouragements=db['encouragemnets']
    encouragemnets.append(encouraging_messages)
    db["encouragements=encouragements"]
  else:
    db["encouragements"] = [encouraging_messages]

  def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements)>index :
      del encouragemnets[index]
    db["encouragements"]=encouragements
  
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if message.content == 'inspire':
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choices(starter_encouragements))


client.run(my_secret)


