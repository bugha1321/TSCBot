import discord 
from discord.ext import commands

client = commands.Bot(command_prefix= "$")
client.remove_command("help")

@client.event
async def on_ready():
    print("TECH.CORD Online")

@client.command()
async def Info(ctx):
    await ctx.channel.send("Test")

client.run("MTAwNDczODk0MDcwOTkwODQ5MA.G-DCy7.54wiLgXO-7JJHEgYpjimASB1eh2279vRnNvEKA")
