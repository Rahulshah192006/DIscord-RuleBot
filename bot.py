import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")
Token = open("Token","r")
Token = Token.read()
@client.event
async def Ready():
    print("Bot is online")

R = open("Rules","r")
rules = R.readlines()

@client.command()
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])


client.run(Token)