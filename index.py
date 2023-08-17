import discord
import requests
import os
from discord import app_commands


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1055272833590235237))
            self.synced = True
        print(f"bot logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="Ping the bot to see if it's actually online", guild=discord.Object(id=1055272833590235237))
async def self(interaction: discord.Interaction):
    print(f"sent ping message to guild {interaction.guild_id} (name: {interaction.guild.name})")
    await interaction.response.send_message("Pong")

@tree.command(name="dogphoto", description="Send a random dog photo", guild=discord.Object(id=1055272833590235237))
async def self(interaction: discord.Interaction):
    apiResponse = requests.get("https://dog.ceo/api/breeds/image/random")
    if apiResponse.status_code == 200:
        print("response recieved from api")
    else:
        print("unexpected error")
        await interaction.response.send_message("unexpected error, error code", apiResponse.status_code)
    embedResponse = discord.Embed(title="Here is a cute dog photo!",color=0x295A99)
    embedResponse.set_image(url=apiResponse.json()['message'])
    print(f"sent dog photo to {interaction.guild_id} (name: {interaction.guild.name})")
    await interaction.response.send_message(embed=embedResponse)

@tree.command(name="catphoto", description="Send a random cat photo", guild=discord.Object(id=1055272833590235237))
async def self(interaction: discord.Interaction):
    apiResponse = requests.get("https://api.thecatapi.com/v1/images/search")
    if apiResponse.status_code == 200:
        print("response recieved from api")
    else:
        print("unexpected error")
        await interaction.response.send_message("unexpected error, error code", apiResponse.status_code)
    embedResponse = discord.Embed(title="Here is a cute cat photo!",color=0xB05F25)
    embedResponse.set_image(url=apiResponse.json()[0]['url'])
    print(f"sent cat photo to {interaction.guild_id} (name: {interaction.guild.name})")
    await interaction.response.send_message(embed=embedResponse)

@tree.command(name="foxphoto", description="Send a random fox photo", guild=discord.Object(id=1055272833590235237))
async def self(interaction: discord.Interaction):
    apiResponse = requests.get("https://randomfox.ca/floof/")
    if apiResponse.status_code == 200:
        print("response recieved from api")
    else:
        print("unexpected error")
        await interaction.response.send_message("unexpected error, error code", apiResponse.status_code)
    embedResponse = discord.Embed(title="Here is a cute fox photo!",color=0xAB3124)
    embedResponse.set_image(url=apiResponse.json()['image'])
    print(f"sent cat photo to {interaction.guild_id} (name: {interaction.guild.name})")
    await interaction.response.send_message(embed=embedResponse)

@tree.command(name="dadjoke", description="Send a random dad joke", guild=discord.Object(id=1055272833590235237))
async def self(interaction: discord.Interaction):
    apiResponse = requests.get(headers={'Accept': 'application/json'},url="https://icanhazdadjoke.com/")
    if apiResponse.status_code == 200:
        print("response recieved from api")
    else:
        print("unexpected error")
        await interaction.response.send_message("unexpected error, error code", apiResponse.status_code)
    embedResponse = discord.Embed(title="Here is a hillarious joke!",color=0x5A2387)
    embedResponse.set_image(url=(f"https://icanhazdadjoke.com/j/{apiResponse.json()['id']}.png"))
    print(f"sent dad joke to {interaction.guild_id} (name: {interaction.guild.name})")
    await interaction.response.send_message(embed=embedResponse)

# disabled this command
#@tree.command(name="chucknorris", description="chuck norris", guild=discord.Object(id=1055272833590235237))
#async def self(interaction: discord.Interaction):
#    apiResponse = requests.get("https://api.chucknorris.io/jokes/random")
#    if apiResponse.status_code == 200:
#        print("response recieved from api")
#    else:
#        print("unexpected error")
#        await interaction.response.send_message("unexpected error, error code", apiResponse.status_code)
#    embedResponse = discord.Embed(title="chuck norris",color=0xAB3124,description=apiResponse.json()['value'])
#    print(f"sent chuck norris to {interaction.guild_id} (name: {interaction.guild.name})")
#    await interaction.response.send_message(embed=embedResponse)

client.run(os.environ['DISCORD_BOT_TOKEN'])
