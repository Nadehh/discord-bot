import discord
import asyncio
import requests
from weatherUpdate import WeatherUpdate

client = discord.Client()
weather = WeatherUpdate("API KEY")


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

    chatMessage = message.content[1:].split()

    if message.content[0]=="!":

        if chatMessage[0]=="hello":
            await client.send_message(message.channel,"hello! I am weather bot :) type !commands for my functionality!")


        elif chatMessage[0] == "commands":

            await client.send_message(message.channel,"Command1: temperature\nCommand2: weather\nCommand3: weatherdetail")


        elif chatMessage[0]=="weather":

            await client.send_message(message.channel,chatMessage[1]+": "+weather.getWeatherStatus(chatMessage[1]))

        elif chatMessage[0]=="weatherdetail":

            await client.send_message(message.channel,chatMessage[1]+": "+weather.getWeatherStatusDetail(chatMessage[1]))

        elif chatMessage[0]=="temperature":
            await client.send_message(message.channel,chatMessage[1]+": "+weather.getTemperature(chatMessage[1]+" degrees Celcius"))
