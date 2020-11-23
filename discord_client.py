import discord
from credentials import login
import espn_client

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
    if 'draft' in message.content.lower():
      player_name = message.content.replace('!bro draft ', '')
      player_info = espn_client.get_local_draft_info(player_name.capitalize())
      if player_info is "Undrafted":
        await message.channel.send("This player was not found in the draft meaning that they were Undrafted or you spelled their name wrong.")
        return
      embed = make_embedded_draft_info(player_info)
      await message.channel.send(embed=embed)

def make_embedded_draft_info(player_info):
    embed = discord.Embed(title="*{0}*".format(player_info["player"]))
    embed.add_field(name="Round Drafted", value=player_info["round"], inline=False)
    embed.add_field(name="Draft Pick", value=player_info["position"], inline=False)
    return embed

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------------')

client.run(TOKEN)