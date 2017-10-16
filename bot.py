import discord
import asyncio
import os
import shelve

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    print("Logged in? ", client.is_logged_in)

    print("SERVERS:\n")
    print("*"*8)
    for server in client.servers:
        print(server)
    print("*"*8)


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await client.send_message(message.channel,"hi there mate this is a robot")
