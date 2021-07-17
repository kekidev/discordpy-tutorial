import discord
from discord.ext import commands
import random

intents = discord.Intents.all() 

client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
	print("Running")

@client.event
async def on_message(message):
	await client.process_commands(message)
	pass 

@client.command() 
async def 골라(ctx, *, message):
	if "@everyone" in message or "@here" in message:
		return
	
	await ctx.send(random.choice(message.strip().split()))


@client.event 
async def on_member_join(member):
	channel = client.get_channel(859297198150647838)

	await channel.send(f"{member.mention}님 환영합니다")

@client.event 
async def on_member_remove(member):
	channel = client.get_channel(859297198150647838)

	await channel.send(f"{member.mention}님 잘가세요")

@client.command()
async def ping(ctx):
	await ctx.send("Pong!")

client.run("token은 여기에")