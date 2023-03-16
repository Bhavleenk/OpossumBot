import os
import discord
import requests #to get data from api it is for http
import json

my_secret = os.environ['TOKEN']

intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
print(my_secret)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + " -" + json_data[0]['a'] #q stands for quote it i sthe value
  return quote
  

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content=='inspire':
    quote = get_quote()
    await message.channel.send(quote)



client.run(my_secret)
