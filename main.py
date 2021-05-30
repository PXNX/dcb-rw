import os

import discord

TOKEN = "ODQ4NTgxOTk5MDAxMzM3ODU3.YLOtkg.GOEpi_3Jv6uQO6Tfb6NiPnvXflI"  # os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)
