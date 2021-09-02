import discord
import requests
import os
from bs4 import BeautifulSoup as bs

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

#Weather
r = requests.get("https://www.worldweatheronline.com/aizawl-weather/mizoram/in.aspx")
soup = bs(r.content,features="html.parser")

print("\nThe Temperature in Aizawl: ")
temp_celcius = soup.find("p", attrs={"class": "h3"})
temperature_string = temp_celcius.string
temperature_float = float(temperature_string[0:2])
temp_farenheit = round(((float(temperature_float) * (9/5)) + 32), 2)
print(f"In Farenheit : {temp_farenheit} °F")
print(f"In Celcius : {temp_celcius.string}")


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'fela_bot_test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '!temperature':
            await message.channel.send(f'Temperature in Aizawl:\nIn Farenheit: {temp_farenheit}°F\nIn Celcius: {temp_celcius.string}')
            return
        elif user_message.lower() == 'swag':
            await message.channel.send(f'Swaaaaaaagg!')
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return
        
client.run(TOKEN)
