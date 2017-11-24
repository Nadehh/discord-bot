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

    result=None
    chatMessage = message.content.lower().split()

    try:
        if message.content[0]=="!": #check if its a command we want to listen to, then we check against our commands

            if chatMessage[0]=="!hello":
                result = "hello! I am weather bot :) type !commands for my functionality!"


            elif chatMessage[0] == "!commands":

                result = "Command1: !temperature\nCommand2: !weather\nCommand3: !weatherdetail\nCommand4: !humidity\nCommand5: !windspeed\n\nMore specific search: Dublin,ie etc"


            elif chatMessage[0]=="!weather":

                result = weather.getWeatherStatus(chatMessage[1])


            elif chatMessage[0]=="!weatherdetail":

                result = weather.getWeatherStatusDetail(chatMessage[1])


            elif chatMessage[0]=="!temperature":

                result = weather.getTemperature(chatMessage[1])


            elif chatMessage[0]=="!humidity":

                result = weather.getHumidity(chatMessage[1])


            elif chatMessage[0]=="!windspeed":

                result = weather.getWindSpeed(chatMessage[1])


            elif chatMessage[0]=="!cloudcoverage":

                result = weather.getCloudCoverage(chatMessage[1])

            if result: #checking against invalid command
                await client.send_message(message.channel,result)

    except ValueError as invalid:

        await client.send_message(message.channel,invalid)
        

client.run(" DISCORD BOT KEY ")
