import discord
import time

# 1) need to have bot token for it to communicate with discord
# 2) Bot needs to be registered on your server
#    Link is of the form:
#    https://discordapp.com/oauth2/authorize?client_id=<BOT_ID>&scope=bot&permissions=0
def read_token():
    with open('token.txt','r') as f:
        lines= f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello")!= -1:
        await message.channel.send("Hi! \n")
        time.sleep(0.5)
        await message.channel.send("I'm BenBot!\n")
        time.sleep(0.5)
        await message.channel.send("Connection Established!")

client.run(token)
