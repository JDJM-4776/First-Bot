import discord
from bot_logic import *
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$what is your name?'):
        await message.channel.send("My name is COCO")
    elif message.content.startswith('$who is your creator?'):
        await message.channel.send("My creator is JDM-4776")
    elif message.content.startswith('$password'):
        await message.channel.send("Password generated: " + gen_pass(5))
    elif message.content.startswith("$tell me something"):
        await message.channel.send(facts())
    else:
        await message.channel.send(message.content)

client.run("el token lo tengo")
