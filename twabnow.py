import discord
from discord.ext import commands
import sqlite3


client = commands.Bot(command_prefix = "~", activity=discord.activity.Streaming(name=("created by makozort"), url="https://www.twitch.tv/makozort"))

conn = sqlite3.connect(f"./serverdata.db")  
cur = conn.cursor()



@client.event
async def on_ready():
    print("bot running on account {0.user}".format(client))
    await sendit()
    exit()



async def sendit():
  cur.execute("SELECT channelId FROM guilds;")
  result = cur.fetchall()
  for x in result:                            
    channelid = (str(x).strip("()'',"))
    if channelid != ("0"):
      print("sending twab to " + channelid)
      channel = client.get_channel(int(channelid))      # get all channel ids and if they are not 0, (blank) message them the latest twab
      with open(f"./twab.txt", 'r') as f:
        url = f.readline()

        await channel.send("A NEW TWAB JUST CAME OUT: " + (url))
client.run("")








