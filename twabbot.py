import discord
from discord.ext import commands
import sqlite3

#test



# this was made by makozort (unfortunately)


client = commands.Bot(command_prefix = "!", activity=discord.activity.Streaming(name=("created by makozort"), url="https://www.twitch.tv/makozort"))
filename = (f'./data.json')

conn = sqlite3.connect(f"./serverdata.db")  
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS guilds(
   guildId TEXT PRIMARY KEY,
   guildName TEXT,
   channelid TEXT);
""")
conn.commit()

class commands:
    

    @client.event
    async def on_ready():
        print("bot running on account {0.user}".format(client))

    @client.event
    async def on_guild_remove(guild):
        cur.execute("DELETE FROM guilds WHERE guildId = ?", [str(guild.id)]) # delete guild from database  
        conn.commit() 
        print("left " + guild.name)

        
    @client.event
    async def on_guild_join(guild):
        guilddata = (guild.id, guild.name, "0")
        cur.execute("INSERT INTO guilds VALUES(?, ?, ?);", guilddata) # add this guild to the database
        conn.commit()
        print ("added " + guild.name + " to the database")

    @client.command()
    async def setchannel(ctx):
        cur.execute('''UPDATE guilds SET channelid = ? WHERE guildId = ?''', (ctx.channel.id, ctx.guild.id))  # update channelid
        conn.commit()
        cur.execute("SELECT * FROM guilds;")
        channel = client.get_channel(ctx.channel.id)
        await channel.send("I will now post the TWAB when it comes out each week")


    @client.command()
    async def twab(ctx):
        channel = client.get_channel(ctx.channel.id)
        with open(f"./twab.txt", 'r') as f:
                url = f.readline()
                await channel.send("Here is the latest TWAB: " + (url))

    


client.run("")

