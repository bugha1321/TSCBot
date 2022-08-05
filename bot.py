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

client.run("MTAwNTA1ODcwMzI2NDg2MjIzOQ.G9l8r2.IPMI6uIdmrnxzAGkzGwgYEJnqz0JAqpK8mBKx0")
