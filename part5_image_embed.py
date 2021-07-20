import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix=">", intents=intents)

@client.event
async def on_ready():
	print("Running..")

@client.command()
async def image(ctx):
	await ctx.send(file=discord.File("logo.png"))

@client.command()
async def embed(ctx):
	test_embed = discord.Embed(title="this is title", description="this is desc", color=0x28b84f)
	test_embed.add_field(name="field1", value="hello")
	test_embed.add_field(name="field2", value="world", inline=False)
	await ctx.send(embed=test_embed)


client.run("")
