from datetime import datetime
import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('ready')
    while True:
        channel = client.get_channel()
        await channel.edit(name="🍀"+ datetime.now().strftime('%d.%m.%y %H:%M:%S')+"🍀")
        print('ok')
        time.sleep(6)

client.run('')