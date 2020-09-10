import discord
from credentials import login

TOKEN = login['token']
client = discord.Client()
war_blake_gif = 'https://media.tenor.com/images/00f4180cbc0fb6d745f28c1bc8b64955/tenor.gif'

@client.event
async def on_message(message):
  # Prevents the bot from executing it's own commands
  if message.author == client.user:
    return

  if message.content.startswith('!bro'):
    if 'blake' in message.content.lower():
      await message.channel.send(war_blake_gif)


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------------')

client.run(TOKEN)