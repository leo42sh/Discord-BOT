
import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = "ScottPosey#6036"  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    var = random.randint(1, 6)
    await ctx.send(var)

@bot.event
async def on_message(message):
    if (message.content == "Salut tout le monde"):
        msg = "Salut tout seul"
        await message.channel.send(msg)
        await message.channel.send(message.author.mention)
    await bot.process_commands(message)

@bot.command()
async def count(ctx):
    i = 0
    dnd = 0
    offline = 0
    online = 0
    idle = 0
    while i < len(ctx.guild.members):
        if (str(ctx.guild.members[i].status) == "dnd"):
            dnd += 1
        if (str(ctx.guild.members[i].status) == "offline"):
            offline += 1
        if (str(ctx.guild.members[i].status) == "online"):
            online = online + 1
        if (str(ctx.guild.members[i].status) == "idle"):
            idle = idle + 1
        i = i + 1

    await ctx.send(dnd + "dnd")
    await ctx.send(offline + "offline")
    await ctx.send(online + "online")
    await ctx.send(idle + "idle")
   
    
token = ""
bot.run(token)  # Starts the bot
