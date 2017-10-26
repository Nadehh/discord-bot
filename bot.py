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

    chatMessage = message.content.lower().split()

    try:
        if message.content[0]=="!": #check if its a command we want to listen to, then we check against our commands

            if chatMessage[0]=="!hello":
                await client.send_message(message.channel,"hello! I am weather bot :) type !commands for my functionality!")


            elif chatMessage[0] == "!commands":

                await client.send_message(message.channel,"Command1: !temperature\nCommand2: !weather\nCommand3: !weatherdetail\nCommand4: !humidity\nCommand5: !windspeed\n\nMore specific search: Dublin,ie etc")



            elif chatMessage[0]=="!weather":

                weatherBasic = weather.getWeatherStatus(chatMessage[1])
                await client.send_message(message.channel,weatherBasic)



            elif chatMessage[0]=="!weatherdetail":

                weatherDetail = weather.getWeatherStatusDetail(chatMessage[1])
                await client.send_message(message.channel,weatherDetail)



            elif chatMessage[0]=="!temperature":

                temp = weather.getTemperature(chatMessage[1])
                await client.send_message(message.channel,temp)

            elif chatMessage[0]=="!humidity":
                humidity = weather.getHumidity(chatMessage[1])
                await client.send_message(message.channel,humidity)

            elif chatMessage[0]=="!windspeed":
                windspeed = weather.getWindSpeed(chatMessage[1])
                await client.send_message(message.channel,windspeed)
    except AttributeError as invalid:

        await client.send_message(message.channel,invalid)
